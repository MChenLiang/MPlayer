#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'miaochenliang'

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# import +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
from UI.GUIImport import *
from UI import UIPlayer

import baseFunction
import existsUI as exUI
import editConf

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# reload +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
reload(baseFunction)

reload(UIPlayer)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# __init__ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
bFc = baseFunction.baseFunc()

__mainName__ = editConf.conf().get('configuration', 'name')
__version__ = editConf.conf().get('configuration', 'version')
_author_ = editConf.decode(editConf.conf().__getAuthor__())


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
class MCLPlayer(QMainWindow):
    '''
    __glo__ = None
    '''

    def __init__(self, parent=None):
        super(MCLPlayer, self).__init__(parent)
        self.F = QFont()
        self.F.setFamily('Monospaced')
        self.F.setPixelSize(20)
        self.setFont(self.F)
        # 设置 窗口名称
        self.setObjectName(__mainName__)
        # 设置系统图标
        icon = QIcon(icon_path('window_icon.png'))
        self.setWindowIcon(icon)
        self.setWindowTitle('{0} {1}'.format(__mainName__, __version__))

        # self.setMouseTracking(True)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        #
        #
        # self.fontColorToolButton = QToolButton()
        # self.fontColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        # self.fontColorToolButton.setMenu(
        #     self.createColorMenu(self.textColorChanged, Qt.black))
        # self.textAction = self.fontColorToolButton.menu().defaultAction()
        # self.fontColorToolButton.setIcon(
        #     self.createColorToolButtonIcon(':/images/textpointer.png',
        #                                    Qt.black))
        # self.fontColorToolButton.setAutoFillBackground(True)
        # self.fontColorToolButton.clicked.connect(self.textButtonTriggered)
        #
        # self.fillColorToolButton = QToolButton()
        # self.fillColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        # self.fillColorToolButton.setMenu(
        #     self.createColorMenu(self.itemColorChanged, Qt.white))
        # self.fillAction = self.fillColorToolButton.menu().defaultAction()
        # self.fillColorToolButton.setIcon(
        #     self.createColorToolButtonIcon(':/images/floodfill.png',
        #                                    Qt.white))
        # self.fillColorToolButton.clicked.connect(self.fillButtonTriggered)
        #
        # self.lineColorToolButton = QToolButton()
        # self.lineColorToolButton.setPopupMode(QToolButton.MenuButtonPopup)
        # self.lineColorToolButton.setMenu(
        #     self.createColorMenu(self.lineColorChanged, Qt.black))
        # self.lineAction = self.lineColorToolButton.menu().defaultAction()
        # self.lineColorToolButton.setIcon(
        #     self.createColorToolButtonIcon(':/images/linecolor.png',
        #                                    Qt.black))
        # self.lineColorToolButton.clicked.connect(self.lineButtonTriggered)
        #
        # self.colorToolBar = self.addToolBar("Color")
        # self.colorToolBar.addWidget(self.fontColorToolButton)
        # self.colorToolBar.addWidget(self.fillColorToolButton)
        # self.colorToolBar.addWidget(self.lineColorToolButton)

    def setupUI(self, parent=None):
        """

        :return:
        """
        self.pt = parent or QWidget()
        self.setCentralWidget(self.pt)

        Lay = QVBoxLayout(self.pt)
        Lay.setSpacing(0)
        Lay.setContentsMargins(0, 0, 0, 0)

        # self.title_widget()
        # Lay.addWidget(self.titleWidget)

        self.main_widget()
        Lay.addWidget(self.mainWidget)

        newSize = self.mainWidget.size()

        self.resize(newSize)

        # self.__init__UI__()
        # self.bt_clicked()

    def title_widget(self):
        self.titleWidget = QWidget(self)
        self.titleWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.title_hLay = QHBoxLayout(self.titleWidget)
        self.title_hLay.setContentsMargins(10, 0, 10, 0)

        self.label_icon = QLabel(self.titleWidget)
        self.label_icon.setScaledContents(True)
        self.label_icon.setPixmap(QPixmap(icon_path('window_icon.png')))
        self.label_icon.setFixedSize(25, 25)
        self.title_hLay.addWidget(self.label_icon)

        self.label_name = QLabel(self.titleWidget)
        self.label_name.setFont(self.F)
        self.label_name.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)
        self.label_name.setText('{0} {1}'.format(__mainName__, __version__))
        self.label_name.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.title_hLay.addWidget(self.label_name)

        spacerItem = QSpacerItem(215, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.title_hLay.addItem(spacerItem)

    def main_widget(self):
        self.mainWidget = UIPlayer.uiForm()
        self.mainWidget.setupUI()

    def __init__UI__(self):
        """
        初始化UI面板
        :return:
        """
        # self.add_ex_bt()
        self.add_tray()

    def bt_clicked(self):
        """
        所有的按钮信号槽链接
        :return:
        """
        pass



    def createColorMenu(self, slot, defaultColor):
        colors = [Qt.black, Qt.white, Qt.red, Qt.blue, Qt.yellow]
        names = ["black", "white", "red", "blue", "yellow"]

        colorMenu = QMenu(self)
        for color, name in zip(colors, names):
            action = QAction(self.createColorIcon(color), name, self,
                    triggered=slot)
            action.setData(QColor(color)) 
            colorMenu.addAction(action)
            if color == defaultColor:
                colorMenu.setDefaultAction(action)
        return colorMenu

    def createColorToolButtonIcon(self, imageFile, color):
        pixmap = QPixmap(50, 80)
        pixmap.fill(Qt.transparent)
        painter = QPainter(pixmap)
        image = QPixmap(imageFile)
        target = QRect(0, 0, 50, 60)
        source = QRect(0, 0, 42, 42)
        painter.fillRect(QRect(0, 60, 50, 80), color)
        painter.drawPixmap(target, image, source)
        painter.end()

        return QIcon(pixmap)

    def createColorIcon(self, color):
        pixmap = QPixmap(20, 20)
        painter = QPainter(pixmap)
        painter.setPen(Qt.NoPen)
        painter.fillRect(QRect(0, 0, 20, 20), color)
        painter.end()

        return QIcon(pixmap)

    def textColorChanged(self):
        self.textAction = self.sender()
        self.fontColorToolButton.setIcon(self.createColorToolButtonIcon(
                    ':/images/textpointer.png',
                    QColor(self.textAction.data())))
        self.textButtonTriggered()

    def itemColorChanged(self):
        self.fillAction = self.sender()
        self.fillColorToolButton.setIcon(self.createColorToolButtonIcon(
                    ':/images/floodfill.png',
                    QColor(self.fillAction.data())))
        self.fillButtonTriggered()

    def lineColorChanged(self):
        self.lineAction = self.sender()
        self.lineColorToolButton.setIcon(self.createColorToolButtonIcon(
                    ':/images/linecolor.png',
                    QColor(self.lineAction.data())))
        self.lineButtonTriggered()

    def textButtonTriggered(self):
        self.scene.setTextColor(QColor(self.textAction.data()))

    def fillButtonTriggered(self):
        self.scene.setItemColor(QColor(self.fillAction.data()))

    def lineButtonTriggered(self):
        self.scene.setLineColor(QColor(self.lineAction.data()))
        
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    # add tray ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    def add_tray(self):
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon(icon_path('window_icon.png')))
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.trayClick)
        self.trayMenu()

    def trayClick(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            self.showNormal()

        elif reason == QSystemTrayIcon.MiddleClick:
            self.showMessage()
        else:
            pass

    def showMessage(self):
        icon = QSystemTrayIcon.Information
        in_text = 'soft :{}\r\n'.format()
        in_text += 'version : {}\r\n'.format(__version__)
        in_text += 'author : {}\r\n'.format(_author_)
        self.trayIcon.showMessage('introduce : ', in_text, icon)

    def trayMenu(self):

        img_main = QIcon(icon_path('window_icon.png'))
        img_min = QIcon(icon_path('min_in.png'))
        img_exit = QIcon(icon_path('del_in.png'))

        self.trayIcon.setToolTip('{0} {1}'.format(__mainName__, __version__))

        self.restoreAction = QAction(img_main, __mainName__, self)
        self.minAction = QAction(img_min, "Minimize", self)
        self.quitAction = QAction(img_exit, "Exit", self)

        self.trayIconMenu = QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addAction(self.minAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)

        self.restoreAction.triggered.connect(self.max_action)
        self.minAction.triggered.connect(self.min_action)
        self.quitAction.triggered.connect(self.exit_action)

    def min_action(self):
        self.showMinimized()

    def max_action(self):
        self.actions()
        self.showNormal()

    def exit_action(self):
        self.close()

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    # add pushbutton ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    def add_ex_bt(self):
        self.btn_min = exUI.my_label_btn(1, icon_path('min_out.png'), self)
        self.btn_min.setFixedSize(20, 20)
        self.btn_min.setToolTip('min')
        self.title_hLay.addWidget(self.btn_min)

        self.btn_max = exUI.my_label_btn(2, icon_path('max_out.png'), self)
        self.btn_max.setFixedSize(20, 20)
        self.btn_max.setToolTip('max')
        self.title_hLay.addWidget(self.btn_max)

        self.btn_exit = exUI.my_label_btn(3, icon_path('del_out.png'), self)
        self.btn_exit.setFixedSize(20, 20)
        self.btn_exit.setToolTip('exit')
        self.title_hLay.addWidget(self.btn_exit)

    def btnHandle(self, ID):
        if ID == 1:
            self.showMinimized()

        if ID == 2:
            if self.isMaximized():
                self.showNormal()
            else:
                self.showMaximized()

        # elif ID == 3:
        #     txt, key = u'Exit ?', 'A'
        #     if openUI.show_warning(txt, key):
        #         self.close()

    def btnEnter(self, ID):
        if ID == 1:
            self.btn_min.setPixmap(QPixmap(icon_path("min_in.png")))

        if ID == 2:
            if self.isMaximized():
                self.btn_max.setPixmap(QPixmap(icon_path("noMax_in.png")))
            else:
                self.btn_max.setPixmap(QPixmap(icon_path("max_in.png")))

        elif ID == 3:
            self.btn_exit.setPixmap(QPixmap(icon_path("del_in.png")))

    def btnLeave(self, ID):
        if ID == 1:
            self.btn_min.setPixmap(QPixmap(icon_path('min_out.png')))
        elif ID == 2:
            if self.isMaximized():
                self.btn_max.setPixmap(QPixmap(icon_path("noMax_out.png")))
            else:
                self.btn_max.setPixmap(QPixmap(icon_path("max_out.png")))
        elif ID == 3:
            self.btn_exit.setPixmap(QPixmap(icon_path("del_out.png")))

    def btnMaxIcon(self, conf):
        if conf:
            self.btn_max.setPixmap(QPixmap(icon_path("noMax_out.png")))
        else:
            self.btn_max.setPixmap(QPixmap(icon_path("max_out.png")))

    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.c_pos = event.globalPos() - self.pos()
            self.m_pressed = True

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.m_pressed:
                self.move(event.globalPos() - self.c_pos)
                event.accept()

    def mouseReleaseEvent(self, event):
        self.m_pressed = False

    # def show(self):
    #     super(MCLPlayer, self).show()

    def close(self):
        self.trayIcon.close()
        super(MCLPlayer, self).close()

        # def deleteLater(self):
        #     super(MCLPlayer, self).deleteLater()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
def show():
    #
    # 开始启动
    app = QApplication(sys.argv)

    ui = MCLPlayer()
    ui.setupUI()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    show()
