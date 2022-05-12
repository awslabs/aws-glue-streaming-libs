# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function
import platform
import pyspark
from pyspark.context import SparkContext
from pyspark.sql import SQLContext
from awsglue.context import GlueContext

sc = SparkContext()
# Change to GlueContext
# TODO: Figure out if/how to use HiveContext
glueContext = GlueContext(sc)

welcome_msg = """Welcome to
    ___ _       _______    ________
   /   | |     / / ___/   / ____/ /_  _____
  / /| | | /| / /\\__ \\   / / __/ / / / / _ \\
 / ___ | |/ |/ /___/ /  / /_/ / / /_/ /  __/
/_/  |_|__/|__//____/   \____/_/\____/\___/
"""

print(welcome_msg)
print("Using Python version %s (%s, %s)" % (
    platform.python_version(),
    platform.python_build()[0],
    platform.python_build()[1]))
print("GlueContext available as glueContext.")
