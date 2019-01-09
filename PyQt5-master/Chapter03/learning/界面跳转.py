# coding:utf-8
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget
from untitled_1 import Ui_MainWindow
from untitled_2 import Ui_Form
import sys

class Example(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Example,self).__init__()
        self.setupUi(self)

        self.children = Children()
        self.addWinAction.triggered.connect(self.childrenShow)

    def childrenShow(self):
        self.gridLayout.addWidget(self.children)
        self.children.show()






class Children(QWidget,Ui_Form):
    def __init__(self):
        super(Children,self).__init__()
        self.setupUi(self)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())