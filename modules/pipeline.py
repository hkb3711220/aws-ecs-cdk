from aws_cdk import (
    Stack,
    pipelines,
    aws_codepipeline_actions as codepipeline_actions
)

from constructs import Construct

class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        common_name = "shanghaixiaochi"
        pipeline = pipelines.CodePipeline(self, 
            "{}-ecs-deploy".format(common_name), 
            pipeline_name="{}-cd-pipeline".format(common_name),
            synth=pipelines.ShellStep("Synth", 
                input=pipelines.CodePipelineSource.git_hub(
                    "hkb3711220/aws_ecs_cdk", "main", trigger=codepipeline_actions.GitHubTrigger.POLL),
                commands=[
                    "npm install -g aws-cdk", 
                    "python -m pip install -r requirements.txt", 
                    "cdk synth"
                    ]
                )
        )