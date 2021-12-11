from FrmUnit import *
from FrmLogin import *
from FrmLogin_prog import *
from FrmUser import *
from FrmUser_prog import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
import MySQLdb as mdb

def signals(self):
    self.PB_add.clicked.connect(self.InsertData)
    self.PB_update.clicked.connect(self.UpdateData)
    self.PB_del.clicked.connect(self.DeleteData)
    self.PB_exit.clicked.connect(self.keluar)
    self.Txt_nounit.textChanged.connect(self.select_data)

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
        pesan(self, QMessageBox.Information,"Connection","Failed to connect to Database")

        sys.exit(1)

def InsertData(self): 
    no_unit = self.Txt_nounit.text()
    tipe = self.Txt_tipe.text()
    luas = self.Txt_luas.text()
    id_owner = self.Txt_idowner.text()
    id_aksescard1 = self.Txt_aksescard1.text()
    id_aksescard2 = self.Txt_aksescard2.text()
    id_aksescard3 = self.Txt_aksescard3.text()
    id_aksescard4 = self.Txt_aksescard4.text()
    id_aksescard5 = self.Txt_aksescard5.text()
    id_kendaraan1 = self.Txt_kendaraan1.text()
    id_kendaraan2 = self.Txt_kendaraan2.text()
    id_kendaraan3 = self.Txt_kendaraan3.text()
    id_kendaraan4 = self.Txt_kendaraan4.text()
    id_kendaraan5 = self.Txt_kendaraan5.text()
    iuranstatus = self.Txt_iuran.text()
    
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("INSERT INTO unit(No unit,tipe,luas,id owner,IdAksesCard1,IdAksesCard2,IdAksesCard3,IdAksesCard4,IdAksesCard5,IdKendaraan1,IdKendaraan2,IdKendaraan3,IdKendaraan4,IdKendaraan5,IuranStatus) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
        cur = con.cursor()
        cur.execute(query, (no_unit,tipe,luas,id_owner,id_aksescard1,id_aksescard2,id_aksescard3,id_aksescard4,id_aksescard5,id_kendaraan1,id_kendaraan2,id_kendaraan3,id_kendaraan4,id_kendaraan5,iuranstatus))
        con.commit()    
        pesan(self, QMessageBox.Information,"Info","Data Inserted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def UpdateData(self):
    no_unit = self.Txt_nounit.text()
    tipe = self.Txt_tipe.text()
    luas = self.Txt_luas.text()
    id_owner = self.Txt_idowner.text()
    id_aksescard1 = self.Txt_aksescard1.text()
    id_aksescard2 = self.Txt_aksescard2.text()
    id_aksescard3 = self.Txt_aksescard3.text()
    id_aksescard4 = self.Txt_aksescard4.text()
    id_aksescard5 = self.Txt_aksescard5.text()
    id_kendaraan1 = self.Txt_kendaraan1.text()
    id_kendaraan2 = self.Txt_kendaraan2.text()
    id_kendaraan3 = self.Txt_kendaraan3.text()
    id_kendaraan4 = self.Txt_kendaraan4.text()
    id_kendaraan5 = self.Txt_kendaraan5.text()
    iuranstatus = self.Txt_iuran.text()

    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        query = ("UPDATE unit SET tipe = %s, luas = %s, IdOwner = %s, IdAksesCard1 = %s, IdAksesCard2 = %s, IdAksesCard3 = %s, IdAksesCard4 = %s, IdAksesCard5 = %s, IdKendaraan1 = %s, IdKendaraan2 = %s, IdKendaraan3 = %s, IdKendaraan4 = %s, IdKendaraan5 = %s, IuranStatus = %s,WHERE NoUnit = %s")
        cur = con.cursor()
        cur.execute(query, (no_unit,tipe,luas,id_owner,id_aksescard1,id_aksescard2,id_aksescard3,id_aksescard4,id_aksescard5,id_kendaraan1,id_kendaraan2,id_kendaraan3,id_kendaraan4,id_kendaraan5,iuranstatus))
        con.commit()    
        
        pesan(self, QMessageBox.Information,"Info","Data Updated Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Update Failed")

def DeleteData(self): 
    no_unit = self.Txt_nounit.text()
            
    try:
        con = mdb.connect('localhost','root','','pbe_final_project_db')
        
        cur = con.cursor()
        cur.execute("DELETE FROM unit WHERE NoUnit = %s", [no_unit])
        con.commit()    

        pesan(self, QMessageBox.Information,"Info","Data Deleted Successfully")

    except mdb.Error as e:
        pesan(self, QMessageBox.Information,"Error","Failed")

def select_data(self):
    try:
        con = mdb.connect(
            host="localhost",
            user="root",
            password="",
            database='pbe_final_project_db'
        )

        no_unit = self.Txt_nounit.text()

        cur = con.cursor()
        
        # cur.execute("SELECT * FROM {} ".format('user'))
        query = ("SELECT * FROM unit WHERE NoUnit= %s")
        cur = con.cursor()
        cur.execute(query, (no_unit))

        result = cur.fetchall()
        # print(str(result))


        if result == ():
            self.Txt_nounit.text()
            self.Txt_tipe.text()
            self.Txt_luas.text()
            self.Txt_idowner.text()
            self.Txt_aksescard1.text()
            self.Txt_aksescard2.text()
            self.Txt_aksescard3.text()
            self.Txt_aksescard4.text()
            self.Txt_aksescard5.text()
            self.Txt_kendaraan1.text()
            self.Txt_kendaraan2.text()
            self.Txt_kendaraan3.text()
            self.Txt_kendaraan4.text()
            self.Txt_kendaraan5.text()
            self.Txt_iuran.text()
            # print(result)
        else:
            for row_number, row_data in enumerate(result):
                # print(row_number)
                # print(row_data)
                for column_number, data in enumerate(row_data):
                    # print(column_number)
                    if (column_number==1):
                        self.Txt_nounit.setText(str(data))
                    elif (column_number==2):
                        self.Txt_tipe.setText(str(data))
                    elif (column_number==3):
                        self.Txt_luas.setText(str(data))
                    elif (column_number==4):
                        self.Txt_idowner.setText(str(data))
                    elif (column_number==5):
                        self.Txt_aksescard1.setText(str(data))
                    elif (column_number==6):
                        self.Txt_aksescard2.setText(str(data))
                    elif (column_number==7):
                        self.Txt_aksescard3.setText(str(data))
                    elif (column_number==8):
                        self.Txt_aksescard4.setText(str(data))
                    elif (column_number==9):
                        self.Txt_aksescard5.setText(str(data))
                    elif (column_number==10):
                        self.Txt_kendaraan1.setText(str(data))
                    elif (column_number==11):
                        self.Txt_kendaraan2.setText(str(data))
                    elif (column_number==12):
                        self.Txt_kendaraan3.setText(str(data))
                    elif (column_number==13):
                        self.Txt_kendaraan4.setText(str(data))
                    elif (column_number==14):
                        self.Txt_kendaraan5.setText(str(data))
                    elif (column_number==15):
                        self.Txt_iuran.setText(str(data))
        
    except mdb.Error as e:
            self.Txt_nounit.text()
            self.Txt_tipe.text()
            self.Txt_luas.text()
            self.Txt_idowner.text()
            self.Txt_aksescard1.text()
            self.Txt_aksescard2.text()
            self.Txt_aksescard3.text()
            self.Txt_aksescard4.text()
            self.Txt_aksescard5.text()
            self.Txt_kendaraan1.text()
            self.Txt_kendaraan2.text()
            self.Txt_kendaraan3.text()
            self.Txt_kendaraan4.text()
            self.Txt_kendaraan5.text()
            self.Txt_iuran.text()
        # pesan(self, QMessageBox.Information,"Error","Id User kosong")

def keluar(self):
    sys.exit(1)

Ui_FrmUnit.signals=signals
Ui_FrmUnit.pesan=pesan
Ui_FrmUnit.DBConnection = DBConnection
Ui_FrmUnit.InsertData = InsertData
Ui_FrmUnit.UpdateData = UpdateData
Ui_FrmUnit.DeleteData = DeleteData
Ui_FrmUnit.select_data = select_data
Ui_FrmUnit.keluar = keluar

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUser = QtWidgets.QMainWindow()
    ui = Ui_FrmUnit()
    ui.setupUi(FrmUser)
    ui.signals()
    FrmUser.show()    
    sys.exit(app.exec_())
