.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0

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