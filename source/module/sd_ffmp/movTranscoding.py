#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  14:31
# Email    : spirit_az@foxmail.com
# File     : movTranscoding.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from importFfmp import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def transcoding(inPath, outPath, inFps, outFps, imageSize, flag):
    ff = FFmpeg(
        inputs={inPath: None},
        outputs={outPath: None}
    )
    print ff.cmd
    ff.run()
