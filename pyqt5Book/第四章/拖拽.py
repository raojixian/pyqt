# coding:utf-8
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Combo(QComboBox):
    def __init__(self):
        super(Combo,self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self,e):
        print(e)
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.addItem(e.mimeData().text())

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUi()

    def initUi(self):
        self.layout = QFormLayout()
        self.layout.addRow(QLabel('请把'))
        edit = QLineEdit()
        edit.setDragEnabled(True)
        com = Combo()
        self.layout.addRow(edit,com)
        self.setLayout(self.layout)
        self.setWindowTitle('raojixian')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
