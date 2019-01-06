# -*- coding: utf-8 -*-

import sys
import qdarkstyle
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget,QMessageBox
from PyQt5.QtWidgets import QMainWindow,QDialog
from PyQt5.QtCore import *
from demo import *

class WinForm(QDialog,Ui_raojixian):
    def __init__(self, parent=None):
        super(WinForm, self).__init__(parent)
        self.setupUi(self)
        # self.initUi()

        self.lineEdit.setText('raojixian')
        self.lineEdit_3.setText('raojixian')

    @pyqtSlot(login)
    def on_pushButton_clicked_login(self):
        QMessageBox.information(self, '消息', '登录成功', QMessageBox.Yes, QMessageBox.Yes)



    def SignUp(self):
        id = self.lineEdit.text()
        password = self.lineEdit_3.text()
        if id == 'raojixian' and password == 'raojixian':
            QMessageBox.information(self,'消息','登录成功',QMessageBox.Yes,QMessageBox.Yes)
            # self.pushbutton.clicked.connect(self.login)
        else:
            QMessageBox.information(self,'消息','输入信息错误',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

    def login(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    win = WinForm()
    win.show()
    # win.SignUp()
    sys.exit(app.exec_())