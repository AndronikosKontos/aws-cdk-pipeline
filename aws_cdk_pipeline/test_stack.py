#This file should include the application stack that we want to deploy through our pipeline
from constructs import Construct
from aws_cdk import Stack

class TestStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Code for the stack