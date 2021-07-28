from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as ddb,

    core,
)

#This is a custom construct which deploys a Dynamo DB and lambda function


# declare a new construct class called HitCounter
# As usual, constructor arguments are scope, id and kwargs, and we propagate them to the cdk.Construct base class.
# The HitCounter class also takes one explicit keyword parameter downstream of type lambda.IFunction. This is where we are going to “plug in” the Lambda function we created in the previous chapter so it can be hit-counted.
class HitCounter(core.Construct):

    @property
    def handler(self):
        return self._handler

    # This function expects a parameter of type string called downstream 
    # which is of type _lambda.IFunction - https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/IFunction.html 
    def __init__(self, scope: core.Construct, id: str, downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        #Create a Dynamo table, call it hits

        #Set the partition key to be string value with the name 'path'
        #Create a dynamo table - https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_dynamodb.html
        #https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_dynamodb/Table.html
        table = ddb.Table(
            self, 'Hits',
            partition_key={'name': 'path', 'type': ddb.AttributeType.STRING}
        )

        #Create a lambda function called HitCountHandler
        self._handler = _lambda.Function(
            self, 'HitCountHandler',
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler='hitcount.handler',
            code=_lambda.Code.from_asset('lambda'), #Look in folder called lambda
            environment={ #Apply environment variables
                'DOWNSTREAM_FUNCTION_NAME': downstream.function_name,
                'HITS_TABLE_NAME': table.table_name, #Set HITS_TABLE_NAME to equal the dynamo table created above

            }
        )

        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_dynamodb/Table.html#aws_cdk.aws_dynamodb.Table.grant_read_write_data
        # Provides the lamda function permissions to read and write to the dynamo table
        table.grant_read_write_data(self.handler)

        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/IFunction.html#aws_cdk.aws_lambda.IFunction.grant_invoke
        # provides the lambda function created in this construct permissions to invoke the lambda function passed as a parameter
        # So basically, hitcount.py lambda function can invoke hello.py
        downstream.grant_invoke(self.handler)