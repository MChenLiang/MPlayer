#!/usr/bin/env python
# -*- coding:UTF-8 -*-
# @Time     : 2018/8/9 18:21
# @Email    : spirit_az@foxmail.com
__author__ = 'miaochenliang'

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #
from GUIImport import *
import seekSlider
# from .. import editConf
import editConf

# reload(editConf)


# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #

# +--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+ #


class ctrlLabel(QWidget):
    valueChanged = pyqtSignal(float)

    def __init__(self, *args):
        super(ctrlLabel, self).__init__(*args)

        self.F = QFont()
        self.F.setFamily('Monospaced')
        self.F.setPixelSize(15)

        self.lay = QHBoxLayout(self)

        tLabel = QLabel(u'播放速度 ：', self)
        tLabel.setFont(self.F)
        self.lay.addWidget(tLabel)

        self.doubleBox = QDoubleSpinBox(self)
        self.doubleBox.setFont(self.F)
        self.doubleBox.setValue(1)
        self.doubleBox.setRange(0.1, 4)
        self.doubleBox.setSingleStep(0.1)
        self.lay.addWidget(self.doubleBox)

        self.slider = seekSlider.seekSlider(self)
        self.slider.setValue(10)
        self.slider.setSingleStep(1)
        self.slider.setRange(1, 40)
        self.slider.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.lay.addWidget(self.slider)
        # self.slider.hide()

        self.comboBox = QComboBox(self)
        self.comboBox.setFont(self.F)
        self.comboBox.setFixedWidth(120)
        self.comboBox.setStyleSheet("""QComboBox {    border: none;   	border:2px groove rgb(100, 100, 100);
border-radius:10px;	padding:2px 4px;	background-color: rgb(0, 170, 200);	color: rgb(255, 255, 255); }
QComboBox::drop-down {	border:none;}""")
        self.comboBox.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.lay.addWidget(self.comboBox)

        self.initComboBox()
        self.bt_clicked()

    def bt_clicked(self):
        self.doubleBox.valueChanged.connect(lambda X: self.slider.setValue(X * 10))
        self.slider.valueChanged.connect(lambda X: self.doubleBox.setValue(X / 10.00))

        self.comboBox.currentTextChanged.connect(self.saveSelMode)

        self.slider.valueChanged.connect(self.doubleChanged)

    def doubleChanged(self, val):
        self.valueChanged.emit(val / 10.00)

    def initComboBox(self):
        keys = editConf.playMode.items()
        keys.sort(key=lambda x: x[1])
        vals = [each[0] for each in keys]
        self.comboBox.addItems(vals)

        defIndex = editConf.playMode[editConf.conf.getPlayMode()]
        self.comboBox.setCurrentIndex(defIndex)

    def saveSelMode(self, val):
        editConf.conf.setPlayMode(val)
        pass

    def getMode(self):
        return editConf.playMode[self.comboBox.currentText()]


if __name__ == '__main__':
    app = QApplication([])
    ui = ctrlLabel()
    ui.show()
    app.exec_()
