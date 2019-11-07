.. ===============LICENSE_START=======================================================
.. O-RAN SC
.. %%
.. Copyright (C) 2019 AT&T Intellectual Property
.. %%
.. Licensed under the Apache License, Version 2.0 (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..      http://www.apache.org/licenses/LICENSE-2.0
..
.. Unless required by applicable law or agreed to in writing, software
.. distributed under the License is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
.. ===============LICENSE_END=========================================================

RIC APP ML Overview
======================

The O-RAN SC Machine Learning (ML) Common Services provides ML tools, adapters to integrate with a radio access network (RAN) controller.

Using Acumos ML models in the RIC:

* Goal is to support ML models in non-real time and near-real time RIC usecases.
    ** quickly import an Acumos model into RIC and adapt it into as an xApp (near-real time).
    ** deploy Acumos models as is into non-real time (mostly on ONAP side).
* Priority is to get something working with minimal changes possible on ML models
    ** focus on performance in the later releases, since many ML models take some time to execute anyway.
* Build a standard xApp/Acumos microservice adapter
    ** deployed along with the Acumos ML model in one Kubernetes pod.
* Adapter speaks RMR protocol to RIC
    ** communicates with the Acumos ML model in the standard http / GRPC manner.
* Configuration needed for each deployment
    ** to tell adapter how to speak with Acumos ML model.
    ** can be auto generated using ML model protobuf definition.
* Consider writing custom RMR model runner
    ** for performance in near-real time RIC xApps in the following releases.