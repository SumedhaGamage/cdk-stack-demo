from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_apigateway as gateway
)

class LambdaApiGateway(core.Construct):
    
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        layer = _lambda.LayerVersion(self, "python-layer",
        code=_lambda.Code.from_asset(".layer")
        )

        bucket = s3.Bucket(self, "thumbnail-bucket", bucket_name="tumbnail-store-bucket")
        func = _lambda.Function(self, "thumbnail_maker",
        code=_lambda.Code.from_asset("code"),
        handler="handler.tubmnail_maker",
        runtime=_lambda.Runtime.PYTHON_3_8,
        layers=[layer]
        )

        func.add_environment("BUCKET_NAME", bucket.bucket_name)
        bucket.grant_read_write(func)

        api = gateway.LambdaRestApi(self, "api-gateway", handler=func)
