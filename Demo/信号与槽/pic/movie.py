# coding:utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Example(QWidget):

    def initUI(self):

        self.lb = QLabel(self)
        self.lb.setGeometry(100,50,300,200)

        self.bt1 = QPushButton('开始',self)
        self.bt2 = QPushButton('停止',self)

        self.pix = QPixmap('movie.gif')
        self.lb.setPixmap(self.pix)
        self.lb.setScaledContents(True)

        self.bt1.clicked.connect(self.run)
        self.bt2.clicked.connect(self.run)

        self.show()
    def run(self):
        movie = QMovie("movie.gif")
        self.lb.setMovie(movie)
        if self.sender() == self.bt1:
            movie.start()
        else:
            movie.stop()
            self.lb.setPixmap(self.pix)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())