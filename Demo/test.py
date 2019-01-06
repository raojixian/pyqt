# coding:utf-8

from PyQt5.QtWidgets import *
import sys

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.setWindowTitle('raojixian')
        flo = QFormLayout()

        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('normal')
        self.button = QPushButton('按钮')

        flo.addRow('normal',self.lineEdit)
        flo.addRow(self.button)
        self.button.clicked.connect(self.showe)
        self.setLayout(flo)


    def showe(self):
        text = self.lineEdit.text()
        print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())