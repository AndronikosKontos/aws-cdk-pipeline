from constructs import Construct
from aws_cdk import (
    Stage
)
from .test_stack import TestStack

class PipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Creates an instance of the application stack that we want to deploy
        service = TestStack(self, 'WebService')