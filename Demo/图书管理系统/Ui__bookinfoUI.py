# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\PyQt5\PyQt546\_bookinfoUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(432, 514)
        # 给窗口设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        # 页面布局

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        # iSbn
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.lineEdit_isbn = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_isbn.setInputMask("")
        self.lineEdit_isbn.setClearButtonEnabled(True)
        self.lineEdit_isbn.setObjectName("lineEdit_isbn")
        # 书名
        self.horizontalLayout_3.addWidget(self.lineEdit_isbn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.lineEdit_bookname = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_bookname.setClearButtonEnabled(True)
        self.lineEdit_bookname.setObjectName("lineEdit_bookname")
        self.horizontalLayout_10.addWidget(self.lineEdit_bookname)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        #作者
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.lineEdit_author = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_author.setClearButtonEnabled(True)
        self.lineEdit_author.setObjectName("lineEdit_author")
        self.horizontalLayout_4.addWidget(self.lineEdit_author)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        # 图书分类
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_11.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        ##国家
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_14.addWidget(self.label_13)
        self.lineEdit_country = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_country.setClearButtonEnabled(True)
        self.lineEdit_country.setObjectName("lineEdit_country")
        self.horizontalLayout_14.addWidget(self.lineEdit_country)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        ##出版单位
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_publisher = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_publisher.setClearButtonEnabled(True)
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.horizontalLayout_5.addWidget(self.lineEdit_publisher)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        # 页数
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEdit_pages = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pages.setClearButtonEnabled(True)
        self.lineEdit_pages.setObjectName("lineEdit_pages")
        self.horizontalLayout_7.addWidget(self.lineEdit_pages)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        # 出版年份
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.lineEdit_pudate = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pudate.setClearButtonEnabled(False)
        self.lineEdit_pudate.setObjectName("lineEdit_pudate")
        self.horizontalLayout_6.addWidget(self.lineEdit_pudate)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        # 定价
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.lineEdit_price = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_price.setClearButtonEnabled(True)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.horizontalLayout_8.addWidget(self.lineEdit_price)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        # 内容简介
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.textEdit_content = QtWidgets.QTextEdit(Dialog)
        self.textEdit_content.setObjectName("textEdit_content")
        self.verticalLayout_3.addWidget(self.textEdit_content)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        # self.pushButton_read = QtWidgets.QPushButton(Dialog)
        # self.pushButton_read.setObjectName("pushButton_read")
        # self.horizontalLayout_9.addWidget(self.pushButton_read)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_pic = QtWidgets.QLabel(Dialog)
        self.label_pic.setText("")
        self.label_pic.setPixmap(QtGui.QPixmap("res/book.png"))
        self.label_pic.setScaledContents(True)
        self.label_pic.setObjectName("label_pic")
        self.verticalLayout.addWidget(self.label_pic)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_chioce = QtWidgets.QPushButton(Dialog)
        self.pushButton_chioce.setObjectName("pushButton_chioce")
        self.horizontalLayout_2.addWidget(self.pushButton_chioce)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout_12.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_12.addWidget(self.pushButton_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        # self.pushButton_ok.clicked.connect(Dialog.accept)
        # self.pushButton_cancel.clicked.connect(Dialog.reject)
        # QtCore.QMetaObject.connectSlotsByName(Dialog)

        # self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "新增图书档案"))
        Dialog.setWhatsThis(_translate("Dialog", "新增图书档案"))
        self.label.setText(_translate("Dialog", "*I S B N"))
        self.label_8.setText(_translate("Dialog", "*书    名"))
        self.label_2.setText(_translate("Dialog", "*作    者"))
        self.label_11.setText(_translate("Dialog", "图  书  分  类"))
        self.label_3.setText(_translate("Dialog", "出版单位"))
        self.label_5.setText(_translate("Dialog", "页    数"))
        self.label_4.setText(_translate("Dialog", "出版年份"))
        self.lineEdit_pudate.setInputMask(_translate("Dialog", "9999-9;0"))
        self.label_6.setText(_translate("Dialog", "定    价"))
        self.label_7.setText(_translate("Dialog", "内容简介"))
        self.label_13.setText(_translate("Dialog", "国家"))

        # self.pushButton_read.setText(_translate("Dialog", "读取网络数据"))
        self.label_9.setText(_translate("Dialog", "封面尺寸不要太过于夸张\n"
"网络数据不对请自行调整"))
        self.pushButton_chioce.setText(_translate("Dialog", "选择图书封面..."))
        self.pushButton_ok.setText(_translate("Dialog", "确认"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))

if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication
    import sys
    import qdarkstyle
    app = QApplication(sys.argv)
    # 设置深的格式
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    form = QtWidgets.QWidget()
    window = Ui_Dialog()
    window.setupUi(form)
    form.show()
    sys.exit(app.exec_())

