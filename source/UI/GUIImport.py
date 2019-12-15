#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2018/7/6 15:20
# @Email    : spirit_az@foxmail.com

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
"""
example:
    fps = 24
    frame = 2600124
    t = frameChangeTime(frame, fps)
    print t
    print timeChangeFrame(t, fps)

    hr = 30 * 3600 * 1000 + 5 * 60 * 1000 + 38 * 1000 + 500

    t_hour_temp = (hr / 3600000) % 60
    t_hour = get_coll(t_hour_temp, 2)
    t_minu_temp = (hr / 60000) % 60
    t_minu = get_coll(t_minu_temp, 2)
    t_sec_temp = (hr / 1000) % 60
    t_sec = get_coll(t_sec_temp, 2)
    frames_temp = int(float(hr % 1000) / 1000)

    print t_hour, ':', t_minu, ':', t_sec, ':', frames_temp

"""
__author__ = 'miaochenliang'

# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import (QAbstractVideoBuffer, QMediaContent,
                                QMediaMetaData, QMediaPlayer, QMediaPlaylist, QVideoFrame, QVideoProbe)
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5 import uic
import sip

USE_PYQT_MODULE = True

import os, sys, math, re

__dir_path__ = os.path.dirname(__file__).replace('\\', '/')


def icon_path(image):
    return os.path.join(__dir_path__, 'icons', image).replace('\\', '/')


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import imp
# import os
# print (os.path.exists(os.path.dirname(__file__) + '/QSS.pyd'))
import QSS

# QSS = imp.load_source('QSS', os.path.join(os.path.dirname(__file__), 'QSS.py'))
# print (QSS.H_slider)

def get_coll(inNum, num):
    str_num = str(inNum)
    if str_num.__len__() < num:
        return get_coll('0%s' % inNum, num)
    return str_num


def durationChangeTime(duration):
    dr = int(duration)
    t_hour_temp = (dr / 3600000) % 60
    t_hour = get_coll(t_hour_temp, 2)
    t_minu_temp = (dr / 60000) % 60
    t_minu = get_coll(t_minu_temp, 2)
    t_sec_temp = (dr / 1000) % 60
    t_sec = get_coll(t_sec_temp, 2)
    frames_temp = dr % 1000
    totalTime = '{0}:{1}:{2}:{3}'.format(t_hour, t_minu, t_sec, frames_temp)
    return totalTime


def durationChangeFrame(duration, fps):
    return timeChangeFrame(durationChangeTime(duration), fps)


def frameChangeDuration(frame, fps):
    tempTime = frameChangeTime(frame, fps)
    hour, minu, sec, millisecond = [int(each.strip()) for each in tempTime.split(':')]

    return int((hour * 3600 + minu * 60 + sec) * 1000 + millisecond)


def frameChangeTime(frame, fps):
    hour = int(frame / (3600 * fps))
    hour_offset = frame % (3600 * fps)
    minu = int(hour_offset / (60 * fps))
    minu_offset = hour_offset % (60 * fps)
    sec = int(minu_offset / (1 * fps))
    sec_offset = minu_offset % (1 * fps)
    millisec = int(sec_offset * 1000 / fps)

    out_hour = get_coll(hour, 2)
    out_minu = get_coll(minu, 2)
    out_sec = get_coll(sec, 2)
    out_frame = get_coll(millisec, 3)

    return '{0}:{1}:{2}:{3}'.format(out_hour, out_minu, out_sec, out_frame)


def timeChangeFrame(t, fps):
    hour, minu, sec, millisecond = [int(each.strip()) for each in t.split(':')]
    return int(math.ceil((hour * 3600 + minu * 60 + sec + float(millisecond) / 1000) * fps))
