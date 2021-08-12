from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)

#This python code is called by app.py, it contains the logic for what should be deployed in the CF stack

# from local file hitcount.py import class HitCounter
# So here we are essentially importing a custom construct to deploy a resource in an opinionated way
from .hitcounter import HitCounter

from cdk_dynamo_table_viewer import TableViewer

# As you can see, the class constructors of both CdkworkshopStack and lambda Function (and many other classes in the CDK) have the signature (scope, id, **kwargs). 
# This is because all of these classes are constructs. Constructs are the basic building block of CDK apps. 
# They represent abstract “cloud components” which can be composed together into higher level abstractions via scopes. 
# Scopes can include constructs, which in turn can include other constructs, etc.

# Constructs are always created in the scope of another construct and must always have an identifier which must be unique within the scope it’s created. 
# Therefore, construct initializers (constructors) will always have the following signature.

    # scope: the first argument is always the scope in which this construct is created. 
    # In almost all cases, you’ll be defining constructs within the scope of current construct, which means you’ll usually just want to pass "self" for the first argument. Make a habit out of it.

    # id: the second argument is the local identity of the construct. It’s an ID that has to be unique amongst construct within the same scope. 
    # The CDK uses this identity to calculate the CloudFormation Logical ID for each resource defined within this scope. To read more about IDs in the CDK, see the CDK user manual.
    
    # kwargs: the last (sometimes optional) arguments is always a set of initialization arguments. Those are specific to each construct. 
    # For example, the lambda.Function construct accepts arguments like runtime, code and handler. You can explore the various options using your IDE’s auto-complete or in the online documentation.

class CdkworkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Defines an AWS Lamda resource
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda.html - The whole lambda python package
        # https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_lambda/Function.html - The function python class
        # https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.Function.html - The generic AWS CDK documentation for the function
        my_lambda = _lambda.Function(
            self, 'HelloHandler', #Deployed lambda with name cdkworkshop-HelloHandler2E4FBA4D-IE9vg9CFOFm6
            runtime=_lambda.Runtime.PYTHON_3_7, # Set the runtime
            code=_lambda.Code.asset('lambda'), #Look in the local dir 'lamba' for the function code
            handler='hello.handler',
        )

        # Define resources using a custom construct (imported above using .hitcounter)
        # send a parameter "downstream" to this construct.This parameter is the above created lambda function (My_lambda)
        hello_with_counter = HitCounter(
            self, 'HelloHitCounter',
            downstream=my_lambda,
        )

        #Defines an AWS API GW with lambda integration
        #https://docs.aws.amazon.com/cdk/api/latest/python/aws_cdk.aws_apigateway.html
        apigw.LambdaRestApi(
            self, 'Endpoint',
            handler=hello_with_counter.handler,
        )

        TableViewer(
            self, 'ViewHitCounter',
            title='Hello Hits',
            sort_by='-hits',
            table=hello_with_counter.table,
        )