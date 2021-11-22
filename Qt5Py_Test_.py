import sys
from mydesign import Ui_MainWindow
from PyQt5 import QtWidgets, uic

#pyuic5 Test(01.11).ui -o Test(01.11).py

#app = QtWidgets.QApplication([])
#win = uic.loadUi("D:\Qt5Py\Test(01.11).ui")

#win.show()
#sys.exit(app.exec())

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
 
 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())