# coding:utf-8
# 内置信号与自定义函数

from PyQt5.QtWidgets import *
import sys

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('raojixian')
        self.resize(330,50)
        btn = QPushButton('关闭',self)
        btn.clicked.connect(self.btn_close)

    def btn_close(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    example.show()
    sys.exit(app.exec_())