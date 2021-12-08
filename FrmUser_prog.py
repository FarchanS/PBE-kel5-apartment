from FrmUser import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb

def signals(self):
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.PB_exit.clicked.connect(self.keluar)
    self.PB_pesan.clicked.connect(self.pesan2)


def pesan(self, ikon, judul, isipesan):
        msgBox = QMessageBox()
        msgBox.setIcon(ikon)
        msgBox.setText(isipesan)
        msgBox.setWindowTitle(judul)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

def pesan2(self):
    pesan(self, QMessageBox.Information,"Info","Dah masuk")

def DBConnection(self):
    try:
        db = mdb.connect('localhost', 'root', '', 'pbe_final_project_db')

        pesan(self, QMessageBox.Information,"Connection","Database Connected Successfully")
    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Connection","Failed to connect to Database")

        sys.exit(1)

def InsertData(self): 
    id_user = self.Txt_id_user.text()
    nama = self.Txt_nama.text()
    password = self.Txt_password.text()
    role = self.Cmb_role.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("INSERT INTO user(IdUser, Nama, Pass, Role) VALUES(%s, %s, %s, %s)")
        cur = con.cursor()
        cur.execute(query, (id_user, nama, password, role))
        con.commit()    
        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    id_user = self.Txt_id_user.text()
    nama = self.Txt_nama.text()
    password = self.Txt_password.text()
    role = self.Cmb_role.currentText()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("UPDATE user SET Nama = %s, Pass = %s, Role = %s WHERE IdUser = %s")
        cur = con.cursor()
        cur.execute(query, (nama, password, role, id_user))
        con.commit()    
        # QMessageBox.about(self, 'Updated', 'Data Updated Successfully')
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    id_user = self.Txt_id_user.text()
            
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM user WHERE IdUser = %s", [id_user])
        con.commit()    

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")
    # QMessageBox.about(self, 'Deleted', 'Data Deleted Successfully')
    # self.close()

def select_data(self):
    try:
        dbname = self.lineEdit_7.text()
        tablename = self.lineEdit_8.text()
        con = mdb.connect(

            host="localhost",
            user="root",
            password="",
            database=dbname
        )

        cur = con.cursor()

        cur.execute("SELECT * FROM {} ".format(tablename))

        result = cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            print(row_number)
            print(row_data)
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(column_number)
                print(str(data))
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    except mdb.Error as e:
        QMessageBox.about(self, 'Error', 'Some Error')
        
def keluar(self):
    sys.exit(1)


Ui_FrmUser.pesan2=pesan2
Ui_FrmUser.signals=signals
Ui_FrmUser.pesan=pesan
Ui_FrmUser.DBConnection = DBConnection
Ui_FrmUser.InsertData = InsertData
Ui_FrmUser.UpdateData = UpdateData
Ui_FrmUser.DeleteData = DeleteData
Ui_FrmUser.select_data = select_data
Ui_FrmUser.keluar = keluar


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUser = QtWidgets.QMainWindow()
    ui = Ui_FrmUser()
    ui.setupUi(FrmUser)
    ui.signals()
    FrmUser.show()    
    sys.exit(app.exec_())