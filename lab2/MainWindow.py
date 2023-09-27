# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(614, 625)
        MainWindow.setMinimumSize(QSize(500, 500))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setCheckable(False)
        self.actionOpen.setChecked(False)
        self.actionOpen.setEnabled(True)
        icon = QIcon()
        icon.addFile(u"resources/open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setShortcutVisibleInContextMenu(True)
        self.centralwidget_layout = QWidget(MainWindow)
        self.centralwidget_layout.setObjectName(u"centralwidget_layout")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget_layout)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bottomLayout = QGridLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.bottomLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.playerSlider = QSlider(self.centralwidget_layout)
        self.playerSlider.setObjectName(u"playerSlider")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playerSlider.sizePolicy().hasHeightForWidth())
        self.playerSlider.setSizePolicy(sizePolicy)
        self.playerSlider.setPageStep(1)
        self.playerSlider.setTracking(True)
        self.playerSlider.setOrientation(Qt.Horizontal)

        self.bottomLayout.addWidget(self.playerSlider, 0, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setContentsMargins(-1, -1, 10, -1)
        self.label = QLabel(self.centralwidget_layout)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)

        self.gridLayout_4.addWidget(self.label, 0, 2, 1, 1)

        self.positionLabel = QLabel(self.centralwidget_layout)
        self.positionLabel.setObjectName(u"positionLabel")
        self.positionLabel.setFont(font)
        self.positionLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.positionLabel, 0, 1, 1, 1)

        self.durationLabel = QLabel(self.centralwidget_layout)
        self.durationLabel.setObjectName(u"durationLabel")
        self.durationLabel.setFont(font)

        self.gridLayout_4.addWidget(self.durationLabel, 0, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 2, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(2)
        self.gridLayout_6.setVerticalSpacing(0)
        self.playButton = QPushButton(self.centralwidget_layout)
        self.playButton.setObjectName(u"playButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy2)
        self.playButton.setMinimumSize(QSize(0, 0))
        self.playButton.setMaximumSize(QSize(50, 50))
        self.playButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.playButton.setAutoFillBackground(False)
        self.playButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"resources/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon1)
        self.playButton.setIconSize(QSize(50, 50))

        self.gridLayout_6.addWidget(self.playButton, 1, 1, 1, 1)

        self.forwardButton = QPushButton(self.centralwidget_layout)
        self.forwardButton.setObjectName(u"forwardButton")
        sizePolicy2.setHeightForWidth(self.forwardButton.sizePolicy().hasHeightForWidth())
        self.forwardButton.setSizePolicy(sizePolicy2)
        self.forwardButton.setMinimumSize(QSize(50, 0))
        self.forwardButton.setMaximumSize(QSize(50, 16777215))
        self.forwardButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u"resources/forward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.forwardButton.setIcon(icon2)
        self.forwardButton.setIconSize(QSize(40, 30))

        self.gridLayout_6.addWidget(self.forwardButton, 1, 2, 1, 1)

        self.backButton = QPushButton(self.centralwidget_layout)
        self.backButton.setObjectName(u"backButton")
        sizePolicy2.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy2)
        self.backButton.setMinimumSize(QSize(50, 0))
        self.backButton.setMaximumSize(QSize(50, 16777215))
        self.backButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u"resources/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backButton.setIcon(icon3)
        self.backButton.setIconSize(QSize(40, 30))

        self.gridLayout_6.addWidget(self.backButton, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_6, 0, 1, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.volumeButton = QPushButton(self.centralwidget_layout)
        self.volumeButton.setObjectName(u"volumeButton")
        icon4 = QIcon()
        icon4.addFile(u"resources/volume_on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.volumeButton.setIcon(icon4)

        self.horizontalLayout.addWidget(self.volumeButton)

        self.volumeSlider = QSlider(self.centralwidget_layout)
        self.volumeSlider.setObjectName(u"volumeSlider")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy3)
        self.volumeSlider.setMinimumSize(QSize(100, 0))
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.volumeSlider)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_5.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.bottomLayout.addLayout(self.gridLayout_3, 1, 0, 1, 3)


        self.verticalLayout.addLayout(self.bottomLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget_layout)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 614, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionOpen)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mediaplayer", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.positionLabel.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.durationLabel.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.playButton.setText("")
        self.forwardButton.setText("")
        self.backButton.setText("")
        self.volumeButton.setText("")
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

