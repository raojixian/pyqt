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
        self.btn1 = QPushButton('图片')
        self.label = QLabel()
        self.btn2 = QPushButton('文字')
        self.text = QTextEdit()
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.text)
        self.btn1.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)
        self.setLayout(self.layout)

    def btn1_clicked(self):

        # file,ok = QFileDialog.getOpenFileName(self,'open file','D:/','Image files(*.*,*.jpg *.gif)')
        file,ok = QFileDialog.getOpenFileName(self,'open file','C:/')
        if ok:
            self.label.setPixmap(QPixmap(file))
    #
    # def btn2_clicked(self):
    #     print("load--text")
    #     dlg = QFileDialog()
    #     dlg.setFileMode(QFileDialog.AnyFile)
    #     dlg.setFilter(QDir.Files)
    #     if dlg.exec_():
    #         filenames = dlg.selectedFiles()
    #         f = open(filenames[0], 'r')
    #         with f:
    #             data = f.read()
    #             print(data)
    #             self.text.setText(data)

    def btn2_clicked(self):
        file,ok = QFileDialog.getOpenFileName(self,'open file','C:\\Users\\Administrator\\Documents','Text files(*.txt)')
        print(type(file))
        print(ok)
        if file:
           file = open(file)
            data = file.read()
            print(data)
            self.text.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())