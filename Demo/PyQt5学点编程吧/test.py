# coding:utf-8
import sys
from Ui__bookinfoUI import Ui_Dialog
from PyQt5.QtWidgets import *

class Example(QDialog,Ui_Dialog):
    def __init__(self):
        super(Example,self).__init__()
        self.setupUi(self)

        self.setUi()

    def setUi(self):
        btn = QPushButton('pk',self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())