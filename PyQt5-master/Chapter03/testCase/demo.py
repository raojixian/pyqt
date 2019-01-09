# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from MatrixWinUi import Ui_MatrixWin

class Example(QMainWindow,Ui_MatrixWin):
    def __init__(self):
        super(Example,self).__init__()
        self.ui = Ui_MatrixWin()
        self.ui.setupUi(self)
        self.initUi()
    def initUi(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())