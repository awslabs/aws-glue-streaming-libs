# aws-glue-streaming-libs
AWS Glue Streaming Libraries are additions and enhancements to Spark Structured Streaming for ETL operations.

This repository contains:
* `awsglue` - the Python libary you can use to author [AWS Glue](https://aws.amazon.com/glue) Streaming ETL job. This library extends [Apache Spark](https://spark.apache.org/) with additional data types and operations for Streaming ETL workflows. It's an interface for Glue Streaming ETL library in Python.
* `bin` - this directory hosts several executables that allow you to run the Python library locally or open up a PySpark shell to run Glue Spark code interactively.


## Setup guide

If you haven't already, please refer to the [official AWS Glue Python local development documentation](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html#develop-local-python) for the official setup documentation. The following is a summary of the AWS documentation:

The `awsglue` library provides only the Python interface to the Glue Spark runtime, you need the Glue Streaming ETL jar to run it locally. The jar is now available via the maven build system in a s3 backed maven repository. Here are the steps to set up your dev environment locally.

1. install Apache Maven from the following location: https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz
1. use `copy-dependencies` target in Apache Maven to download the jar from S3 to your local dev environment.
1. download and extract the Apache Spark distribution based on the Glue version you're using:
    * Glue version 0.9: `https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-0.9/spark-2.2.1-bin-hadoop2.7.tgz`
    * Glue version 1.0: `https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-1.0/spark-2.4.3-bin-hadoop2.8.tgz1`
    * Glue version 2.0: `https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-2.0/spark-2.4.3-bin-hadoop2.8.tgz1`
    * Glue version 3.0: `https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-3.0/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3`
1. export the `SPARK_HOME` environmental variable to the extracted location of the above Spark distribution. For example:
    ```
    Glue version 0.9: export SPARK_HOME=/home/$USER/spark-2.2.1-bin-hadoop2.7
    Glue version 1.0: export SPARK_HOME=/home/$USER/spark-2.4.3-bin-hadoop2.8
    Glue version 2.0: export SPARK_HOME=/home/$USER/spark-2.4.3-bin-hadoop2.8
    Glue version 3.0: export SPARK_HOME=/home/$USER/spark-3.1.1-amzn-0-bin-3.2.1-amzn-3
    ```
1. now you can run the executables in the `bin` directory to start a Glue Shell or submit a Glue Spark application.
    ```
    Glue shell: ./bin/gluepyspark
    Glue submit: ./bin/gluesparksubmit
    pytest: ./bin/gluepytest
    ```
(The `gluepytest` script assumes that the pytest module is installed and available in the `PATH` env variable)

## Licensing

Copyright 2022 Amazon

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
