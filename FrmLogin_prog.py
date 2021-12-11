from FrmLogin import *
from FrmLogin_prog import *
from FrmUnit import *
from FrmUnit_prog import *
from FrmUser import *
# from FrmUser_prog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb
import os

def signals(self):
    self.PB_login.clicked.connect(self.login)

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
    try:
        username = self.Txt_username.text()
        password = self.Txt_password.text()

        con = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database="pbe_final_project_db"
        )

        cur = con.cursor()
        cur.execute("SELECT * from user where Nama like '"+username + "'and Pass like '"+password+"'")
        result = cur.fetchone()

        # print(result)

        if result == None:
            pesan(self, QMessageBox.Information,"Failed to Login","Incorrect Email & Password")

        else:
            self.FrmUnit = QtWidgets.QMainWindow()
            self.ui_unit = Ui_FrmUnit()
            self.ui_unit.setupUi(self.FrmUnit)
            self.ui_unit.signals()
            self.FrmUnit.show()  
            self.ui_unit.Lbl_user.setText(username)
            self.ui_unit.Lbl_user_role.setText(result[3])
            self.ui_unit.Lbl_user_role.setVisible(False)

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Some Error")
        

Ui_FrmLoginMainWindow.pesan=pesan
Ui_FrmLoginMainWindow.signals=signals
Ui_FrmLoginMainWindow.DBConnection = DBConnection
Ui_FrmLoginMainWindow.login = login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLoginMainWindow = QtWidgets.QMainWindow()
    ui = Ui_FrmLoginMainWindow()
    ui.setupUi(FrmLoginMainWindow)
    ui.signals()
    FrmLoginMainWindow.show()    
    sys.exit(app.exec_())

    
    
    
    
    
    