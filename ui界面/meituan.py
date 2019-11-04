# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meituan.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1800, 950)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(99999, 99999))
        Form.setStyleSheet("QWidget#Form{\n"
"border-image: url(:/newPrefix/mages/5e2ef5bc5be18e1c7babf0e1eaad04d6.png);}")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1120, 120, 341, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1120, 270, 341, 111))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1120, 430, 341, 111))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1120, 590, 341, 111))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(40, 20, 821, 931))
        self.textEdit.setStyleSheet("\n"
"font: 14pt \"楷体\";")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 30, 751, 220))
        self.label.setStyleSheet("border-image: url(:/newPrefix/mages/Figure_1.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 260, 751, 220))
        self.label_2.setStyleSheet("border-image: url(:/newPrefix/mages/Figure_1-1.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 490, 751, 220))
        self.label_3.setStyleSheet("border-image: url(:/newPrefix/mages/Figure_1-2.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 720, 749, 220))
        self.label_4.setStyleSheet("border-image: url(:/newPrefix/mages/Figure_1-3.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 761, 461))
        self.label_5.setStyleSheet("\n"
"border-image: url(:/newPrefix/mages/人气商圈.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(70, 230, 761, 461))
        self.label_6.setStyleSheet("border-image: url(:/newPrefix/mages/美食聚集地.png);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(70, 230, 761, 461))
        self.label_7.setStyleSheet("border-image: url(:/newPrefix/mages/服饰商圈-1.png);")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.btn_1)
        self.pushButton_2.clicked.connect(Form.btn_2)
        self.pushButton_3.clicked.connect(Form.btn_3)
        self.pushButton_4.clicked.connect(Form.btn_4)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "最受欢迎的商圈"))
        self.pushButton_2.setText(_translate("Form", "人均消费"))
        self.pushButton_3.setText(_translate("Form", "最佳美食聚集地"))
        self.pushButton_4.setText(_translate("Form", "服饰类综合评分最高的商圈"))
        self.label_6.setText(_translate("Form", "TextLabel"))
        self.label_7.setText(_translate("Form", "TextLabel"))
import MT_rc
