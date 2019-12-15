#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  1:02
# Email    : spirit_az@foxmail.com
# File     : importFfmp.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from ffmMCL import ffmpeg_parse_infos
import os


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
def get_coll(inNum, num):
    str_num = str(inNum)
    if str_num.__len__() < num:
        return get_coll('0%s' % inNum, num)
    return str_num


def frameChangeTime(frame, fps):
    hour = int(frame / (3600 * fps))
    hour_offset = frame % (3600 * fps)
    minu = int(hour_offset / (60 * fps))
    minu_offset = hour_offset % (60 * fps)
    sec = int(minu_offset / (1 * fps))
    sec_offset = minu_offset % (1 * fps)
    millisec = sec_offset * 1000 / fps

    out_hour = get_coll(hour, 2)
    out_minu = get_coll(minu, 2)
    out_sec = get_coll(sec, 2)
    out_frame = get_coll(millisec, 3)

    return '{0}:{1}:{2}:{3}'.format(out_hour, out_minu, out_sec, out_frame)


def timeChangeFrame(t, fps):
    hour, minu, sec, millisecond = [int(each.strip()) for each in t.split(':')]
    return int((hour * 3600 + minu * 60 + sec + float(millisecond) / 1000) * fps)
