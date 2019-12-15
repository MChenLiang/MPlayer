#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  14:32
# Email    : spirit_az@foxmail.com
# File     : seekSlider.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class seekSlider(QSlider):
    _frame = 0
    _fps = 24
    durationSignal = pyqtSignal(int)

    def __init__(self, *args):
        super(seekSlider, self).__init__(*args)
        self.setOrientation(Qt.Horizontal)
        self.setStyleSheet(QSS.H_slider)
        self.setMinimum(0)

    @property
    def FRAME(self):
        return self._frame

    @FRAME.setter
    def FRAME(self, frame):
        self._frame = frame

    @property
    def FPS(self):
        return self._fps

    @FPS.setter
    def FPS(self, fps):
        self._fps = fps

