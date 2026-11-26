import sys
import os
import subprocess
from datetime import datetime
from rdc_tarantool import *
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QFileDialog, QListWidget

os.environ.pop("GTK_PATH", None)
os.environ.pop("GIO_MODULE_DIR", None)

if sys.platform.startswith("linux"):
    os.environ["QT_QPA_PLATFORM"] = "xcb"



class MyWin(QtWidgets.QMainWindow):
    count = 0
    selected_text = ""
    device = ""
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit_2.triggered.connect(self.exit_func)
        self.ui.pushButton.clicked.connect(self.show_devices_func)
        self.ui.listWidget.itemClicked.connect(self.item_select_func)
        self.ui.pushButton_start.clicked.connect(self.make_iso_func)
        self.ui.pushButton_exit.clicked.connect(self.exit_func)

   
    def show_devices_func(self):
        self.ui.listWidget.clear()
        show_dev = subprocess.run(["lsblk", "-o", "NAME,SIZE,TYPE,MOUNTPOINTS"], capture_output=True, text=True)
        # print(show_dev.stdout)
        lst_devs = show_dev.stdout.splitlines()
        for dv in lst_devs:
            self.ui.listWidget.addItem(dv)

       
    def item_select_func(self, item):
        self.device = ""
        self.selected_text = item.text()
        dev_txt = self.selected_text
        res = dev_txt.split(" ")
        raw_str = res[0]
        for i in raw_str:
            if i.isalnum():
                self.device += i
        print(self.device)       

    
    def make_iso_func(self):
        # device = self.item_select_func(self)
        # dd if=/dev/cdrom of=image.iso
        result = subprocess.run(['dd', f'if=/dev/{self.device}', f'of={self.device}_image.iso', 'status=progress'], capture_output=True, text=True, check=True)
        print(f"Code of return: {result.returncode}")
        print(f"Result {result.stdout}")
        print(f"ERR: {result.stderr}")

   
    def exit_func(self):
        exit()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())