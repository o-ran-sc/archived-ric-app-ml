# ========================LICENSE_START=================================
#   O-RAN-SC
#   %%
#   Copyright (c) 2019 AT&T Intellectual Property.
#   %%
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#          http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ========================LICENSE_END===================================

# Adapter from RMR to standard Acumos model microservices. Must be deployed in the same pod as the Acumos model.
# Translates RMR protocol messages into calls into Acumos RPC calls.


from rmr import rmr
import time
import sys
import signal
import json
import requests

verbose = True
requireartifacts = True

confdir = '/conf/'
conffilename = 'config.json'
protobuffilename = 'model.proto'
metadatafilename = 'metadata.json'

configfilename = confdir + conffilename

if verbose:
    print("Reading config file")

# Fetch and parse config file which must be mounted as a volume during deployment
try:
    with open(configfilename) as f:
        conf = json.load(f)
except:
    print('Cannot read/parse config file at', configfilename, '; aborting')
    exit(1)

methodurl = conf['microserviceRootURL'] + conf['methodRoot']
artifacturl = conf["microserviceRootURL"] + conf['artifactRoot']

if verbose:
    print ('\nRetrieving artifacts from Acumos model microservice\n')

# See if we can retrieve protobuf and metadata artifacts from running model. Not all models may provide these, but we
# should have a retry mechanism added for robustness
try:
    r = requests.get(artifacturl + 'protobuf')
    protobuf = r.content
    with open(confdir + protobuffilename, 'wb') as f:
        f.write(protobuf)
    if verbose:
        print('Protbuf:')
        print(protobuf.decode('ascii'))
    r = requests.get(artifacturl + 'metadata')
    metadata = r.content
    with open(confdir + metadatafilename, 'wb') as f:
        f.write(metadata)
    if verbose:
        print('\nMetadata:')
        print(metadata.decode('ascii'))
except:
    if requireartifacts:
        print('Problem with retrieving/saving model protobuf and/or metadata; aborting.')

method1 = conf['methods']['1']
method1url = methodurl + method1['service']
method1headers = {'content-type': method1['content-type'], 'accept': method1['return-type']}

if verbose:
    print('\nInitializing RMR\n')

if verbose:
    print('\Awaiting connections')


# NNG cleanup on signal
def signal_handler(sig, frame):
    if verbose:
        print('SIGINT received! Cleaning up rmr')
    rmr.rmr_close(mrc)
    print("Exiting")
    sys.exit(0)


# Initialize RMR
mrc = rmr.rmr_init("4560".encode('utf-8'), rmr.RMR_MAX_RCV_BYTES, 0x00)
while rmr.rmr_ready(mrc) == 0:
    time.sleep(1)
    if verbose:
        print("Not yet ready")
rmr.rmr_set_stimeout(mrc, 2)


# Capture ctrl-c
signal.signal(signal.SIGINT, signal_handler)


sbuf = None
while True:
    if verbose:
        print("Waiting for a message; will time out after 2000ms")
    sbuf = rmr.rmr_torcv_msg(mrc, sbuf, 2000)
    summary = rmr.message_summary(sbuf)
    if verbose and summary['message state'] == 12:
        print("Nothing received.")
    else:
        if verbose:
            print("Message received: {}".format(summary))
        payload = sbuf['payload']
        # Call Acumos microservice
        r = requests.post(method1url, headers=method1headers, body=payload)
        val = r.content
        rmr.set_payload_and_length(val, sbuf)
        sbuf = rmr.rmr_rts_msg(mrc, sbuf)
