#!/user/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'miaoChenLiang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
from UI.GUIImport import *


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ↓++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class mSplashScreen(QSplashScreen):
    def __init__(self, animation, flag, widget):
        super(mSplashScreen, self).__init__(QPixmap(), flag)
        self.movie = QMovie(animation)
        self.movie.frameChanged.connect(self.onNextFrame)
        self.count = self.movie.frameCount()
        self.step = 0
        self.widget = widget

    def onNextFrame(self):
        if self.step < self.count:
            pixmap = self.movie.currentPixmap()
            self.setPixmap(pixmap)
            self.setMask(pixmap.mask())
            self.step += 1

        else:
            self.finish(self.widget)

    def showEvent(self, *args):
        self.movie.start()

    def finish(self, widget):
        widget.show()
        self.deleteLater()
        self.movie.deleteLater()


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class my_label_btn(QLabel):
    def __init__(self, *args):
        super(my_label_btn, self).__init__()
        self.setMouseTracking(True)
        self.setScaledContents(True)
        if args:
            self.ID = args[0]
            self.setPixmap(QPixmap(args[1]))
            self.func = args[2]

    def mouseReleaseEvent(self, event):
        self.func.btnHandle(self.ID)

    def enterEvent(self, event):
        self.func.btnEnter(self.ID)

    def leaveEvent(self, event):
        self.func.btnLeave(self.ID)

    # def mousePressEvent(self, event):
    #     self.parent().btnClick(self.ID)
