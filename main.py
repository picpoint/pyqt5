import sys
import os
import subprocess
from datetime import datetime
from rdc_tarantool import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import QProcess
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
        self.ui.pushButton_umount.clicked.connect(self.umount_device_func)

   
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
        self.ui.label1.setText("Attention!")
        self.ui.label2.setText("The device will be automatically unmounted before the image is created.")       

    
    def make_iso_func(self):
        self.process = QProcess(self)
        self.process.finished.connect(self.on_dd_finished)
        program = 'sudo'
        arguments = [
            'dd',
            f'if=/dev/{self.device}',
            f'of={self.device}_image.iso',
            'status=progress'
        ]
        self.process.start(program, arguments)
        print('dd is started in background')

        # device = self.item_select_func(self)
        # dd if=/dev/cdrom of=image.iso
        # result = subprocess.run(['sudo', 'dd', f'if=/dev/{self.device}', f'of={self.device}_image.iso', 'status=progress'], capture_output=True, text=True, check=True)                
        # print(f"Code of return: {result.returncode}")
        # print(f"Result {result.stdout}")
        # print(f"ERR: {result.stderr}")

    def on_dd_finished(self, exit_code, exit_status):
        print(f"dd is fiinished {exit_code}")
        stdout = self.process.readAllStandardOutput().data().decode()
        stderr = self.process.readAllStandardError().data().decode()

        if exit_code == 0:
            print(f"programm is OK: {stdout}")
        else:
            print(f"dd is ERR: {stderr}")


    def umount_device_func(self):
        self.process = QProcess(self)
        program = 'sudo'
        arguments = [
            'umount',
            f'/dev/{self.device}'
        ]
        self.process.start(program, arguments)
        # res = subprocess.run(['pkexec', 'umount', f'/dev/{self.device}'])
        # print(f"Result {res.returncode}")
        # print(f"ERR: {res.stderr}")

   
    def exit_func(self):
        exit()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())