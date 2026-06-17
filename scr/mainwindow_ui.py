# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QToolBar, QVBoxLayout, QWidget)
import scr.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(624, 760)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(624, 760))
        MainWindow.setMaximumSize(QSize(624, 760))
        icon = QIcon()
        icon.addFile(u":/dark_theme/icons/dark_theme/user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon1 = QIcon()
        icon1.addFile(u":/dark_theme/icons/dark_theme/new_user.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action.setIcon(icon1)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        icon2 = QIcon()
        icon2.addFile(u":/dark_theme/icons/dark_theme/print.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_2.setIcon(icon2)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        icon3 = QIcon()
        icon3.addFile(u":/dark_theme/icons/dark_theme/save.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_3.setIcon(icon3)
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        icon4 = QIcon()
        icon4.addFile(u":/dark_theme/icons/dark_theme/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_4.setIcon(icon4)
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        icon5 = QIcon()
        icon5.addFile(u":/dark_theme/icons/dark_theme/open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.action_5.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 601, 671))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.TextFormat.AutoText)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_1 = QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setAutoFillBackground(False)
        self.lineEdit_1.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_2.addWidget(self.lineEdit_1)

        self.pushButton_1 = QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        icon6 = QIcon()
        icon6.addFile(u":/dark_theme/icons/dark_theme/copy.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_1.setIcon(icon6)
        self.pushButton_1.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.pushButton_1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon6)

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)

        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_5.addWidget(self.lineEdit_4)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_6.addWidget(self.lineEdit_5)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setIcon(icon6)

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_7.addWidget(self.lineEdit_6)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setIcon(icon6)

        self.horizontalLayout_7.addWidget(self.pushButton_6)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout.addWidget(self.comboBox)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_7 = QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_8.addWidget(self.lineEdit_7)

        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setIcon(icon6)

        self.horizontalLayout_8.addWidget(self.pushButton_7)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_8)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_8 = QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout.addWidget(self.lineEdit_8)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        icon7 = QIcon()
        icon7.addFile(u":/dark_theme/icons/dark_theme/reset.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon7)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setIcon(icon6)

        self.horizontalLayout.addWidget(self.pushButton_8)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_9)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_9 = QLineEdit(self.layoutWidget)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"background-color: rgba(255,255,255,20);")

        self.horizontalLayout_9.addWidget(self.lineEdit_9)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setIcon(icon6)

        self.horizontalLayout_9.addWidget(self.pushButton_9)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 3, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_2.addWidget(self.label_10)

        self.comboBox_2 = QComboBox(self.layoutWidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_2.addWidget(self.comboBox_2)

        self.textEdit_2 = QTextEdit(self.layoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")

        self.verticalLayout_2.addWidget(self.textEdit_2)

        self.pushButton_12 = QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon6)
        self.pushButton_12.setIconSize(QSize(16, 16))

        self.verticalLayout_2.addWidget(self.pushButton_12)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")

        self.gridLayout.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setFont(font)
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 624, 30))
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setAllowedAreas(Qt.ToolBarArea.AllToolBarAreas)
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menuBar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_2)
        self.toolBar.addAction(self.action_3)
        self.toolBar.addAction(self.action_4)
        self.toolBar.addAction(self.action_5)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"UserStone", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439...", None))
        self.action.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"new_user", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u044c...", None))
        self.action_2.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"print", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.action_3.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"save", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.action_4.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"settings", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.action_5.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"users", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0438 \u0418\u043c\u044f</span></p></body></html>", None))
        self.pushButton_1.setText("")
        self.pushButton_1.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0424\u0430\u043c\u0438\u043b\u0438\u044f</span></p></body></html>", None))
        self.pushButton_2.setText("")
        self.pushButton_2.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0418\u043c\u044f</span></p></body></html>", None))
        self.pushButton_3.setText("")
        self.pushButton_3.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430</span></p></body></html>", None))
        self.pushButton_4.setText("")
        self.pushButton_4.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u041c\u043e\u0431\u0438\u043b\u044c\u043d\u044b\u0439</span></p></body></html>", None))
        self.pushButton_5.setText("")
        self.pushButton_5.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">Email</span></p></body></html>", None))
        self.pushButton_6.setText("")
        self.pushButton_6.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.comboBox.setItemText(0, "")

        self.comboBox.setCurrentText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u044c</span></p></body></html>", None))
        self.pushButton_7.setText("")
        self.pushButton_7.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u041f\u0430\u0440\u043e\u043b\u044c</span></p></body></html>", None))
        self.pushButton.setText("")
        self.pushButton.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"reset", None))
        self.pushButton_8.setText("")
        self.pushButton_8.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">\u041b\u043e\u0433\u0438\u043d</span></p></body></html>", None))
        self.lineEdit_9.setText("")
        self.pushButton_9.setText("")
        self.pushButton_9.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043c\u0435\u043d", None))
        self.comboBox_2.setItemText(0, "")

        self.pushButton_12.setText("")
        self.pushButton_12.setProperty(u"iconName", QCoreApplication.translate("MainWindow", u"copy", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

