#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  15:37
# Email    : spirit_az@foxmail.com
# File     : messageWidget.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *


class messageWidget(QWidget):
    def __init__(self, *args):
        super(messageWidget, self).__init__(*args)

        self.F = QFont()
        self.F.setFamily('Monospaced')
        self.F.setPixelSize(15)

        self.setFont(self.F)
        lay = QHBoxLayout(self)
        lay.setSpacing(0)
        lay.setContentsMargins(0, 0, 0, 0)

        sizeLay = QHBoxLayout()
        sizeLay.setSpacing(0)
        sizeLay.setContentsMargins(5, 0, 0, 5)
        lay.addLayout(sizeLay)

        sizeLabel = QLabel('size  :  ', self)
        sizeLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)

        self.video_w, self.video_h = QLabel('1024', self), QLabel('1024', self)
        label = QLabel('*', self)

        sizeLabel.setFont(self.F)
        self.video_w.setFont(self.F)
        self.video_h.setFont(self.F)
        label.setFont(self.F)

        self.video_w.setFixedWidth(56)
        self.video_h.setFixedWidth(56)

        sizeLabel.setAlignment(Qt.AlignLeft | Qt.AlignLeading | Qt.AlignCenter)
        self.video_w.setAlignment(Qt.AlignCenter | Qt.AlignLeading | Qt.AlignCenter)
        self.video_h.setAlignment(Qt.AlignCenter | Qt.AlignLeading | Qt.AlignCenter)

        sizeLay.addWidget(sizeLabel)
        sizeLay.addWidget(self.video_w)
        sizeLay.addWidget(label)
        sizeLay.addWidget(self.video_h)

        label = QLabel('  |  ', self)
        label.setFont(self.F)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizeLay.addWidget(label)

        fpsLay = QHBoxLayout()
        fpsLay.setContentsMargins(5, 0, 0, 5)
        lay.addLayout(fpsLay)

        label = QLabel('FPS  :  ', self)
        label.setFont(self.F)
        fpsLay.addWidget(label)

        self.video_fps = QLabel('0.000', self)
        self.video_fps.setFont(self.F)
        self.video_fps.setFixedWidth(60)
        fpsLay.addWidget(self.video_fps)

        spacerItem = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        lay.addItem(spacerItem)

    def setSize(self, w, h, fps):
        self.video_w.setText(str(w))
        self.video_h.setText(str(h))
        self.video_fps.setText(str(round(float(fps), 3)))

    def defaultAll(self):
        self.video_w.setText('0')
        self.video_h.setText('0')
        self.video_fps.setText('0.000')


class pushButton(QPushButton):
    def __init__(self, *args):
        super(pushButton, self).__init__(*args)

    def mousePressEvent(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    app = QApplication([])

    ui = messageWidget()
    ui.show()

    ui.setSize(1024, 1024, 23.9764500)
    app.exec_()
