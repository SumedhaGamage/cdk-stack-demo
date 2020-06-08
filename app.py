#!/usr/bin/env python3

from aws_cdk import core

from thumbnail_maker.thumbnail_maker_stack import ThumbnailMakerStack


app = core.App()
ThumbnailMakerStack(app, "thumbnail-maker")

app.synth()
