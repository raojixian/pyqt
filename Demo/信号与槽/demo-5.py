# coding:utf-8
'''
1.定义信号
2.定义槽函数
3.连接信号与槽函数
4.发射信号
'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class CustSignal(QObject):
    # 定义信号
    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int,str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    signal6 = pyqtSignal([int,str],[str])

    def __init__(self):
        super(CustSignal,self).__init__()
        # 连接信号与槽函数
        self.signal1.connect(self.signalCall1)
        self.signal2.connect(self.signalCall2)
        self.signal3.connect(self.signalCall3)
        self.signal4.connect(self.signalCall4)
        self.signal5.connect(self.signalCall5)
        self.signal6[int,str].connect(self.signalCall6)
        self.signal6[str].connect(self.signalCall6Overload)

        # 发射信号
        self.signal1.emit()
        self.signal2.emit(1)
        self.signal3.emit(1,'raojixian')
        self.signal4.emit([1,2,3,4])
        self.signal5.emit({"name":"raojixian","age":"25"})
        self.signal6[int,str].emit(1,'raojixian')
        self.signal6[str].emit("raojixian")
    # 定义槽函数

    def signalCall1(self):
        print('signal1 emit')

    def signalCall2(self,val):
        print('signal2 emit,value',val)

    def signalCall3(self,val,text):
        print('signal3 emit,value',val,text)

    def signalCall4(self,val):
        print('signal4 emit,value',val)

    def signalCall5(self,val):
        print('signal5 emit,value',val)

    def signalCall6(self,val,text):
        print('signal6 emit,value',val,text)

    def signalCall6Overload(self,val):
        print('signal6 Overload emit,value',val)

if __name__ == '__main__':
    custSignal = CustSignal()



