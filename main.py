import sys
import os
import subprocess
from datetime import datetime
from rdc_tarantool import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

os.environ.pop("GTK_PATH", None)
os.environ.pop("GIO_MODULE_DIR", None)

if sys.platform.startswith("linux"):
    os.environ["QT_QPA_PLATFORM"] = "xcb"



class MyWin(QtWidgets.QMainWindow):
    count = 0
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit_2.triggered.connect(self.exit_func)
        self.ui.pushButton.clicked.connect(self.show_devices)
        self.ui.pushButton_2.clicked.connect(self.open_file)


    def show_devices(self):
        show_dev = subprocess.run(["lsblk", "-o", "NAME,SIZE,TYPE,MOUNTPOINTS"], capture_output=True, text=True)
        # print(show_dev.stdout)
        lst_devs = show_dev.stdout.splitlines()
        for dv in lst_devs:
            self.ui.listWidget.addItem(dv)

       
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "", "Все файлы (*);;Текстовые файлы (*.txt)")
        if file_path:
            print("Выбранный файл", file_path)
            self.ui.lineEdit.setText(file_path)

   
    def exit_func(self):
        exit()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())