from aws_cdk import core
from web_construct import StaticWebConstruct
from lambda_api_construct import LambdaApiGateway


class ThumbnailMakerStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        StaticWebConstruct(self, "static-web-construct")
        LambdaApiGateway(self, "Lambda-API-Gateway")
