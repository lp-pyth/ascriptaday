# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 09:47:36 2021
PyQt6 URL to PDF (Cookie window on every page)
@author: lux
"""
# install:  conda install -c anaconda pyqt 
import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
url = "YOUR_URL_HERE"

app = QtWidgets.QApplication(sys.argv)
loader = QtWebEngineWidgets.QWebEngineView()
loader.setZoomFactor(1)
loader.page().pdfPrintingFinished.connect(
    lambda *args: print('finished:', args))
loader.load(QtCore.QUrl(url))
def emit_pdf(finished):
    loader.show()
    loader.page().printToPdf("test.pdf")
loader.loadFinished.connect(emit_pdf)
app.exec()