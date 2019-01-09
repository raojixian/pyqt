# coding:utf-8
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('raojixian')
        # self.resize(200,300)
        self.layout = QVBoxLayout()
        self.cal = QCalendarWidget()
        self.cal.setMinimumDate(QDate(1980,1,1))
        self.cal.setMaximumDate(QDate(2300,1,1))
        self.cal.setGridVisible(True)
        self.cal.move(20,20)
        date = self.cal.selectedDate()
        print(date)
        self.label = QLabel("时间为：")
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.cal.clicked[QtCore.QDate].connect(self.showDate)

        self.layout.addWidget(self.cal)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def showDate(self,date):
        self.label.setText("时间为："+date.toString('yyyy-MM-dd dddd'))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())