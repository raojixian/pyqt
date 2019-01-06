# coding:utf-8
from PyQt5.QtCore import QObject,pyqtSignal
from PyQt5.QtWidgets import QPushButton

class QTypeSignal(QObject):
    sendmsg = pyqtSignal(str,str)

    def __init__(self):
        super(QTypeSignal,self).__init__()

    def run(self):
        self.sendmsg.emit('第一个参数','第二个参数')

class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot,self).__init__()

    def get(self,msg1,msg2):
        print("Qslot get msg .." + msg1+'   '+ msg2)


if __name__ == '__main__':
    send  = QTypeSignal()
    slot = QTypeSlot()

    print('--信号绑定')
    send.sendmsg.connect(slot.get)
    send.run()

    print('---信号断开')
    send.sendmsg.disconnect(slot.get)
    send.run()
