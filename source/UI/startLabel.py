#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  14:27
# Email    : spirit_az@foxmail.com
# File     : startLabel.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class startLabel(QLabel):
    clicked = pyqtSignal(bool)
    _in_ = False
    _isStart = False

    def __init__(self, *args):
        super(startLabel, self).__init__(*args)
        self.setFixedSize(40, 40)
        self.setScaledContents(True)

        self.setPixmap(QPixmap(icon_path('play_in.png')))

    @property
    def isStart(self):
        return self._isStart

    @isStart.setter
    def isStart(self, conf):
        self._isStart = conf
        if self._in_:
            imagePath = icon_path('pause.png') if self._isStart else icon_path('play.png')
        else:
            imagePath = icon_path('pause_in.png') if self._isStart else icon_path('play_in.png')

        self.setImage(imagePath)

    @isStart.deleter
    def isStart(self):
        self._isStart = False

    def setImage(self, imagePath):
        self.setPixmap(QPixmap(imagePath))

    def mouseReleaseEvent(self, *args, **kwargs):
        imagePath = icon_path('pause_in.png') if self.isStart else icon_path('play_in.png')
        self.setImage(imagePath)

    def mousePressEvent(self, event):
        if event.button() != Qt.LeftButton:
            return
        self.isStart = not self.isStart
        self.clicked.emit(self.isStart)

    def enterEvent(self, event):
        self._in_ = True
        imagePath = icon_path('pause.png') if self.isStart else icon_path('play.png')
        self.setImage(imagePath)

    def leaveEvent(self, *args, **kwargs):
        self._in_ = False
        imagePath = icon_path('pause_in.png') if self.isStart else icon_path('play_in.png')
        self.setImage(imagePath)

