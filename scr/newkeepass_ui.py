# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newkeepass.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_newkeepass(object):
    def setupUi(self, newkeepass):
        if not newkeepass.objectName():
            newkeepass.setObjectName(u"newkeepass")
        newkeepass.resize(220, 180)
        newkeepass.setMinimumSize(QSize(220, 180))
        newkeepass.setMaximumSize(QSize(220, 180))
        self.verticalLayout = QVBoxLayout(newkeepass)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(newkeepass)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(newkeepass)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(newkeepass)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(135, 29))
        self.lineEdit.setMaximumSize(QSize(135, 29))

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(newkeepass)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(newkeepass)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(135, 29))
        self.lineEdit_2.setMaximumSize(QSize(135, 29))

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(newkeepass)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(newkeepass)
        self.buttonBox.accepted.connect(newkeepass.accept)
        self.buttonBox.rejected.connect(newkeepass.reject)

        QMetaObject.connectSlotsByName(newkeepass)
    # setupUi

    def retranslateUi(self, newkeepass):
        newkeepass.setWindowTitle(QCoreApplication.translate("newkeepass", u"Keepass +", None))
        self.label_3.setText(QCoreApplication.translate("newkeepass", u"\u041d\u043e\u0432\u0430\u044f \u0431\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label.setText(QCoreApplication.translate("newkeepass", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("newkeepass", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
    # retranslateUi

