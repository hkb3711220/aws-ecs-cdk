import aws_cdk as core
import aws_cdk.assertions as assertions

from shanghaixiaochi_ecs.shanghaixiaochi_ecs_stack import ShanghaixiaochiEcsStack

# example tests. To run these tests, uncomment this file along with the example
# resource in shanghaixiaochi_ecs/shanghaixiaochi_ecs_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ShanghaixiaochiEcsStack(app, "shanghaixiaochi-ecs")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
