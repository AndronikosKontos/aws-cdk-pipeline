#!/usr/bin/env python3

import aws_cdk as cdk

from aws_cdk_pipeline.aws_cdk_pipeline_stack import AwsCdkPipelineStack


app = cdk.App()
AwsCdkPipelineStack(app, "AwsCdkPipelineStack")

app.synth()
