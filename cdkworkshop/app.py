#!/usr/bin/env python3

###This deploys everything, you can see it is looking for:
    # cdkworkshop.cdkworkshop_stack.py
    # it deploys all content from cdkworkshop.cdkworkshop_stack.py as CF stack cdkworkshop

from aws_cdk import core

from cdkworkshop.cdkworkshop_stack import CdkworkshopStack


app = core.App()
CdkworkshopStack(app, "cdkworkshop")

app.synth()
