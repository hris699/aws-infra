import aws_cdk as cdk
from my_cdk_app.my_cdk_app_stack import MyCdkAppStack

app = cdk.App()
MyCdkAppStack(app, "MyCdkAppStack", env=env)

app.synth()