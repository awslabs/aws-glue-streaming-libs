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

from pyspark import SparkContext
from pyspark.sql.column import Column, _to_java_column, _to_seq

def replaceArrayElement(srcCol, replaceCol, idx):
    sc = SparkContext._active_spark_context
    jsrcCol, jreplaceCol = _to_java_column(srcCol), _to_java_column(replaceCol)
    return Column(sc._jvm.gluefunctions.replaceArrayElement(jsrcCol, jreplaceCol, idx))

def namedStruct(*cols):
    sc = SparkContext._active_spark_context
    if len(cols) == 1 and isinstance(cols[0], (list, set)):
        cols = cols[0]
    jc = sc._jvm.gluefunctions.namedStruct(_to_seq(sc, cols, _to_java_column))
    return Column(jc)

def explodeWithIndex(col):
    sc = SparkContext._active_spark_context
    jc = sc._jvm.gluefunctions.explodeWithIndex(_to_java_column(col))
    return Column(jc).alias('index', 'val')