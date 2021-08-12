[Where am I up to?](https://cdkworkshop.com/30-python/40-hit-counter/700-test.html)

# awscdklab
Repo for this lab - https://cdkworkshop.com/

# Handy Links
https://docs.aws.amazon.com/cdk/latest/guide/home.html
https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html
https://docs.aws.amazon.com/CDK/latest/userguide/tools.html
https://github.com/jorgebastida/awslogs (Python cli based log parsing tool for cloudwatch logs)

# Python specifics
Virtual Envs - https://docs.python.org/3/tutorial/venv.html
setup.py - https://stackoverflow.com/questions/1471994/what-is-setup-py

# Commands setup
npm install -g aws-cdk
cdk --version
python3 --version
pip3 --version
pip3 install --upgrade pip

# Commands deploying
 * `cdk init sample-app --language python` Create a new CDK project
 * `cdk ls`          list all stacks in the app
 * `cdk bootstrap` bootstrap an AWS account for CDK deployments
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 * `pip install aws-cdk.aws-lambda` Install a new construct library (Needed for each AWS service used)
 * `pip install aws-cdk.aws_apigateway` Install a new construct library (Needed for each AWS service used)
 * `pip install aws-cdk.aws_dynamodb` Install a new construct library (Needed for each AWS service used)

# Commands to get started - python
 * One time command per project - `python3 -m venv .venv` Manually create a virtual env (CDK init does this for you though)
 * `source .venv/bin/activate` activate your virtual env
 * 'deactivate' leave your virtual env
 * `pip install --upgrade pip` upgrade pip
 * `pip install -r requirements.txt`install all package requirements from the txt file


# Terminology CDK
constructs (CDK)
interface

# Terminology Python
class, object, self, '__init__' = https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
method
@property