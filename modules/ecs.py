from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_ecs_patterns as ecs_patterns,
)
from constructs import Construct

class EcsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        common_name = "shanghaixiaochi"
        ecr_arn="arn:aws:ecr:ap-northeast-1:894724431332:repository/shanghaixiaochi"
        vpc = ec2.Vpc(self, "{}-vpc".format(common_name), max_azs=3)
        cluster = ecs.Cluster(self, "{}-cluster".format(common_name), vpc=vpc)
        repository = ecr.Repository.from_repository_arn(self, "{}-ecr".format(common_name), repository_arn=ecr_arn)
        ecs_patterns.ApplicationLoadBalancedFargateService(self,
            "{}-fargate".format(common_name),
            cluster=cluster,
            cpu=1024,
            desired_count=1,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_ecr_repository(repository),
                container_port=3000
            ),
            memory_limit_mib=4096,
            public_load_balancer=True
            )
