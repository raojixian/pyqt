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

        self.vertickle  = QVBoxLayout()
        self.button = QPushButton('选择')
        self.label = QLabel()
        self.button.clicked.connect(self.button_click)
        self.btn = QPushButton('打印')
        self.image = QImage()
        self.btn.clicked.connect(self.btn_click)

        self.vertickle.addWidget(self.button)
        self.vertickle.addWidget(self.label)
        self.vertickle.addWidget(self.btn)

        self.setLayout(self.vertickle)


    def button_click(self):
        file,ok = QFileDialog.getOpenFileName(self,'openfile','c:\\',"Image files(*)")
        if ok:
            self.label.setPixmap(QPixmap(file))

    def btn_click(self):
        printer = QPrinter()
        printDialog = QPrintDialog(printer,self)
        if printDialog.exec():
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(),Qt.KeepAspectRatio)
            painter.setViewport(rect.x(),rect.y(),size.width(),size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0,0,self.image)






if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())