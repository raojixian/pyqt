# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(20, 0, 75, 23))
        self.btn1.setObjectName("btn1")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 30, 751, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionxinjain = QtWidgets.QAction(MainWindow)
        self.actionxinjain.setCheckable(True)
        self.actionxinjain.setObjectName("actionxinjain")
        self.actiondakai = QtWidgets.QAction(MainWindow)
        self.actiondakai.setObjectName("actiondakai")
        self.actionbaocun = QtWidgets.QAction(MainWindow)
        self.actionbaocun.setObjectName("actionbaocun")
        self.actiondaxiao = QtWidgets.QAction(MainWindow)
        self.actiondaxiao.setObjectName("actiondaxiao")
        self.addWinAction = QtWidgets.QAction(MainWindow)
        self.addWinAction.setObjectName("addWinAction")
        self.menu.addAction(self.actionxinjain)
        self.menu.addAction(self.actiondakai)
        self.menu.addAction(self.actionbaocun)
        self.menu_2.addAction(self.actiondaxiao)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.toolBar.addAction(self.addWinAction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn1.setText(_translate("MainWindow", "按钮"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionxinjain.setText(_translate("MainWindow", "新建"))
        self.actionxinjain.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actiondakai.setText(_translate("MainWindow", "打开"))
        self.actiondakai.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionbaocun.setText(_translate("MainWindow", "保存"))
        self.actionbaocun.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actiondaxiao.setText(_translate("MainWindow", "大小"))
        self.addWinAction.setText(_translate("MainWindow", "文件"))
        self.addWinAction.setToolTip(_translate("MainWindow", "文件"))

