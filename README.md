# awscdklab
Repo for this lab - https://cdkworkshop.com/

# Handy Links
https://docs.aws.amazon.com/cdk/latest/guide/home.html
https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html
https://docs.aws.amazon.com/CDK/latest/userguide/tools.html

# Python specifics
Virtual Envs - https://docs.python.org/3/tutorial/venv.html

# Commands setup
npm install -g aws-cdk
cdk --version
python3 --version
pip3 --version
pip3 install --upgrade pip

# Commands deploying
 * ```cdk init sample-app --language python``` Create a new CDK project
 * `cdk ls`          list all stacks in the app
 * ```cdk bootstrap``` bootstrap an AWS account for CDK deployments
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

# Commands python
 * ```python3 -m venv .venv``` Manually create a virtual env (CDK init does this for you though)
 * ```source .venv/bin/activate``` activate your virtual env
 * ```pip install --upgrade pip``` upgrade pip
 * ```pip install -r requirements.txt```install all packahe requirements from the txt file


# Terminology
