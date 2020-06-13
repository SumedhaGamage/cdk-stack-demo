from aws_cdk import core


class ApiAndLambdaConstruct(core.Construct):
    
    def __init__(self, scope: core.Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)