# coding:utf-8
from untitled import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Example(QWidget,Ui_Form):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        pass

    # def radioButton_click(self):
    #     str = '我'
    #     print(str)
    # def radioButton_click_2(self):
    #     str = '爱'
    #     print(str)
    #     self.radioButton_5.setChecked(True)
    # def radioButton_click_3(self):
    #     str = '你'
    #     print(str)
    #     self.radioButton_4.setChecked(True)
    # def radioButton_click_5(self):
    #     str = '确认'
    #     print(str)
    # def radioButton_click_4(self):
    #     str = '取消'
    #     print(str)
    @pyqtSlot()
    def on_dial_valueChanged_(vale):
        print(vale)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # form = QDialog()
    ex = Example()
    # ex.setupUi(form)
    ex.show()
    sys.exit(app.exec())