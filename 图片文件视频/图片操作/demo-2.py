import sys, os
from datetime import date, timedelta
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QMarginsF
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtGui import QPageLayout, QPageSize


app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.load(QtCore.QUrl('http://shici.store/poetry-calendar/'))

layout = QPageLayout(
    QPageSize(QPageSize.B5),
    QPageLayout.Portrait, QMarginsF(0, 0, 0, 0)
)

def printFinished():
    page = loader.page()
    print("%s Printing Finished!" % page.title())
    app.exit()

def printToPDF(finished):
    loader.show()
    page = loader.page()
    page.printToPdf("%s.pdf" % page.title(), layout)


loader.page().pdfPrintingFinished.connect(printFinished)
loader.loadFinished.connect(printToPDF)

app.exec_()