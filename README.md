
Coherent Spark Runner Compiler Compatibility
============================================


The Spark team developed [`nodegen-server`](https://github.com/orgs/Coherent-Partners/packages/container/package/nodegen-server) (also referred to as the Neuron runner) to create and run containerized applications designed explicitly for executing [Wasm](https://webassembly.org/) modules generated by Spark.

This page details the compatibility between a version of the [`nodegen-server`](https://github.com/orgs/Coherent-Partners/packages/container/package/nodegen-server) against the Spark [Neuron compiler](https://docs.coherent.global/build-spark-services/neuron/release-history). The compiler version can be found from the Spark UI under the _[Service Documentation Version details](https://docs.coherent.global/navigation/service-documentation#version-details)_ or in the [_Execute API_ `response_meta`.](https://docs.coherent.global/spark-apis/execute-api/execute-api-v3#response_meta)

`nodegen-server` `1.31.0` is the first version that includes the capability and configuration for processing compatibility versions and the version compatibility mapping. However, Neuron compiled assets still do not have the Neuron version embedded and therefore the compatibility feature is still not fully functional.

The releases include the download for a JSON file mapping the compatibility versions.


# Compatibility versions


List of all released runner versions and their corresponding __highest__ supported Neuron version.
|date|runner_version|safe_compiler|
| :---: | :---: | :---: |
|2024-05-27|1.31.0|1.19.1|
|2024-05-02|1.30.0|1.18.1|
|2024-03-19|1.28.4|1.16.0|
|2024-03-18|1.29.2|1.17.0|
|2024-03-12|1.28.3|1.16.0|
|2024-03-08|1.28.2|1.16.0|
|2024-02-26|1.28.0|1.16.0|
|2024-02-15|1.27.5|1.15.2|
|2024-02-07|1.27.4|1.15.2|
|2024-02-06|1.27.3|1.15.1|
|2024-02-01|1.27.2|1.15.1|
|2024-01-29|1.27.1|1.15.1|
|2023-12-18|1.25.0|1.14.0|
|2023-10-25|1.24.0|1.13.0|
|2023-10-04|1.23.2|1.12.1|
|2023-09-25|1.23.1|1.12.0|
|2023-09-06|1.22.10|1.11.0|
|2023-09-01|1.22.9|1.11.0|
|2023-08-29|1.22.8|1.11.0|
|2023-08-01|1.22.6|1.10.1|
|2023-07-24|1.22.4|1.10.0|
|2023-07-11|1.22.3|1.9.0|
|2023-07-03|1.22.1|1.9.0|
|2023-06-26|1.21.1|1.9.0|
|2023-06-16|1.19.0|1.8.2|
|2023-05-05|1.17.0|1.6.2|
|2023-03-29|1.16.9|1.4.0|
|2023-03-27|1.16.7|1.4.0|
|2023-02-16|1.16.5|1.1.1|
|2023-01-31|1.16.2|1.1.0|
|2022-12-20|1.16.0|1.1.0|
