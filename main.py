import sys
import os
import random
from datetime import datetime
from passgen_tarantool import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

os.environ.pop("GTK_PATH", None)
os.environ.pop("GIO_MODULE_DIR", None)

if sys.platform.startswith("linux"):
    os.environ["QT_QPA_PLATFORM"] = "xcb"

lower_letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
spechial_symbols = '!@#$%^&*().?' 


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.exit_func)
        self.ui.pushButton.clicked.connect(self.check_status)
        self.ui.actionAbout.triggered.connect(self.about_func)
        

    def check_status(self):
        full_result = ""
        spin = self.ui.spinBox.value()        
        
        if self.ui.checkBox_numbers.isChecked() == False and self.ui.checkBox_lowletter.isChecked() == False and self.ui.checkBox_upletter.isChecked() == False and self.ui.checkBox_specsymbol.isChecked() == False:
            self.ui.label_msg.setText("No items selected :-( ")
        elif self.ui.checkBox_numbers.isChecked() == True and self.ui.checkBox_lowletter.isChecked() == False and self.ui.checkBox_upletter.isChecked() == False and self.ui.checkBox_specsymbol.isChecked() == False:
            res_number = ""
            for i in range(1, spin + 1):
                rand_from_numbers = random.choice(numbers)
                res_number += rand_from_numbers
            full_result = res_number
            self.ui.lineEdit.setText(full_result)
        elif self.ui.checkBox_numbers.isChecked() == False and self.ui.checkBox_lowletter.isChecked() == True and self.ui.checkBox_upletter.isChecked() == False and self.ui.checkBox_specsymbol.isChecked() == False:
            res_lowletter = ""
            for i in range(1, spin + 1):
                rand_from_lowletter = random.choice(lower_letters)
                res_lowletter += rand_from_lowletter
            full_result = res_lowletter
            self.ui.lineEdit.setText(full_result) 
        
        else:
            # spin = self.ui.spinBox.value()
            # if self.ui.checkBox_numbers.isChecked():

            # print(f"Number ->", self.ui.checkBox_numbers.isChecked())
            # print(f"SpecSymbol ->", self.ui.checkBox_specsymbol.isChecked())        
            # print(f"Uppercase ->", self.ui.checkBox_upletter.isChecked())
            # print(f"Lowercase ->", self.ui.checkBox_lowletter.isChecked())
            # print(f"SPINBOX ->", self.ui.spinBox.value())
            print("="*30)
            self.ui.label_msg.setText("")
            rand_from_lowletters = random.choice(lower_letters)
            rand_from_upletters = random.choice(lower_letters).upper()
            rand_from_numbers = random.choice(numbers)
            rand_from_specsymbol = random.choice(spechial_symbols)           
            res = rand_from_lowletters + "" + rand_from_upletters + "" + rand_from_numbers + "" + rand_from_specsymbol
            self.ui.lineEdit.setText(res)
    
    
    def about_func(self):
        QMessageBox.about(self,
            "About", 
            "<h3>Password generate v1.0</h3>"
            "<p>The program generates passwords.</p>"
            "<p>Developer: Tarantool</p>"
            "<p>2026</p>"       
        )


    def exit_func(self):
        exit()




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())