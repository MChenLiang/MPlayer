#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  1:01
# Email    : spirit_az@foxmail.com
# File     : movieToImage.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from importFfmp import *


def movToFrame(inMov, outFileDir, frame, isOverride, outSize, flag, fps):
    size_dir = os.path.join(outFileDir, str(outSize)).replace('\\', '/')
    os.path.exists(size_dir) or os.makedirs(size_dir)

    inFile, inFlag = os.path.splitext(os.path.basename(inMov))
    outImagePath = os.path.join(size_dir, '{0}_{1}{2}'.format(inFile, frame, flag)).replace('\\', '/')
    if os.path.exists(outImagePath) and not isOverride:
        return
    ff = FFmpeg(
        inputs={inMov: None},
        outputs={outImagePath: '-s {0} -r {1} -y -f mjpeg -ss {2} -vframes 1 '.format(outSize, fps, frame/fps)}

    )
    print ff.cmd
    ff.run()
    print 'create image : --- >> ', outImagePath


def movToFrames(inMov, outFileDir, frames, isOverride, outSize, flag, fps):
    func = lambda x: movToFrame(inMov, outFileDir, x, isOverride, outSize, flag, fps)
    map(func, frames)


if __name__ == '__main__':
    inMov = "E:/MCL/python/MCLPlayer/temp/wwe.mp4"
    outFileDir = 'E:/MCL/python/MCLPlayer/temp'
    frames = range(1000)
    isOverride = True
    outSize = '1280x720'
    flag = '.png'
    movToFrames(inMov, outFileDir, frames, isOverride, outSize, flag, 24.00)

