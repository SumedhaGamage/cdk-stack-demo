#!/usr/bin/env python3

from aws_cdk import core

from thumbnail_maker.thumbnail_maker_stack import ThumbnailMakerStack

#set the environment
env_us_east = core.Environment(account="035060142173", region="us-east-1")

app = core.App()
ThumbnailMakerStack(app, "thumbnail-maker", env=env_us_east)


app.synth()
