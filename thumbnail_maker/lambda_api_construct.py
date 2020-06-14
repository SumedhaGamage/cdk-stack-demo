from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_apigateway as gateway,
    aws_dynamodb as db
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
        handler="handler.thubmnail_maker",
        runtime=_lambda.Runtime.PYTHON_3_8,
        layers=[layer]
        )

        func.add_environment("BUCKET_NAME", bucket.bucket_name)
        bucket.grant_read_write(func)

        api = gateway.LambdaRestApi(self, "api-gateway", handler=func, binary_media_types=["image/jpeg","image/png"],
        default_cors_preflight_options=gateway.CorsOptions(allow_origins=['http://localhost:4200'], allow_methods=gateway.Cors.ALL_METHODS, status_code=200)
        )

        table = db.Table(self, "metadata-table", table_name="picture_meta_data", 
        partition_key=db.Attribute(name="id", type=db.AttributeType.STRING))

        func.add_environment("TABLE_NAME", table.table_name)
        table.grant_read_write_data(func)
        