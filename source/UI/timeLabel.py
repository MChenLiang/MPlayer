#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  14:30
# Email    : spirit_az@foxmail.com
# File     : timeLabel.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class timeLabel(QLabel):
    _signal = pyqtSignal(int)
    _timeType = 0

    changeT = 0

    def __init__(self, *args):
        super(timeLabel, self).__init__(*args)
        self.F = QFont()
        self.F.setFamily('Monospaced')
        self.F.setPixelSize(15)
        self.setFont(self.F)
        self.setFixedWidth(120)
        self.setText('00:00:00:000')
        self.setAlignment(Qt.AlignCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self._fps = 24

    @property
    def FPS(self):
        return self._fps

    @FPS.setter
    def FPS(self, fps):
        self._fps = fps

    @property
    def timeStyle(self):
        return self._timeType

    @timeStyle.setter
    def timeStyle(self, style):
        if self._timeType == style:
            return
        self._timeType = style
        self.changeTime(self.txtList)

    @timeStyle.deleter
    def timeStyle(self):
        self._timeType = 0

    def changeTime(self, txtList):
        """

        :param txtList:  [time , frame]
        :return:
        """
        self.txtList = txtList
        self.setText(str(txtList[self._timeType]))
