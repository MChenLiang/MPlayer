#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  14:31
# Email    : spirit_az@foxmail.com
# File     : soundLabel.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class soundLabel(QLabel):
    _soundPower = 60
    temp_sound = 60
    valueChanged = pyqtSignal(int)

    def __init__(self, *args):
        super(soundLabel, self).__init__(*args)
        self.setFixedSize(40, 40)
        self.setScaledContents(True)
        self.setPixmap(QPixmap(icon_path("volume_70.png")))
        self.font = QFont()
        self.font.setFamily('Monospaced')
        self.font.setPointSize(14)
        self.setFont(self.font)
        self.initUI()

    @property
    def soundPower(self):
        return self._soundPower

    @soundPower.setter
    def soundPower(self, val):
        if val >= 100:
            value = 100
        elif val <= 0:
            value = 0
        else:
            value = val

        self._soundPower = value
        self._soundPower_change_()

    def _soundPower_change_(self):
        if self.soundPower == 0:
            image_p = icon_path('volume_0.png')
        elif 0 < self._soundPower <= 10:
            image_p = icon_path('volume_10.png')

        elif 10 < self._soundPower <= 40:
            image_p = icon_path('volume_40.png')

        elif 40 < self._soundPower <= 70:
            image_p = icon_path('volume_70.png')

        else:
            image_p = icon_path('volume_100.png')
        self.set_image(image_p)

        self.valueChanged.emit(self.soundPower)

    def initUI(self):
        self.createSlider()

    def set_image(self, IPath):
        self.setPixmap(QPixmap(IPath))

    def wheelEvent(self, event):
        val = event.angleDelta().y()
        if val not in [120, -120]:
            return

        self.soundPower += val / 120 * 5

    def mousePressEvent(self, event):
        """
        :param event: button = {1: left, 4: MiddleButton, 2:RightButton}
        :return:
        """
        if event.button() == Qt.LeftButton:
            if self.soundPower != 0:
                self.temp_sound = self.soundPower
                self.soundPower = 0
            else:
                self.soundPower = self.temp_sound

        if event.button() == Qt.RightButton:
            self.showSlider()

    def createSlider(self):
        self.contextMenu = QMenu(self)
        self.contextMenu.setFixedHeight(200)
        lay = QHBoxLayout(self.contextMenu)
        lay.setContentsMargins(0, 6, 0, 6)

        self.slider = QSlider(self.contextMenu)
        self.slider.setOrientation(Qt.Vertical)
        self.slider.setStyleSheet(QSS.S_slider)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slider.sizePolicy().hasHeightForWidth())
        self.slider.setSizePolicy(sizePolicy)

        lay.addWidget(self.slider)

        self.slider.valueChanged['int'].connect(self.on_slider_valueChange)
        self.customContextMenuRequested.connect(self.showSlider)

    def showSlider(self):
        self.slider.setValue(self.soundPower)
        self.contextMenu.exec_(QCursor.pos() + QPoint(0, -210))

    def on_slider_valueChange(self, val):
        self.soundPower = val
        style = self.slider.style()
        opt = QStyleOptionSlider()
        self.slider.initStyleOption(opt)
        rectHandle = style.subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self.contextMenu)

        w, h = rectHandle.width(), rectHandle.height()
        my_p = self.contextMenu.pos() + rectHandle.bottomLeft()
        offset_x = 0 + 1 * w
        offset_y = 0 - 3 * h
        x = my_p.x() + offset_x
        y = my_p.y() + offset_y

        QToolTip.setFont(self.font)
        QToolTip.showText(QPoint(x, y), str(val), self.slider)

    def deleteLater(self):
        self.phonon_audio.deleteLater()
        super(soundLabel, self).deleteLater()
