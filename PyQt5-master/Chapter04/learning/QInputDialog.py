# coding:utf-8
from PyQt5.QtWidgets import *
import sys

class Example(QWidget):
    def __init__(self):
        super(Example,self).__init__()
        self.resize(200,300)
        self.setWindowTitle('raojixian')
        self.layout = QVBoxLayout()
        self.btn = QPushButton('请输入语言')
        self.text = QLineEdit("")
        self.btn.clicked.connect(self.btn_clicked)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)
        self.show()

    def btn_clicked(self):
        ##item
        # items = ['C++','python','Java','R']
        # item ,ok = QInputDialog.getItem(self,"select input you language:",
        #                                 "语言列表",items,0,False)
        # if ok:
        #     self.text.setText(str(item))
        # text
        # text,ok = QInputDialog.getText(self,'Text','input your text')
        # if ok:
        #     self.text.setText(str(text))
        # number
        # num,ok = QInputDialog.getInt(self,'text','input your text')
        # if ok:
        #     self.text.setText(str(num))

        font,ok = QFontDialog.getFont()
        if ok:
            self.text.setFont(font)


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())