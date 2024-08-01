# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'blog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(865, 562)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget_Titles_name = QListWidget(Form)
        self.listWidget_Titles_name.setObjectName(u"listWidget_Titles_name")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_Titles_name.sizePolicy().hasHeightForWidth())
        self.listWidget_Titles_name.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.listWidget_Titles_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonCreate = QPushButton(Form)
        self.pushButtonCreate.setObjectName(u"pushButtonCreate")

        self.horizontalLayout.addWidget(self.pushButtonCreate)

        self.pushButtonDelete = QPushButton(Form)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")

        self.horizontalLayout.addWidget(self.pushButtonDelete)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Zagolovok = QLabel(Form)
        self.Zagolovok.setObjectName(u"Zagolovok")

        self.horizontalLayout_2.addWidget(self.Zagolovok)

        self.lineEdit_Post_name = QLineEdit(Form)
        self.lineEdit_Post_name.setObjectName(u"lineEdit_Post_name")

        self.horizontalLayout_2.addWidget(self.lineEdit_Post_name)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.textBrowser_Main_text = QTextBrowser(Form)
        self.textBrowser_Main_text.setObjectName(u"textBrowser_Main_text")
        self.textBrowser_Main_text.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textBrowser_Main_text)

        self.pushButton_Save = QPushButton(Form)
        self.pushButton_Save.setObjectName(u"pushButton_Save")

        self.verticalLayout_2.addWidget(self.pushButton_Save)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"MySite CMS", None))
        self.pushButtonCreate.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.Zagolovok.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u043e\u0441\u0442\u0430", None))
        self.pushButton_Save.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

