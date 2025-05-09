from constructs import Construct
from aws_cdk import (
    Stack
)
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_apigateway as apigateway

class MyCdkAppStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        table = dynamodb.Table(
            self, "MyTable",
            table_name="DemoTable", 
            partition_key=dynamodb.Attribute(
                name="id",
                type=dynamodb.AttributeType.STRING
            )
            )

        lambda_function = _lambda.Function(
            self, "MyFunction",
            function_name="TestLambda",  
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="test.lambda_handler",  
            code=_lambda.Code.from_asset("my_cdk_app/lambda/test_lambda"),
            environment={
                "DYNAMODB_TABLE": table.table_name 
            }
        )


        table.grant_read_write_data(lambda_function)

        # Create an API Gateway
        api = apigateway.RestApi(
            self, "MyApi"
        )

        # Add a POST method to the API Gateway
        items = api.root.add_resource("items")
        items.add_method(
            "POST",
            apigateway.LambdaIntegration(lambda_function)
        )