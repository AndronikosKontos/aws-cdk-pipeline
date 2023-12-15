from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
    pipelines as pipelines,
)

from pipeline_stage import PipelineStage

class WorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creates a CodeCommit repository called 'TestRepo'
        repo = codecommit.Repository(
            self, 'TestRepo',
            repository_name= "TestRepo"
        )

        # Creates a new pipeline
        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            synth=pipelines.ShellStep(
                "Synth",
                input=pipelines.CodePipelineSource.code_commit(repo, "main"), # Specifies the repository where the code is stored
                commands=[
                    "npm install -g aws-cdk",  # Installs the cdk cli on Codebuild
                    "pip install -r requirements.txt",  # Instructs Codebuild to install required packages
                    "cdk synth",
                ]
            ),
        )

        # Creates an instance of the PipelineStage
        deploy = PipelineStage(self, "deploy")
        # Adds stage to the pipeline
        deploy_stage = pipeline.add_stage(deploy)
