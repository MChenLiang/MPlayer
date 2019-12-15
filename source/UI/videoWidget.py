#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  18:17
# Email    : spirit_az@foxmail.com
# File     : videoWidget.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class player(QWidget):
    def __init__(self, *args, **kwargs):
        super(player, self).__init__(*args, **kwargs)

        self.trackInfo = ""
        self.statusInfo = ''

        self.setFocusPolicy(Qt.TabFocus)
        self.lay = QVBoxLayout(self)
        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.setupUI()

    def setupUI(self):

        self.videoWidget = VideoWidget(self)
        self.lay.addWidget(self.videoWidget)

        self.media = mMedia(None, QMediaPlayer.VideoSurface)
        self.media.setVideoOutput(self.videoWidget)

        self.bt_clicked()

    def bt_clicked(self):
        self.media.metaDataChanged.connect(self.metaDataChanged)
        self.media.mediaStatusChanged.connect(self.on_statusChanged)

    def playUpdate(self, val):
        if val:
            self.play()
        else:
            self.stop()

    def setPlaybackRate(self, p_float):
        self.media.setPlaybackRate(p_float)

    def play(self):
        self.media.play()

    def pause(self):
        self.media.pause()

    def stop(self):
        self.media.stop()
        # self.media.set

    def state(self):
        self.media.state()

    def metaDataChanged(self):
        if self.media.isMetaDataAvailable():
            self.setTrackInfo("%s - %s" % (
                self.media.metaData(QMediaMetaData.AlbumArtist),
                self.media.metaData(QMediaMetaData.Title)))

    def setTrackInfo(self, info):
        self.trackInfo = info
        outTxt = self.trackInfo if self.statusInfo != '' else '{0} | {1}'.format(self.trackInfo, self.statusInfo)
        # print outTxt

    def on_statusChanged(self, status):
        self.handleCursor(status)

        if status == QMediaPlayer.LoadingMedia:
            self.setStatusInfo("Loading...")
        elif status == QMediaPlayer.StalledMedia:
            self.setStatusInfo("Media Stalled")
        elif status == QMediaPlayer.EndOfMedia:
            QApplication.alert(self)
        elif status == QMediaPlayer.InvalidMedia:
            self.displayErrorMessage()
        else:
            self.setStatusInfo("")

    def handleCursor(self, status):
        if status in (QMediaPlayer.LoadingMedia, QMediaPlayer.BufferingMedia, QMediaPlayer.StalledMedia):
            self.setCursor(Qt.BusyCursor)
        else:
            self.unsetCursor()

    def displayErrorMessage(self):
        self.setStatusInfo(self.media.errorString())

    def setStatusInfo(self, info):
        self.statusInfo = info
        outTxt = self.statusInfo if self.statusInfo != '' else '{0} | {1}'.format(self.trackInfo, self.statusInfo)
        # print outTxt


class mMedia(QMediaPlayer):
    timeChanged = pyqtSignal(int)

    def __init__(self, *args, **kwargs):
        super(mMedia, self).__init__(*args, **kwargs)


class VideoWidget(QVideoWidget):
    def __init__(self, parent=None):
        super(VideoWidget, self).__init__(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.setAttribute(Qt.WA_OpaquePaintEvent)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape and self.isFullScreen():
            self.setFullScreen(False)
            event.accept()
        elif event.key() == Qt.Key_Enter and event.modifiers() & Qt.Key_Alt:
            self.setFullScreen(not self.isFullScreen())
            event.accept()
        else:
            super(VideoWidget, self).keyPressEvent(event)

    def mouseDoubleClickEvent(self, event):
        self.setFullScreen(not self.isFullScreen())
        event.accept()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    player = player(QMediaPlaylist())
    player.resize(320, 240)
    player.show()

    sys.exit(app.exec_())
