import sys
#import PyQt5
from PyQt5 import QtWidgets, uic

#pyuic5 Test(01.11).ui -o Test(01.11).py

app = QtWidgets.QApplication([])
win = uic.loadUi("D:\Qt5Py\Test(01.11).ui")

win.show()
sys.exit(app.exec())