#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2018/7/6 14:58
# @Email    : spirit_az@foxmail.com
__author__ = 'miaochenliang'

# import++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# from ..module.sd_ffmp import baseCommand as bcmds
import module.sd_ffmp.baseCommand as bcmds
from GUIImport import *

import listView
import videoWidget
import startLabel
import seekSlider
import timeLabel
import soundLabel
import messageWidget
import ctrlWidget

from functools import partial

reload(bcmds)
reload(listView)
reload(videoWidget)
reload(ctrlWidget)
reload(timeLabel)


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class uiForm(QWidget):
    _fps = 24
    _frame = 0
    _conf = 'stop'
    _speed = 1.0
    _tmpSpeed = 1.0

    @property
    def FPS(self):
        return self._fps

    @FPS.setter
    def FPS(self, val):
        self._fps = val
        self.stTimeLabel.FPS = val
        self.etTimeLabel.FPS = val
        self.seekSlider.FPS = val

    @property
    def FRAME(self):
        return self._frame

    @FRAME.setter
    def FRAME(self, frame):
        self._frame = frame

    def __init__(self, *args):
        super(uiForm, self).__init__(*args)

        self.colorDialog = None
        self.isPlay = False

        self.timer = QTimer()

        self.resize(960, 540)
        self.lay = QVBoxLayout(self)
        self.lay.setSpacing(0)
        self.lay.setContentsMargins(0, 0, 0, 0)

    def setupUI(self):
        HLay = QHBoxLayout()
        self.lay.addLayout(HLay)
        self.playListView = listView.listView(self)
        self.playListView.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.videoView = videoWidget.player(self)  # self.playList,
        self.videoView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.media = self.videoView.media
        HLay.addWidget(self.videoView)
        HLay.addWidget(self.playListView)

        ctrlHLay = QHBoxLayout()
        self.lay.addLayout(ctrlHLay)

        self.statusBt = startLabel.startLabel(self)
        self.statusBt.setEnabled(False)
        self.seekSlider = seekSlider.seekSlider(self)
        self.seekSlider.setRange(0, 0)
        self.seekSlider.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.stTimeLabel = timeLabel.timeLabel(self)
        label = QLabel('/', self)
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        label.setAlignment(Qt.AlignCenter)
        self.etTimeLabel = timeLabel.timeLabel(self)
        self.soundBt = soundLabel.soundLabel(self)

        ctrlHLay.addWidget(self.statusBt)
        ctrlHLay.addWidget(self.seekSlider)
        ctrlHLay.addWidget(self.stTimeLabel)
        ctrlHLay.addWidget(label)
        ctrlHLay.addWidget(self.etTimeLabel)
        ctrlHLay.addWidget(self.soundBt)

        messHLay = QHBoxLayout()
        self.lay.addLayout(messHLay)
        self.messageWidget = messageWidget.messageWidget(self)
        self.ctrlWidget = ctrlWidget.ctrlLabel(self)

        spacerItem = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Fixed)

        messHLay.addWidget(self.messageWidget)
        messHLay.addItem(spacerItem)
        messHLay.addWidget(self.ctrlWidget)

        self.bt_clicked()
        self.initUI()

    def initUI(self):
        self.media.setVolume(self.soundBt.soundPower)
        self.createContextMenu(self.stTimeLabel)
        self.createContextMenu(self.etTimeLabel)

    def bt_clicked(self):
        self.playListView.doubleClicked.connect(self.on_playListView_doubleClicked)
        self.playListView.messClicked.connect(self.on_playListView_messClicked)
        self.soundBt.valueChanged.connect(self.media.setVolume)
        self.media.mediaStatusChanged.connect(self.on_media_mediaStatusChanged)
        self.seekSlider.valueChanged['int'].connect(self.on_seekSlider_valueChanged)
        self.seekSlider.sliderPressed.connect(self.on_slider_pressed)
        self.seekSlider.sliderReleased.connect(self.on_slider_release)
        self.statusBt.clicked.connect(self.on_statusBt_clicked)
        self.ctrlWidget.valueChanged.connect(self.setPlaybackRate)

        self.timer.timeout.connect(self.on_media_positionChanged)

    def setPlaybackRate(self, val):
        self._speed = val
        self.videoView.setPlaybackRate(val)

    def changeStatus(self, conf):
        self._conf = conf
        if conf == 'play':
            self.play()
        elif conf == 'pause':
            self.pause()
        elif conf == 'stop':
            self.stop()
        elif conf == 'auto':
            status = self.media.state()
            if status == QMediaPlayer.StoppedState or status == QMediaPlayer.PausedState:
                self.play()
            else:
                self.pause()
        else:
            pass

    def on_seekSlider_valueChanged(self, val):
        t = frameChangeTime(val, self.FPS)
        self.stTimeLabel.changeTime((t, val))

    def on_slider_pressed(self):
        self.tmp = self.media.state()
        self.pause()

    def on_slider_release(self):
        val = self.seekSlider.value()
        if val < 1:
            val = 1
        elif val == self.seekSlider.maximum():
            val = self.seekSlider.maximum() - 1
        self.media.setPosition(frameChangeDuration(val - 1, self.FPS))
        if self.tmp == QMediaPlayer.PlayingState:
            self.play()

    def on_media_mediaStatusChanged(self, status):
        if status == QMediaPlayer.EndOfMedia:
            mode = self.ctrlWidget.getMode()
            self.playListView.playUpdate(mode)

    def on_seekSlider_statusSignal(self, status):
        self.changeStatus(status)

    def on_media_positionChanged(self):
        self.seekSlider.setValue(durationChangeFrame(self.media.position(), self.FPS) + 1)

    def on_statusBt_clicked(self, conf):
        self.play() if conf else self.pause()

    def on_playListView_messClicked(self, url):
        self.statusBt.setEnabled(True)
        local = url.toLocalFile()
        self.movie = bcmds.movie_message('"%s"' % local)
        self.FPS = self.movie.getFPS()
        totalTime, frame, dr = self.movie.getTime()
        w, h = self.movie.get_size()
        self.FRAME = frame
        self.seekSlider.setRange(0, frame)
        self.etTimeLabel.changeTime((totalTime, frame))
        self.messageWidget.setSize(w, h, self.FPS)
        self.timer.setInterval(int(2000 / self.FPS))

    def on_playListView_doubleClicked(self, url, conf, isReload=False):
        if url.toLocalFile() != self.media.currentMedia().canonicalUrl().toLocalFile():
            self.media.setMedia(QMediaContent(url))
        if conf == 'play' and isReload:
            self.stop()
            self.isPlay = True
            self.on_playListView_messClicked(url)
        self.changeStatus(conf)
        # if conf == 'stop':
        #     self.media.setPosition(0)

    def play(self):
        self.setPlaybackRate(self._speed)
        self.isPlay = True
        self.statusBt.isStart = True
        self.timer.start()
        self.videoView.play()

    def pause(self):
        self.isPlay = False
        self.videoView.pause()
        self.timer.stop()
        self.statusBt.isStart = False
        duration = frameChangeDuration(durationChangeFrame(self.media.position(), self.FPS), self.FPS)
        self.media.setPosition(duration)
        self.on_media_positionChanged()

    def stop(self):
        self._tmpSpeed = self._speed
        self.setPlaybackRate(1.0)
        self._speed = self._tmpSpeed
        self.isPlay = False
        self.timer.stop()
        self.videoView.stop()
        self.statusBt.isStart = False
        self.seekSlider.setValue(0)
        self.media.setPosition(0)

    def createContextMenu(self, widget):
        widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.contextMenu = QMenu(widget)
        time_action = QAction('time', self, triggered=partial(self.changeTimeStyle, 0))
        frame_action = QAction('Frame', self, triggered=partial(self.changeTimeStyle, 1))
        self.contextMenu.addActions([time_action, frame_action])

        widget.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self):
        self.contextMenu.exec_(QCursor.pos())

    def changeTimeStyle(self, style):
        for widget in [self.stTimeLabel, self.etTimeLabel]:
            widget.timeStyle = style

    def keyReleaseEvent(self, event):
        url = self.media.currentMedia().canonicalUrl()
        if not bool(url.toLocalFile()):
            return

        if event.modifiers() == Qt.ControlModifier and event.key() == Qt.Key_Alt:
            self.changeStatus('auto')

        if event.key() not in [Qt.Key_Left, Qt.Key_Right]:
            return

        if self.isPlay or self._conf == 'stop':
            self.changeStatus('pause')
        duration = self.media.position()
        cTime = int(math.floor(durationChangeFrame(duration, self.FPS)))
        if event.key() == Qt.Key_Left:
            frame = cTime - 1
            frame = frame if frame >= 0 else self.FRAME - 1
        elif event.key() == Qt.Key_Right:
            frame = cTime + 1
            if frame >= self.FRAME:
                frame = 0
        else:
            frame = cTime
        duration = frameChangeDuration(frame, self.FPS)
        self.media.setPosition(duration)
        self.seekSlider.setValue(frame + 1)

    def showColorDialog(self):
        if self.colorDialog is None:
            brightnessSlider = seekSlider.seekSlider()
            brightnessSlider.setRange(-100, 100)
            brightnessSlider.setValue(self.videoView.videoWidget.brightness())
            brightnessSlider.sliderMoved.connect(self.videoView.videoWidget.setBrightness)
            self.videoView.videoWidget.brightnessChanged.connect(brightnessSlider.setValue)

            contrastSlider = seekSlider.seekSlider()
            contrastSlider.setRange(-100, 100)
            contrastSlider.setValue(self.videoWidget.contrast())
            contrastSlider.sliderMoved.connect(self.videoView.videoWidget.setContrast)
            self.videoView.videoWidget.contrastChanged.connect(contrastSlider.setValue)

            hueSlider = seekSlider.seekSlider()
            hueSlider.setRange(-100, 100)
            hueSlider.setValue(self.videoWidget.hue())
            hueSlider.sliderMoved.connect(self.videoView.videoWidget.setHue)
            self.videoView.videoWidget.hueChanged.connect(hueSlider.setValue)

            saturationSlider = seekSlider.seekSlider()
            saturationSlider.setRange(-100, 100)
            saturationSlider.setValue(self.videoWidget.saturation())
            saturationSlider.sliderMoved.connect(self.videoView.videoWidget.setSaturation)
            self.videoView.videoWidget.saturationChanged.connect(saturationSlider.setValue)

            layout = QFormLayout()
            layout.addRow("Brightness", brightnessSlider)
            layout.addRow("Contrast", contrastSlider)
            layout.addRow("Hue", hueSlider)
            layout.addRow("Saturation", saturationSlider)

            button = QPushButton("Close")
            layout.addRow(button)

            self.colorDialog = QDialog(self)
            self.colorDialog.setWindowTitle("Color Options")
            self.colorDialog.setLayout(layout)

            button.clicked.connect(self.colorDialog.close)

        self.colorDialog.show()

    def closeEvent(self, event):
        self.videoView.stop()


if __name__ == '__main__':
    app = QApplication([])
    ui = uiForm()
    ui.setupUI()
    ui.show()
    app.exec_()
