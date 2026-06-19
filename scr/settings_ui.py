# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QAbstractButton, QAbstractItemView, QApplication, QDialog,
    QDialogButtonBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListView, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import scr.resources_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(325, 635)
        Settings.setMinimumSize(QSize(325, 635))
        Settings.setMaximumSize(QSize(325, 635))
        icon = QIcon()
        icon.addFile(u":/dark_theme/icons/dark_theme/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Settings.setWindowIcon(icon)
        Settings.setModal(False)
        self.verticalLayout_3 = QVBoxLayout(Settings)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Settings)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(Settings)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(255, 32))
        self.lineEdit.setMaximumSize(QSize(255, 32))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(Settings)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(40, 39))
        icon1 = QIcon()
        icon1.addFile(u":/dark_theme/icons/dark_theme/open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Settings)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView = QListView(Settings)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(255, 0))
        self.listView.setMaximumSize(QSize(255, 16777215))
        self.listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_2.addWidget(self.listView)

        self.lineEdit_2 = QLineEdit(Settings)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(255, 32))
        self.lineEdit_2.setMaximumSize(QSize(255, 32))

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Settings)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(40, 39))
        self.frame.setMaximumSize(QSize(40, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.pushButton_2 = QPushButton(Settings)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(39)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(40, 39))
        self.pushButton_2.setMaximumSize(QSize(40, 39))
        icon2 = QIcon()
        icon2.addFile(u":/dark_theme/icons/dark_theme/plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(Settings)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QSize(40, 39))
        self.pushButton_3.setMaximumSize(QSize(40, 39))
        icon3 = QIcon()
        icon3.addFile(u":/dark_theme/icons/dark_theme/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label_3 = QLabel(Settings)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listView_2 = QListView(Settings)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setMinimumSize(QSize(255, 0))
        self.listView_2.setMaximumSize(QSize(255, 16777215))
        self.listView_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView_2.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_4.addWidget(self.listView_2)

        self.lineEdit_3 = QLineEdit(Settings)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(255, 32))
        self.lineEdit_3.setMaximumSize(QSize(255, 32))

        self.verticalLayout_4.addWidget(self.lineEdit_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(Settings)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(40, 39))
        self.frame_2.setMaximumSize(QSize(40, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_2)

        self.pushButton_4 = QPushButton(Settings)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(40, 39))
        self.pushButton_4.setMaximumSize(QSize(40, 39))
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(Settings)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMinimumSize(QSize(40, 39))
        self.pushButton_5.setMaximumSize(QSize(40, 39))
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.pushButton_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.buttonBox = QDialogButtonBox(Settings)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(Settings)
        self.buttonBox.rejected.connect(Settings.reject)
        self.buttonBox.accepted.connect(Settings.accept)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("Settings", u"\u0424\u0430\u0439\u043b \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.pushButton.setText("")
        self.pushButton.setProperty(u"iconName", QCoreApplication.translate("Settings", u"open", None))
        self.label_2.setText(QCoreApplication.translate("Settings", u"Email", None))
        self.pushButton_2.setText("")
        self.pushButton_2.setProperty(u"iconName", QCoreApplication.translate("Settings", u"plus", None))
        self.pushButton_3.setText("")
        self.pushButton_3.setProperty(u"iconName", QCoreApplication.translate("Settings", u"minus", None))
        self.label_3.setText(QCoreApplication.translate("Settings", u"Domain", None))
        self.pushButton_4.setText("")
        self.pushButton_4.setProperty(u"iconName", QCoreApplication.translate("Settings", u"plus", None))
        self.pushButton_5.setText("")
        self.pushButton_5.setProperty(u"iconName", QCoreApplication.translate("Settings", u"minus", None))
    # retranslateUi

