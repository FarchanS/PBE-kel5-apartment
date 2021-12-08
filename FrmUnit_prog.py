from FrmLogin import *
from FrmUnit import *
from FrmUnit_prog import *
from FrmUser import *
from FrmUser_prog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb

def signals(self):
    self.PB_user.clicked.connect(self.login)
    # self.PB_testcon.clicked.connect(self.DBConnection)
    # self.PB_msgbox.clicked.connect(self.pesan)

def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def DBConnection(self):
    try:
        db = mdb.connect('localhost', 'root', '', 'pbe_final_project_db')

        pesan(self, QMessageBox.Information,"Connection","Database Connected Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Connection","Database Failed Connected")
        sys.exit(1)     

def login(self):
    self.window = QtWidgets.QMainWindow()
    self.gui = Ui_FrmUser()
    self.gui.setupUi(self.window) 
    self.gui.signals()
    self.window.show()
    # Main.hide()
    # print("signal")

    # self.window = QtWidgets.QMainWindow()
    # self.gui = Ui_FrmUser()
    # self.gui.setupUi(self.window) 
    # self.gui.signals()
    # self.window.show()

    # app = QtWidgets.QApplication(sys.argv)
    # FrmUser = QtWidgets.QMainWindow()
    # ui = Ui_FrmUser()
    # ui.setupUi(FrmUser)
    # FrmUser.show()
    
Ui_FrmUnit.pesan=pesan
Ui_FrmUnit.signals=signals
Ui_FrmUnit.DBConnection = DBConnection
Ui_FrmUnit.login = login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUnit = QtWidgets.QMainWindow()
    ui = Ui_FrmUnit()
    ui.setupUi(FrmUnit)
    ui.signals()
    FrmUnit.show()    
    sys.exit(app.exec_())