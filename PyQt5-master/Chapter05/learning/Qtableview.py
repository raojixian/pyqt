# coding:utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtPrintSupport import *

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('raojixian')
        # self.resize(200,300)
        self.model = QStandardItemModel(4,4)
        self.model.setHorizontalHeaderLabels(['我','饶','继','先'])
        for i in range(4):
            for j in range(4):
                item = QStandardItem('women %s man %s'%(i,j))
                self.model.setItem(i,j,item)

        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableView)
        self.setLayout(self.layout)












if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())