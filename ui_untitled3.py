# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled3vpfABe.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(785, 670)
        palette = QPalette()
        brush = QBrush(QColor(210, 210, 210, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(44, 49, 60, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        brush3 = QBrush(QColor(210, 210, 210, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(785, 670))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.centralwidget.setPalette(palette1)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Top_frame = QFrame(self.centralwidget)
        self.Top_frame.setObjectName(u"Top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Top_frame.sizePolicy().hasHeightForWidth())
        self.Top_frame.setSizePolicy(sizePolicy)
        self.Top_frame.setMaximumSize(QSize(16777215, 40))
        self.Top_frame.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.Top_frame.setFrameShape(QFrame.NoFrame)
        self.Top_frame.setFrameShadow(QFrame.Plain)
        self.Top_frame.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.Top_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Title_Frame = QFrame(self.Top_frame)
        self.Title_Frame.setObjectName(u"Title_Frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Title_Frame.sizePolicy().hasHeightForWidth())
        self.Title_Frame.setSizePolicy(sizePolicy1)
        self.Title_Frame.setMinimumSize(QSize(0, 0))
        self.Title_Frame.setMaximumSize(QSize(16777215, 50))
        self.Title_Frame.setFrameShape(QFrame.NoFrame)
        self.Title_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Title_Frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(50, 5, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.window_title = QLabel(self.Title_Frame)
        self.window_title.setObjectName(u"window_title")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.window_title.sizePolicy().hasHeightForWidth())
        self.window_title.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.window_title.setFont(font)
        self.window_title.setTabletTracking(False)
        self.window_title.setLayoutDirection(Qt.LeftToRight)
        self.window_title.setAutoFillBackground(False)
        self.window_title.setStyleSheet(u"color:white")
        self.window_title.setFrameShadow(QFrame.Raised)
        self.window_title.setScaledContents(False)
        self.window_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.window_title.setMargin(5)

        self.horizontalLayout_7.addWidget(self.window_title)


        self.horizontalLayout_2.addWidget(self.Title_Frame)

        self.Button_Frame = QFrame(self.Top_frame)
        self.Button_Frame.setObjectName(u"Button_Frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Button_Frame.sizePolicy().hasHeightForWidth())
        self.Button_Frame.setSizePolicy(sizePolicy3)
        self.Button_Frame.setMinimumSize(QSize(0, 38))
        self.Button_Frame.setMaximumSize(QSize(16777215, 50))
        self.Button_Frame.setStyleSheet(u"")
        self.Button_Frame.setFrameShape(QFrame.NoFrame)
        self.Button_Frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.Button_Frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.Button_Frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy4)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.Button_Frame)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy4.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy4)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.Button_Frame)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy4.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy4)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_close)


        self.horizontalLayout_2.addWidget(self.Button_Frame)


        self.verticalLayout_2.addWidget(self.Top_frame)

        self.Bottom_frame = QFrame(self.centralwidget)
        self.Bottom_frame.setObjectName(u"Bottom_frame")
        self.Bottom_frame.setFrameShape(QFrame.NoFrame)
        self.Bottom_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.Bottom_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Bottom_frame)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy5)
        self.frame_left_menu.setMaximumSize(QSize(50, 16777215))
        self.frame_left_menu.setMouseTracking(True)
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.btn_open_file = QPushButton(self.frame_menus)
        self.btn_open_file.setObjectName(u"btn_open_file")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_open_file.sizePolicy().hasHeightForWidth())
        self.btn_open_file.setSizePolicy(sizePolicy6)
        self.btn_open_file.setMinimumSize(QSize(0, 60))
        palette2 = QPalette()
        brush4 = QBrush(QColor(27, 29, 35, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        brush6 = QBrush(QColor(120, 120, 120, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_open_file.setPalette(palette2)
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.btn_open_file.setFont(font1)
        self.btn_open_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_open_file.setLayoutDirection(Qt.LeftToRight)
        self.btn_open_file.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-folder-open.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid rgb(27, 29, 35);\n"
"	border-right: 5px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 18px solid rgb(33, 37, 43);\n"
"}\n"
"")

        self.layout_menus.addWidget(self.btn_open_file)

        self.btn_save = QPushButton(self.frame_menus)
        self.btn_save.setObjectName(u"btn_save")
        sizePolicy6.setHeightForWidth(self.btn_save.sizePolicy().hasHeightForWidth())
        self.btn_save.setSizePolicy(sizePolicy6)
        self.btn_save.setMinimumSize(QSize(0, 60))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_save.setPalette(palette3)
        self.btn_save.setFont(font1)
        self.btn_save.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save.setLayoutDirection(Qt.LeftToRight)
        self.btn_save.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-save.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid rgb(27, 29, 35);\n"
"	border-right: 0px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left:18px solid rgb(33, 37, 43);\n"
"}\n"
"")

        self.layout_menus.addWidget(self.btn_save)

        self.btn_new = QPushButton(self.frame_menus)
        self.btn_new.setObjectName(u"btn_new")
        sizePolicy6.setHeightForWidth(self.btn_new.sizePolicy().hasHeightForWidth())
        self.btn_new.setSizePolicy(sizePolicy6)
        self.btn_new.setMinimumSize(QSize(0, 60))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_new.setPalette(palette4)
        self.btn_new.setFont(font1)
        self.btn_new.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new.setLayoutDirection(Qt.LeftToRight)
        self.btn_new.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-file.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid rgb(27, 29, 35);\n"
"	border-right: 0px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 18px solid rgb(33, 37, 43);\n"
"}\n"
"")

        self.layout_menus.addWidget(self.btn_new)

        self.btn_new_user = QPushButton(self.frame_menus)
        self.btn_new_user.setObjectName(u"btn_new_user")
        sizePolicy6.setHeightForWidth(self.btn_new_user.sizePolicy().hasHeightForWidth())
        self.btn_new_user.setSizePolicy(sizePolicy6)
        self.btn_new_user.setMinimumSize(QSize(0, 60))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_new_user.setPalette(palette5)
        self.btn_new_user.setFont(font1)
        self.btn_new_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_new_user.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/16x16/icons/16x16/cil-user-follow.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid rgb(27, 29, 35);\n"
"	border-right: 0px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left:18px solid rgb(33, 37, 43);\n"
"}\n"
"")

        self.layout_menus.addWidget(self.btn_new_user)


        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy5.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy5)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(0)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 0)
        self.btn_settings = QPushButton(self.frame_extra_menus)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy6.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy6)
        self.btn_settings.setMinimumSize(QSize(0, 50))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.btn_settings.setPalette(palette6)
        self.btn_settings.setFont(font1)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"QPushButton {	\n"
"	background-image: url(:/20x20/icons/20x20/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 16px solid rgb(27, 29, 35);\n"
"	border-right: 0px solid rgb(44, 49, 60);\n"
"	background-color: rgb(27, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 45px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-left: 16px solid rgb(33, 37, 43);\n"
"}\n"
"")

        self.layout_menu_bottom.addWidget(self.btn_settings)

        self.verticalSpacer = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.layout_menu_bottom.addItem(self.verticalSpacer)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_3.addWidget(self.frame_left_menu)

        self.Right_frame = QFrame(self.Bottom_frame)
        self.Right_frame.setObjectName(u"Right_frame")
        self.Right_frame.setFrameShape(QFrame.NoFrame)
        self.Right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Right_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_Mid = QFrame(self.Right_frame)
        self.frame_Mid.setObjectName(u"frame_Mid")
        self.frame_Mid.setFrameShape(QFrame.NoFrame)
        self.frame_Mid.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_Mid)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_Mid)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.Page_Settings = QWidget()
        self.Page_Settings.setObjectName(u"Page_Settings")
        self.stackedWidget.addWidget(self.Page_Settings)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_Mid)

        self.frame_Bottom = QFrame(self.Right_frame)
        self.frame_Bottom.setObjectName(u"frame_Bottom")
        sizePolicy.setHeightForWidth(self.frame_Bottom.sizePolicy().hasHeightForWidth())
        self.frame_Bottom.setSizePolicy(sizePolicy)
        self.frame_Bottom.setMaximumSize(QSize(16777215, 25))
        self.frame_Bottom.setStyleSheet(u"background:rgb(38, 43, 52)")
        self.frame_Bottom.setFrameShape(QFrame.NoFrame)
        self.frame_Bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_Bottom)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_Bottom)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 25))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(15, 0, 0, 0)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.verticalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_5.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_Bottom)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy7)
        self.frame_10.setMinimumSize(QSize(154, 25))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4.setMargin(5)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.frame_size_grip_2 = QFrame(self.frame_10)
        self.frame_size_grip_2.setObjectName(u"frame_size_grip_2")
        self.frame_size_grip_2.setMaximumSize(QSize(20, 20))
        self.frame_size_grip_2.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip_2.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip_2)


        self.horizontalLayout_5.addWidget(self.frame_10)


        self.verticalLayout_3.addWidget(self.frame_Bottom)


        self.horizontalLayout_3.addWidget(self.Right_frame)


        self.verticalLayout_2.addWidget(self.Bottom_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"Main Window", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.btn_open_file.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.btn_new_user.setText(QCoreApplication.translate("MainWindow", u"New User", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Designed By: Immanuel Mundary", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"v2.0.1", None))
    # retranslateUi

