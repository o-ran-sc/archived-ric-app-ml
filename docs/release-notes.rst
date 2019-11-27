.. This work is licensed under a Creative Commons Attribution 4.0 International License.
.. SPDX-License-Identifier: CC-BY-4.0
.. Copyright (C) 2019 AT&T


Release Notes
=============


This document provides the release notes for the Amber Release of the Acumos xAPP adapter.

.. contents::
   :depth: 3
   :local:


Version history
---------------

+--------------------+--------------------+--------------------+--------------------+
| **Date**           | **Ver.**           | **Author**         | **Comment**        |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+
| 2019-11-14         | 0.0.1              |  Guy Jacobson      | First draft        |
|                    |                    |                    |                    |
+--------------------+--------------------+--------------------+--------------------+



Summary
-------

The Amber release of the Acumos xAPP adapter contains the code needed to use an existing
Acumos microservice as an O-RAN xAPP, by providing "glue" that listens and speaks RMR protocol
and translates these into calls to the Acumos microservice, which is co-deployed in the
same pod as the adapter.



Release Data
------------

+--------------------------------------+--------------------------------------+
| **Project**                          |      RAN Intelligent Controller      |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| **Repo/commit-ID**                   |              ric-app/ml              |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| **Release designation**              |                 Amber                |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| **Release date**                     |              2019-11-14              |
|                                      |                                      |
+--------------------------------------+--------------------------------------+
| **Purpose of the delivery**          | open-source adapter between Acumos   |
|                                      | and xAPPs.                           |
|                                      |                                      |
+--------------------------------------+--------------------------------------+


Components
----------

- *AcumosXappAdapter/* contains the source code and other items of interest. Under that directory :
  
  + *rmracumosadapter.py is source code for the adapter itself.
  + *iris_sklearn.py* is the source code for a generic Acumos model (iris classification).
  + *config.json*  is a sample configuration file, needed to connect the Acumos model with the xAPP adapter during deployment.
  + *Dokcerfile* is the Dockerfile that builds the xAPP adapter microservice.
  + *testdata.csv* contains sample input data to test the iris_sklearn.py classifier
 

Limitations
-----------
- This is a first release and needs some fixes to the Dockerfile to function correctly, due to
known problems with the build process to incorporate the required nng libraries.
