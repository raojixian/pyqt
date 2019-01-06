# coding:utf-8

from PyQt5.QtCore import QObject,pyqtSignal
class QTypeSignal(QObject):
    # 生成一个信号
    sendmsg = pyqtSignal(object)

    def __init__(self):
        super(QTypeSignal,self).__init__()

    def run(self):
        # 发射信号实现
        self.sendmsg.emit('hello pyqt5')

class QTypeSlot(QObject):
    def __init__(self):
        super(QTypeSlot,self).__init__()
    def get(self,msg):
        print('QSlot get mag +'+msg)
if __name__ == '__main__':
    send = QTypeSignal()
    slot = QTypeSlot()

    print('----把信号绑定到槽函数上')
    # 将信号与槽函数绑定起来
    send.sendmsg.connect(slot.get)
    send.run()

    print('---把信号与槽函数断开')
    send.sendmsg.disconncet(slot.get)
    send.run()