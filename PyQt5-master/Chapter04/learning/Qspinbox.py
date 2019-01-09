# coding:utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
    #     self.initUi()
    #
    # def initUi(self):
        self.setWindowTitle('raojixian')
        self.resize(200,300)
        self.layout = QVBoxLayout()
        self.lable = QLabel('current value')
        self.layout.addWidget(self.lable)
        self.sp = QSpinBox()
        self.layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valueChanged)
        self.setLayout(self.layout)

    def valueChanged(self):
        self.lable.setText('current value:'+str(self.sp.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())