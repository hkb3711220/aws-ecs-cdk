import aws_cdk as cdk
from constructs import Construct
from modules.ecs import EcsStack

class AppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        EcsStack(self, "shanghaixiaochi-ecs")
