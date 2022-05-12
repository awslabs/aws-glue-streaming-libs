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

from logging import Logger

from botocore.exceptions import ClientError, NoCredentialsError


def boto_client_error(logger: Logger, message: str = ""):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ClientError as error:
                if error.response['Error']['Code'] == 'InternalError':  # Generic error
                    # We grab the message, request ID, and HTTP code to give to customer support
                    logger.error('Error Message: {}'.format(error.response['Error']['Message']))
                    logger.error('Request ID: {}'.format(error.response['ResponseMetadata']['RequestId']))
                    logger.error('Http code: {}'.format(error.response['ResponseMetadata']['HTTPStatusCode']))
                else:
                    logger.error(f"boto3 clientError raised in function {func.__name__}" + repr(error) + message)
                raise
            except NoCredentialsError as error:
                logger.error(f"boto3 NoCredentialsError raised in function {func.__name__}: {repr(error)}"
                                 f"Check if the IAM role has the right permission or if you need to increase IMDS retry.")
                raise

        return wrapper
    return decorator
