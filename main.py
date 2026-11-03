import sys
import os
from form import *
from PyQt5 import QtWidgets, QtCore, QtGui

os.environ.pop("GTK_PATH", None)
os.environ.pop("GIO_MODULE_DIR", None)

if sys.platform.startswith("linux"):
    os.environ["QT_QPA_PLATFORM"] = "xcb"



class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.exit_func)


    def exit_func(self):
        exit()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())