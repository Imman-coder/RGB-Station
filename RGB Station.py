import sys,os
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from ui_untitled3 import Ui_MainWindow
from ui_untitled_dialog import Ui_Dialog

RUN_PATH = "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"

class MainWindow(QMainWindow):
    
        def __init__(self):
                QMainWindow.__init__(self)
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.setWindowFlag(Qt.FramelessWindowHint)
                self.setWindowIcon(QIcon(r'icon.png'))
                self.setWindowTitle("RGB Station")
                

                self.setMouseTracking(True)
                self.stat=False

                def toggleMenu(maxWidth, enable):
                        if enable:
                                width = self.ui.frame_left_menu.width()
                                maxExtend = maxWidth
                                standard = 50
                                if width == 50:
                                        widthExtended = maxExtend
                                else:
                                        widthExtended = standard
                                self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
                                self.animation.setDuration(300)
                                self.animation.setStartValue(width)
                                self.animation.setEndValue(widthExtended)
                                self.animation.setEasingCurve(QEasingCurve.InOutQuart)
                                self.animation.start()
                                
                def prt():
                        if not(self.ui.frame_left_menu.underMouse()==self.stat):
                                if self.ui.frame_left_menu.underMouse():
                                        # print("Mouse On Widget")
                                        toggleMenu(220, True)
                                else:
                                        # print("Mouse Left")
                                        toggleMenu(220, True)
                        self.stat=self.ui.frame_left_menu.underMouse()

                def moveWindow(event):
                        if event.buttons() == Qt.LeftButton:
                                if self.isMaximized():
                                        self.showNormal()
                                        self.move(self.dragPos+QPoint(-(self.width()/5),-10))
                                self.move(self.pos() + event.globalPos() - self.dragPos)
                                self.dragPos = event.globalPos()
                                event.accept()
                
                def maxmin(event):
                        if self.isMaximized():
                                self.showNormal()
                        else:
                                self.showMaximized()

                def shd():
                        dlg = CloseDialog(self)
                        dlg.exec()
                

                self.ui.Top_frame.mouseMoveEvent = moveWindow
                timer = QTimer(self)
                timer.timeout.connect(prt)
                timer.start(300)

                #Handeling Button Click
                # self.ui.btn_close.clicked.connect(lambda:self.close())
                self.ui.btn_close.clicked.connect(lambda:shd())
                self.ui.btn_minimize.clicked.connect(lambda:self.showMinimized())
                self.ui.btn_maximize_restore.clicked.connect(lambda:maxmin("ev"))
                self.ui.Top_frame.mouseDoubleClickEvent = maxmin
                self.sizegrip = QSizeGrip(self.ui.frame_size_grip_2)
                self.sizegrip.setStyleSheet("width: 25px; height: 30px; margin 0px; padding: 0px;")
                # self.ui.btn_open_file.clicked.connect(lambda:print("clicked"))
                self.ui.btn_open_file.clicked.connect(self.anyBtn)
                self.ui.btn_save.clicked.connect(self.anyBtn)
                self.ui.btn_new_user.clicked.connect(self.anyBtn)
                self.ui.btn_new.clicked.connect(self.anyBtn)
                self.ui.btn_settings.clicked.connect(self.anyBtn)
                self.ui.window_title.setText("RGB Station")

        def DeselectButtonFn(self,note):
                rl=note.replace("border-right: 5px solid rgb(44, 49, 60);", "border-right: 0px solid rgb(44, 49, 60);")
                return rl

        def SelectButtonFn(self,note):
                rl=note.replace("border-right: 0px solid rgb(44, 49, 60);","border-right: 5px solid rgb(44, 49, 60);")
                return rl

        def resetButtonFn(self):
                for k in self.ui.frame_left_menu.findChildren(QPushButton):
                        k.setStyleSheet(self.DeselectButtonFn(k.styleSheet()))


        def anyBtn(self):
                if self.ui.btn_open_file.underMouse():
                        self.resetButtonFn()
                        self.ui.btn_open_file.setStyleSheet(self.SelectButtonFn(self.ui.btn_open_file.styleSheet()))

                if self.ui.btn_new.underMouse():
                        self.resetButtonFn()
                        self.ui.btn_new.setStyleSheet(self.SelectButtonFn(self.ui.btn_new.styleSheet()))

                if self.ui.btn_new_user.underMouse():
                        self.resetButtonFn()
                        self.ui.btn_new_user.setStyleSheet(self.SelectButtonFn(self.ui.btn_new_user.styleSheet()))

                if self.ui.btn_save.underMouse():
                        self.resetButtonFn()
                        self.ui.btn_save.setStyleSheet(self.SelectButtonFn(self.ui.btn_save.styleSheet()))

                if self.ui.btn_settings.underMouse():
                        self.resetButtonFn()
                        self.ui.btn_settings.setStyleSheet(self.SelectButtonFn(self.ui.btn_settings.styleSheet()))

        def mousePressEvent(self, event):
                self.dragPos = event.globalPos()
                if event.buttons() == Qt.LeftButton:
                        # print('Mouse click: LEFT CLICK')  
                        self.anyBtn()              
                # if event.buttons() == Qt.RightButton:
                #         print('Mouse click: RIGHT CLICK')
                # if event.buttons() == Qt.MidButton:
                #         print('Mouse click: MIDDLE BUTTON')
        

        def trayIconClick(self,reason):
                        if reason == QtWidgets.QSystemTrayIcon.DoubleClick:
                                self.show()

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtWidgets.QMenu(parent)
        exitAction = menu.addAction("Exit")
        
        self.setContextMenu(menu)
        self.setObjectName("RGB Station")
        exitAction.triggered.connect(lambda:QtCore.QCoreApplication.exit())




app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
w = QtWidgets.QWidget()
trayicon = SystemTrayIcon(QtGui.QIcon('icon.ico'), w)
# trayicon = SystemTrayIcon(QtGui.QIcon(QPixmap(':/icon.png')))


trayicon.setToolTip("RGB Controller Application")
# trayicon.show()
trayicon.activated.connect(window.trayIconClick)

class CloseDialog(QDialog):
        def __init__(self,parent=None):
                super().__init__(parent)
                self.dl=Ui_Dialog()
                self.setWindowFlag(Qt.FramelessWindowHint)
                self.setAttribute(Qt.WA_TranslucentBackground)
                self.dl.setupUi(self)
                def moveWindow(event):
                        if event.buttons() == Qt.LeftButton:
                                self.move(self.pos() + event.globalPos() - self.dragPos)
                                self.dragPos = event.globalPos()
                                event.accept()
                self.dl.top.mouseMoveEvent = moveWindow
                def hd():
                        window.hide()
                        self.hide()
                        trayicon.show()
                        trayicon.showMessage("Tray Notification","The app is minimized to System Tray.")
                self.dl.pushButton_3.clicked.connect(lambda:QtCore.QCoreApplication.exit())
                self.dl.pushButton_4.clicked.connect(lambda:hd())

        def mousePressEvent(self, event):
                self.dragPos = event.globalPos()

window.show()
app.exec_()