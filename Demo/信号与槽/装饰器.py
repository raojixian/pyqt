# coding:utf-8
from PyQt5 import  QtCore
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QPushButton
import sys
from untitled import Ui_Form

class Example(QWidget,Ui_Form):
    def __init__(self):
        super(Example,self).__init__()

        self.okbutton = QPushButton('pk',self)
        # 设置setObjectName的名称
        self.okbutton.setObjectName('raojixian')

        layout = QHBoxLayout()
        layout.addWidget(self.okbutton)
        self.setLayout(layout)
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_raojixian_clicked(self):
        print('单击ok按钮')
        ex = EX()
        ex.show()

class EX(QWidget,Ui_Form):
    def __init__(self):
        super(EX,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())