from aws_cdk import (
    # Duration,
    Stack,
    # developer import
    aws_lambda as _lambda
)
from constructs import Construct

# developer import
import os


class AuthStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        cwd = os.getcwd()
        # authentication
        app_backend_authentization = _lambda.Function(
        self, 'AppBackEndAuthentication',
        runtime=_lambda.Runtime.PYTHON_3_12,
        handler='lambda_function.handler',
        code=_lambda.Code.from_asset(os.path.join(cwd, "src/authentication")),
        # Customize the Lambda function name
        function_name='BackEndAuthentization'
        )
        #authorization
        app_backend_authorization = _lambda.Function(
        self, 'AppBackEndAuthorization',
        runtime=_lambda.Runtime.PYTHON_3_12,
        handler='lambda_function.handler',
        code=_lambda.Code.from_asset(os.path.join(cwd, "src/authorization")),
        # Customize the Lambda function name
        function_name='BackEndAuthorization'
        )
        """ 
        # example resource
        # queue = sqs.Queue(
        #     self, "AuthQueue",
        #     visibility_timeout=Duration.seconds(300),
        # ) 
        # 
        # """
