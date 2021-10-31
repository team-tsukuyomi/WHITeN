# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_main_window(object):
    def setupUi(self, main_window):
        if not main_window.objectName():
            main_window.setObjectName(u"main_window")
        main_window.resize(897, 481)
        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName(u"central_widget")
        self.central_widget_v_layout = QVBoxLayout(self.central_widget)
        self.central_widget_v_layout.setObjectName(u"central_widget_v_layout")
        self.central_widget_v_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.central_widget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame {\n"
"	background-color: rgb(35, 39, 49);\n"
"	border-radius: 10px;\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_v_layout = QVBoxLayout(self.main_frame)
        self.main_v_layout.setObjectName(u"main_v_layout")
        self.main_v_layout.setContentsMargins(0, 0, 0, 0)
        self.title_frame = QFrame(self.main_frame)
        self.title_frame.setObjectName(u"title_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_frame.sizePolicy().hasHeightForWidth())
        self.title_frame.setSizePolicy(sizePolicy)
        self.title_frame.setMinimumSize(QSize(0, 40))
        self.title_frame.setMaximumSize(QSize(16777215, 40))
        self.title_frame.setToolTipDuration(-1)
        self.title_frame.setStyleSheet(u"QFrame {\n"
"}")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.title_h_layout = QHBoxLayout(self.title_frame)
        self.title_h_layout.setObjectName(u"title_h_layout")
        self.title_h_layout.setContentsMargins(0, 0, 10, 0)
        self.min_button = QPushButton(self.title_frame)
        self.min_button.setObjectName(u"min_button")
        self.min_button.setMinimumSize(QSize(20, 20))
        self.min_button.setMaximumSize(QSize(20, 20))
        self.min_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(67, 203, 68);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(67, 220, 68);\n"
"}")

        self.title_h_layout.addWidget(self.min_button)

        self.max_button = QPushButton(self.title_frame)
        self.max_button.setObjectName(u"max_button")
        self.max_button.setMinimumSize(QSize(20, 20))
        self.max_button.setMaximumSize(QSize(20, 20))
        self.max_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(248, 188, 58);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	background-color: rgb(255, 200, 58);\n"
"}")

        self.title_h_layout.addWidget(self.max_button)

        self.exit_button = QPushButton(self.title_frame)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(20, 20))
        self.exit_button.setMaximumSize(QSize(20, 20))
        self.exit_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(243, 91, 90);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(255, 91, 90);\n"
"}")

        self.title_h_layout.addWidget(self.exit_button)


        self.main_v_layout.addWidget(self.title_frame)

        self.content_frame = QFrame(self.main_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.content_v_layout = QVBoxLayout(self.content_frame)
        self.content_v_layout.setObjectName(u"content_v_layout")
        self.content_v_layout.setContentsMargins(-1, -1, -1, 0)
        self.widget_frame = QFrame(self.content_frame)
        self.widget_frame.setObjectName(u"widget_frame")
        self.widget_frame.setFrameShape(QFrame.StyledPanel)
        self.widget_frame.setFrameShadow(QFrame.Raised)
        self.widget_v_layout = QVBoxLayout(self.widget_frame)
        self.widget_v_layout.setObjectName(u"widget_v_layout")
        self.label = QLabel(self.widget_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: #e3e3e3;\n"
"	font-size: 20vh;\n"
"}")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.widget_v_layout.addWidget(self.label)


        self.content_v_layout.addWidget(self.widget_frame)

        self.input_frame = QFrame(self.content_frame)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setMinimumSize(QSize(0, 50))
        self.input_frame.setMaximumSize(QSize(16777215, 50))
        self.input_frame.setFrameShape(QFrame.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Raised)
        self.input_h_layout = QHBoxLayout(self.input_frame)
        self.input_h_layout.setObjectName(u"input_h_layout")
        self.input_h_layout.setContentsMargins(0, 0, 0, 6)
        self.input_box = QLineEdit(self.input_frame)
        self.input_box.setObjectName(u"input_box")
        self.input_box.setMinimumSize(QSize(0, 40))
        self.input_box.setMaximumSize(QSize(16777215, 40))
        self.input_box.setFont(font)
        self.input_box.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(35, 39, 49);\n"
"	color: rgb(236, 236, 236);\n"
"	border: 1px solid rgb(236, 236, 236);\n"
"	border-radius: 7px;\n"
"}")
        self.input_box.setFrame(True)
        self.input_box.setCursorPosition(0)
        self.input_box.setDragEnabled(True)
        self.input_box.setClearButtonEnabled(True)

        self.input_h_layout.addWidget(self.input_box)

        self.enter_button = QPushButton(self.input_frame)
        self.enter_button.setObjectName(u"enter_button")
        self.enter_button.setMinimumSize(QSize(40, 40))
        self.enter_button.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.enter_button.setFont(font1)
        self.enter_button.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(242, 80, 34);\n"
"	color: rgb(235, 235, 235);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(255, 80, 34);\n"
"}")

        self.input_h_layout.addWidget(self.enter_button)


        self.content_v_layout.addWidget(self.input_frame)


        self.main_v_layout.addWidget(self.content_frame)


        self.central_widget_v_layout.addWidget(self.main_frame)

        main_window.setCentralWidget(self.central_widget)

        self.retranslateUi(main_window)

        QMetaObject.connectSlotsByName(main_window)
    # setupUi

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QCoreApplication.translate("main_window", u"MainWindow", None))
        self.min_button.setText("")
        self.max_button.setText("")
        self.exit_button.setText("")
        self.label.setText("")
        self.input_box.setText("")
        self.input_box.setPlaceholderText(QCoreApplication.translate("main_window", u" Enter text here", None))
        self.enter_button.setText(QCoreApplication.translate("main_window", u">", None))
    # retranslateUi

