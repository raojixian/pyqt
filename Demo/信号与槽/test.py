# coding:utf-8
from Caohanshu import Ui_Form
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


    def btn1_click(self):
        print('btn1 is clicked')
        self.lineEdit.setText('i love raojixian')
    def btn2_click(self):
        my_str = self.lineEdit_2.text()
        self.textEdit.append(my_str)
        print(self.textEdit.toPlainText())
    def btn3_click(self):
        self.textEdit.clear()
        print('textEdit里面的内容被清除了')
    def btn4_click(self):
        pass
    def btn5_click(self):
        pass
    def commandLinkButton_click(self):
        pass
    def radioButton_click(self):
        mystr = '你点击了同意'
        print(mystr)
        self.textEdit.append(mystr)


    def radioButton_2_click(self):
        print('你点击了不同意')
        if self.radioButton_4.isClicked():
            print('确认不同意')
    def radioButton_3_click(self):
        print('你点击了不知道')
    def radioButton_4_click(self):
        print('你点击了确认')
    def radioButton_5_click(self):
        print('你点击了取消')
    def lcdNumber_click(self):
        pass
    def horizontalSlider_click(self):
        pass
    def verticalSlider_click(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # form = QDialog()
    ex = Example()
    # ex.setupUi(form)
    ex.show()
    sys.exit(app.exec())


