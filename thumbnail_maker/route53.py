from aws_cdk import (
    core,
    aws_route53_targets as target,
    aws_route53 as route,
    aws_cloudfront as cdn
)

class ARecordCreate(core.Construct):

    def __init__(self, scope: core.Construct, id: str, *, cdn_target: cdn.IDistribution, domain_name: str, record_name: str):
        super().__init__(scope, id)

        hosted_zone = route.HostedZone.from_lookup(self, "ffvie-hosted-zone", domain_name=domain_name)
        route.ARecord(self, id,
        zone=hosted_zone,
        target=route.RecordTarget(alias_target=target.CloudFrontTarget(distribution=cdn_target)),
        record_name=record_name
        )
