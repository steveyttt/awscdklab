#!/usr/bin/env python3

###This deploys everything, you can see it is looking for:
    # cdkworkshop.cdkworkshop_stack.py
    # it deploys all content from cdkworkshop.cdkworkshop_stack.py as CF stack cdkworkshop

from aws_cdk import core

#From local directory cdkworkshop and file cdkworkshop_stack.py import class CdkworkshopStack
from cdkworkshop.cdkworkshop_stack import CdkworkshopStack

app = core.App()

#deploy a stack called cdk workshop
CdkworkshopStack(app, "cdkworkshop")

app.synth()
