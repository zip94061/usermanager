# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'users.ui'
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
    QDialogButtonBox, QFrame, QHBoxLayout, QListView,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import scr.resources_rc

class Ui_Users(object):
    def setupUi(self, Users):
        if not Users.objectName():
            Users.setObjectName(u"Users")
        Users.resize(325, 635)
        icon = QIcon()
        icon.addFile(u":/dark_theme/icons/dark_theme/users.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Users.setWindowIcon(icon)
        self.verticalLayout_2 = QVBoxLayout(Users)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listView = QListView(Users)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(0, 0))
        self.listView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.listView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        self.horizontalLayout.addWidget(self.listView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Users)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(40, 39))
        self.frame.setMaximumSize(QSize(40, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.pushButton = QPushButton(Users)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(39)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(40, 39))
        self.pushButton.setMaximumSize(QSize(40, 39))
        icon1 = QIcon()
        icon1.addFile(u":/dark_theme/icons/dark_theme/minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.pushButton)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Users)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(Users)
        self.buttonBox.accepted.connect(Users.accept)
        self.buttonBox.rejected.connect(Users.reject)

        QMetaObject.connectSlotsByName(Users)
    # setupUi

    def retranslateUi(self, Users):
        Users.setWindowTitle(QCoreApplication.translate("Users", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.pushButton.setText("")
        self.pushButton.setProperty(u"iconName", QCoreApplication.translate("Users", u"minus", None))
    # retranslateUi

