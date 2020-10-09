# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled_dialogSUIgCA.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(329, 164)
        Dialog.setMinimumSize(QSize(329, 164))
        Dialog.setMaximumSize(QSize(329, 164))
        Dialog.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 329, 164))
        self.frame.setMinimumSize(QSize(329, 164))
        self.frame.setMaximumSize(QSize(329, 164))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setStyleSheet(u"QFrame{\n"
"border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.frame)
        self.top.setObjectName(u"top")
        self.top.setMaximumSize(QSize(16777215, 25))
        self.top.setStyleSheet(u"QFrame{\n"
"	border-radius:0px;\n"
"	border-top-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"	background-color: rgb(30, 30, 30);\n"
"}")
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.top)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(8, 0, 0, 0)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        palette1 = QPalette()
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush2 = QBrush(QColor(30, 30, 30, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        brush3 = QBrush(QColor(120, 120, 120, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.label_2.setPalette(palette1)

        self.horizontalLayout_4.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_2 = QFrame(self.top)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMaximumSize(QSize(25, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(15, 15))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 7px;		\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.top)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"	border-radius:0px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"	background-color: rgb(50, 50, 51);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush4 = QBrush(QColor(50, 50, 51, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush4)
        brush5 = QBrush(QColor(255, 255, 255, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.label.setPalette(palette2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMaximumSize(QSize(16777215, 27))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButton_2.setPalette(palette3)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border-radius:8px;\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"	border-radius:8px;\n"
"	background-color:rgb(235, 235, 235)\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMaximumSize(QSize(16777215, 27))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButton_3.setPalette(palette4)
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius:8px;\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"	border-radius:8px;\n"
"	background-color:rgb(235, 235, 235)\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMaximumSize(QSize(16777215, 27))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.pushButton_4.setPalette(palette5)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border-radius:8px;\n"
"	background-color:rgb(255, 255, 255)\n"
"}\n"
"QPushButton:hover{\n"
"	border-radius:8px;\n"
"	background-color:rgb(235, 235, 235)\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.reject)
        self.pushButton.clicked.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"System Tray Notification", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"The window will be minimized to system tray.", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"No", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

