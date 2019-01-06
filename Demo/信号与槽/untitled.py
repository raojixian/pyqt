# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1003, 609)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(240, 150, 195, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.message)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def message(self):
        # my_button = QtWidgets.QMessageBox.information(self,'提示信息框','提示消息')
        # my_button = QtWidgets.QMessageBox.question(self,'question','是否保存')
        # my_button = QtWidgets.QMessageBox.warning(self,'warning','警告')
        # print(my_button)
        # if my_button:
        #     print('保存')
        # else:
        #     print('取消')

        # my_button = QtWidgets.QMessageBox.critical(self,'critical warning','严重警告')
        # my_button = QtWidgets.QMessageBox.aboutQt(self)

        # QtWidgets.QInputDialog.getText(self,'字符串',self.lineEdit.Normal,'请在此输入信息')
        # mystr,ok = QtWidgets.QInputDialog.getInt(self,'整数','请输入一个整数',30,0,100)

        my_list = QtWidgets.QStringList()
        my_list.append('苹果')
        my_list.append('香蕉')
        mystr,ok = QtWidgets.QInputDialog.getItem(self,'下拉框','请选择',my_list)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "按钮"))
        self.label.setText(_translate("Form", "内容"))

