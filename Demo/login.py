# coding:utf-8
import sys
from demo import Ui_raojixian
import hashlib

class SignUP():
    demo = Ui_raojixian()
    id = demo.lineEdit.text ()
    password = demo.lineEdit_3.text()
    print(id,password)

if __name__ == '__main__':
    signUp = SignUP()
    signUp()