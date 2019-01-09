# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog,QToolTip
from PyQt5.QtGui import QFont
from untitled_1 import Ui_MainWindow
from untitled_2 import Ui_Form


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # self.child = children()生成子窗口实例self.child
        self.child = ChildrenForm()

        # 菜单的点击事件，当点击关闭菜单时连接槽函数 close()
        # self.fileCloseAction.triggered.connect(self.close)
        # 菜单的点击事件，当点击打开菜单时连接槽函数 openMsg()
        # self.fileOpenAction.triggered.connect(self.openMsg)

        # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
        # self.addWinAction.triggered.connect(self.childShow)
        self.btn1.clicked.connect(self.childShow)

        self.initUi()
    def initUi(self):
        QToolTip.setFont(QFont('SanSerif', 10))
        self.setToolTip('这是一个<b>气泡提示</b>')

    def childShow(self):
        # 添加子窗口
        self.gridLayout.addWidget(self.child)
        self.child.show()

    # def openMsg(self):
    #     file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "All Files (*);;Text Files (*.txt)")
    #     # 在状态栏显示文件地址
    #     self.statusbar.showMessage(file)


class ChildrenForm(QWidget, Ui_Form):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
