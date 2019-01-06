# coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import sys

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('raojixian')
        self.layout = QVBoxLayout()
        pic = QPixmap('Qlable.png')
        self.lable = QLabel('raojixian')
        lable1 = QLabel('Raojixian')
        lable2 = QLabel('rao')
        self.layout.addWidget(self.lable)
        self.layout.addWidget(lable1)
        self.layout.addWidget(lable2)

        self.setLayout(self.layout)

        self.lable.setPixmap(pic)
        lable1.setText('i love you')
        movie = QMovie('movie.mp4')
        player = QMediaPlayer()
        
        lable2.setMovie(movie)
        movie.start()
        pic.save('file.png')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())