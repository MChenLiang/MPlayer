#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Time     :  16:07
# Email    : spirit_az@foxmail.com
# File     : newListView.py

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
"""
if __name__ == '__main__':
    app = QApplication([])
    form = listView()
    for each in range(10):
        form.add_widget("E:/MCL/python/MCLPlayer/temp/wwe.mp4", each)
    form.show()

    app.exec_()

"""
# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *

from collections import defaultdict
# from .. import editConf, baseFunction
import editConf, baseFunction
import random

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
bFc = baseFunction.baseFunc()

No_Found = 'No Found'


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
class listView(QWidget):
    selectedVideo = None
    doubleClicked = pyqtSignal(QUrl, str, bool)
    messClicked = pyqtSignal(QUrl)
    _playModel = 0

    @property
    def PlayModel(self):
        return self._playModel

    @PlayModel.setter
    def PlayModel(self, model):
        self._playModel = model

    def __init__(self, *args):
        super(listView, self).__init__(*args)

        self.message_list = list()
        self.flag = editConf.conf.getFlag()

        self.setFixedWidth(240)
        self.setAcceptDrops(True)

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        self.scro = QScrollArea(self)
        self.scro.setWidgetResizable(True)
        layout.addWidget(self.scro)

        tempWidget = QWidget(self.scro)
        self.scro.setWidget(tempWidget)

        vLay = QVBoxLayout(tempWidget)
        vLay.setSpacing(0)
        vLay.setContentsMargins(0, 0, 0, 0)

        self.item_area = QWidget(tempWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_area.sizePolicy().hasHeightForWidth())
        self.item_area.setSizePolicy(sizePolicy)
        vLay.addWidget(self.item_area)

        self.itemLay = QVBoxLayout(self.item_area)
        self.itemLay.setSpacing(0)
        self.itemLay.setContentsMargins(0, 0, 0, 0)

        spacerItem = QSpacerItem(20, 173, QSizePolicy.Minimum, QSizePolicy.Expanding)
        vLay.addItem(spacerItem)

    def playUpdate(self, val):
        self.PlayModel = val
        self.playChanged()

    def get_current_index(self):
        for (i, (ID, wgt)) in enumerate(self.message_list):
            if wgt.selected:
                return i

        return No_Found

    def playChanged(self):
        all_wgt = [each[1] for each in self.message_list]
        all_num = all_wgt.__len__()
        currentIndex = self.get_current_index()
        if self.PlayModel == editConf.playMode['playLoop']:
            index = currentIndex
            self.doubleClicked.emit(all_wgt[currentIndex]._videoPath, 'play', False)
        elif self.PlayModel == editConf.playMode['playSingle']:
            index = currentIndex
            self.doubleClicked.emit(all_wgt[currentIndex]._videoPath, 'stop', False)
        elif self.PlayModel == editConf.playMode['playOrder']:
            index = currentIndex + 1 if currentIndex + 1 < all_num else 0
            self.doubleClicked.emit(all_wgt[index]._videoPath, 'play', True)
        else:  # play random
            index = random.randint(0, all_num - 1)
            self.doubleClicked.emit(all_wgt[index]._videoPath, 'play', True)

        all_wgt[index].setSelected(1)

    def remove_widget(self, ID):
        for (i, (ID_now, wgt)) in enumerate(self.message_list):
            if ID == ID_now:
                self.message_list.pop(i)
                wgt.close()

    def add_widget(self, videoPath, ID, ascPath='', title=''):
        fileInfo = QFileInfo(videoPath)

        if not fileInfo.exists():
            return

        suffix = fileInfo.suffix().lower()
        if suffix not in self.flag:
            return
        url = QUrl().fromLocalFile(fileInfo.absoluteFilePath())
        if self.existPath(url.toLocalFile()) != No_Found:
            return

        wgt = image_frame(self.item_area)
        wgt.initDefault(url, ID, ascPath=ascPath, title=title)
        wgt.doubleClicked.connect(self.on_image_frame_doubleClicked)
        wgt.delSignal.connect(self.remove_widget)
        self.itemLay.addWidget(wgt)
        self.message_list.append((ID, wgt))
        wgt.show()

    def add_widgets(self, *args):
        map(lambda each: self.add_widget(*each), args)

    def on_image_frame_doubleClicked(self, videoPath, conf):
        self.doubleClicked.emit(videoPath, conf, True)

    def existPath(self, videoPath):
        for (ID, wgt) in self.message_list:
            if wgt._videoPath.toLocalFile() == videoPath:
                return wgt

        return No_Found

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super(listView, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(listView, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            # 遍历输出拖动进来的所有文件路径
            allFilePath = (u'%s' % url.toLocalFile() for url in event.mimeData().urls())
            for each in allFilePath:
                if os.path.isfile(each):
                    self.add_widget(each, QUuid().createUuid())
                else:
                    map(lambda x: self.add_widget(x, QUuid().createUuid()), self.getAllImage(each))

            event.acceptProposedAction()
        else:
            super(listView, self).dropEvent(event)

    def getAllImage(self, inPath):
        patten = '(' + ')|('.join(self.flag) + ')'
        for each in bFc.getListDirK(inPath, 'file', patten):
            yield '%s' % each  # .encode('GB2312').decode('GB2312')


class image_frame(QFrame):
    _iconPath = ''
    _videoPath = ''
    _title = ''
    _ascPath = ''
    delSignal = pyqtSignal(QUuid)
    doubleClicked = pyqtSignal(QUrl, str)
    prevSelected = None
    clSelected = None
    selected = False
    is_height = 0
    id = 0

    @property
    def videoPath(self):
        return self._videoPath

    def __init__(self, *args):
        super(image_frame, self).__init__(*args)

        font = QFont()
        font.setFamily('Monospaced')
        font.setPixelSize(20)

        self.messageDict = defaultdict()

        self.setFixedHeight(46)

        HLay = QHBoxLayout(self)
        HLay.setSpacing(0)
        HLay.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(self)
        self.label.setFixedSize(40, 40)
        self.label.setLineWidth(0)
        self.label.setScaledContents(True)

        HLay.addWidget(self.label)

        self.line = QLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFont(font)
        HLay.addWidget(self.line)

        self.createContextMenu()

    def initDefault(self, videoPath, ID, ascPath='', title=''):
        self._videoPath = videoPath
        self.id = ID
        self._ascPath = ascPath or self._videoPath
        self._title = title or videoPath.fileName()

        self.setImage(icon_path('sPlay.png'))
        self.setTitle(self._title)

    def setImage(self, image):
        self.label.setPixmap(QPixmap(image))

    def setTitle(self, title):
        self.line.setText(title)

    def setSelected(self, conf):
        if image_frame.prevSelected is not None:
            image_frame.prevSelected.selected = False
        self.selected = conf
        self.repaint()
        image_frame.prevSelected = self

    def setSelect(self):
        if image_frame.clSelected == self:
            return
        if image_frame.clSelected is not None:
            image_frame.clSelected.is_height = False
        self.is_height = True
        self.repaint()
        image_frame.clSelected = self

    def createContextMenu(self):
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

        # create menu
        self.contextMenu = QMenu(self)
        self.playAction = QAction(u'| 开始', self)
        self.pauseAction = QAction(u'| 暂停', self)
        self.stopAction = QAction(u'| 结束', self)
        self.delAction = QAction(u'| 删除', self)
        self.contextMenu.addAction(self.playAction)
        self.contextMenu.addAction(self.pauseAction)
        self.contextMenu.addAction(self.stopAction)
        self.contextMenu.addAction(self.delAction)

        self.playAction.triggered.connect(self.play_action_clicked)
        self.pauseAction.triggered.connect(self.pause_action_clicked)
        self.stopAction.triggered.connect(self.stop_action_clicked)
        self.delAction.triggered.connect(self.del_stop_clicked)

    def showContextMenu(self):
        self.setSelect()
        self.contextMenu.exec_(QCursor.pos())

    def closeContextMenu(self):
        self.contextMenu.close()

    def play_action_clicked(self):
        self.doubleClicked.emit(self._videoPath, 'play')
        self.setSelected(1)

    def pause_action_clicked(self):
        self.doubleClicked.emit(self._videoPath, 'pause')
        self.setSelected(1)

    def stop_action_clicked(self):
        self.doubleClicked.emit(self._videoPath, 'stop')
        self.setSelected(0)

    def del_stop_clicked(self):
        self.delSignal.emit(self.id)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setSelect()

        if event.button() == Qt.MiddleButton:
            self.stop_action_clicked()
        if event.button() == Qt.RightButton:
            self.showContextMenu()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.play_action_clicked()

    def enterEvent(self, event):
        if image_frame.clSelected and image_frame.clSelected != self:
            image_frame.clSelected.closeContextMenu()
        self.setSelect()

    def paintEvent(self, event):
        if self.selected:
            self.setImage(icon_path('pause.png'))
            if self.is_height:
                self.setStyleSheet("QFrame{background-color: rgb(0, 120, 215);}QLabel{border:0;}")
            else:
                self.setStyleSheet("QFrame{background-color: rgb(0, 120, 215);}QLabel{border:0;}")

        else:
            self.setImage(icon_path('play.png'))

            if self.is_height:
                self.setStyleSheet("QFrame{background-color: rgb(118,185,237); border:3px solid rgb(0, 120, 215);}"
                                   "QLabel{border:0;}")

            else:
                self.setStyleSheet("QFrame{background-color: none;}QLabel{border:0;}")


if __name__ == '__main__':
    app = QApplication([])
    ui = listView()
    ui.show()
    app.exec_()
