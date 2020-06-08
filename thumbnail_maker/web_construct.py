from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_s3_deployment as s3_deployment,
    aws_route53 as r53,
    aws_cloudfront as cdn, 
    aws_certificatemanager as cert
)

from route53 import ARecordCreate


class StaticWebConstruct(core.Construct):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        ori = cdn.OriginAccessIdentity(self, "static-web-s3-oai", comment="ORI for CDN to access S# content")
        
        #Create S3 bucket and deploy the UI content
        bucket = s3.Bucket(self, "static-content-s3",
        bucket_name="thumbnail-maker-web-content-bucket",
        website_index_document="index.html",
        website_error_document="error.html")
        web_content = s3_deployment.Source.asset("ThumbnailMaker/dist/ThumbnailMaker")
        s3_deployment.BucketDeployment(self, "static-content-deployment",
        destination_bucket=bucket,
        sources=[web_content])

        #Certificate reference
        certificate = cdn.ViewerCertificate.from_acm_certificate(
                    cert.Certificate.from_certificate_arn(self, "enqbatorCertificate","arn:aws:acm:us-east-1:035060142173:certificate/3cf99a52-4e8a-4992-b420-fdb0b4414ffd"),
                    aliases=["ffive.com", "www.ffive.com"]
        )
        #Cloudfront develivery for the S3 content
        distribution = cdn.CloudFrontWebDistribution(self, "cdn-distribution",
        origin_configs=[
            cdn.SourceConfiguration(
                s3_origin_source=cdn.S3OriginConfig(s3_bucket_source=bucket, origin_access_identity=ori),
                behaviors=[cdn.Behavior(allowed_methods=cdn.CloudFrontAllowedMethods.GET_HEAD, is_default_behavior=True)])
        ], 
        viewer_certificate=certificate)

        ARecordCreate(self, "ffive-arecord", cdn_target=distribution, domain_name="ffive.com", record_name="thumbnail.ffive.com")
        ARecordCreate(self, "ffive-arecord-www", cdn_target=distribution, domain_name="ffive.com", record_name="www.thumbnail.ffvie.com")