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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(325, 635)
        Dialog.setMinimumSize(QSize(325, 635))
        Dialog.setMaximumSize(QSize(325, 635))
        icon = QIcon()
        icon.addFile(u":/dark_theme/icons/dark_theme/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setModal(False)
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 310, 621))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(255, 32))
        self.lineEdit.setMaximumSize(QSize(255, 32))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(40, 39))
        icon1 = QIcon()
        icon1.addFile(u":/dark_theme/icons/dark_theme/open.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listView = QListView(self.layoutWidget)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(255, 0))
        self.listView.setMaximumSize(QSize(255, 16777215))
        self.listView.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_2.addWidget(self.listView)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(255, 32))
        self.lineEdit_2.setMaximumSize(QSize(255, 32))

        self.verticalLayout_2.addWidget(self.lineEdit_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.layoutWidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(40, 39))
        self.frame.setMaximumSize(QSize(40, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.pushButton_2 = QPushButton(self.layoutWidget)
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

        self.pushButton_3 = QPushButton(self.layoutWidget)
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

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listView_2 = QListView(self.layoutWidget)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setMinimumSize(QSize(255, 0))
        self.listView_2.setMaximumSize(QSize(255, 16777215))
        self.listView_2.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_4.addWidget(self.listView_2)

        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(255, 32))
        self.lineEdit_3.setMaximumSize(QSize(255, 32))

        self.verticalLayout_4.addWidget(self.lineEdit_3)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.layoutWidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(40, 39))
        self.frame_2.setMaximumSize(QSize(40, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_5.addWidget(self.frame_2)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QSize(40, 39))
        self.pushButton_4.setMaximumSize(QSize(40, 39))
        self.pushButton_4.setIcon(icon2)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget)
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

        self.buttonBox = QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(Dialog.accept)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0424\u0430\u0439\u043b \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.pushButton.setText("")
        self.pushButton.setProperty(u"iconName", QCoreApplication.translate("Dialog", u"open", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.pushButton_2.setText("")
        self.pushButton_2.setProperty(u"iconName", QCoreApplication.translate("Dialog", u"plus", None))
        self.pushButton_3.setText("")
        self.pushButton_3.setProperty(u"iconName", QCoreApplication.translate("Dialog", u"minus", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Domain", None))
        self.pushButton_4.setText("")
        self.pushButton_4.setProperty(u"iconName", QCoreApplication.translate("Dialog", u"plus", None))
        self.pushButton_5.setText("")
        self.pushButton_5.setProperty(u"iconName", QCoreApplication.translate("Dialog", u"minus", None))
    # retranslateUi

