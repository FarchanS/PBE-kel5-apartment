# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmUnit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmUnit(object):
    def setupUi(self, FrmUnit):
        FrmUnit.setObjectName("FrmUnit")
        FrmUnit.resize(246, 496)
        self.centralwidget = QtWidgets.QWidget(FrmUnit)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 40, 221, 451))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.nounitlabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.nounitlabel.setObjectName("nounitlabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nounitlabel)
        self.Txt_nounit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_nounit.setObjectName("Txt_nounit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Txt_nounit)
        self.namaLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName("namaLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.namaLabel)
        self.Txt_tipe = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_tipe.setObjectName("Txt_tipe")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Txt_tipe)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.Txt_luas = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_luas.setObjectName("Txt_luas")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Txt_luas)
        self.roleLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.roleLabel.setObjectName("roleLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.roleLabel)
        self.Txt_idowner = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_idowner.setObjectName("Txt_idowner")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.Txt_idowner)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.Txt_aksescard1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_aksescard1.setObjectName("Txt_aksescard1")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Txt_aksescard1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.Txt_aksescard2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_aksescard2.setObjectName("Txt_aksescard2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.Txt_aksescard2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.Txt_aksescard3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_aksescard3.setObjectName("Txt_aksescard3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.Txt_aksescard3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.Txt_aksescard4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_aksescard4.setObjectName("Txt_aksescard4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.Txt_aksescard4)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.Txt_aksescard5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_aksescard5.setObjectName("Txt_aksescard5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.Txt_aksescard5)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.Txt_kendaraan1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_kendaraan1.setObjectName("Txt_kendaraan1")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.Txt_kendaraan1)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.Txt_kendaraan2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_kendaraan2.setObjectName("Txt_kendaraan2")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.Txt_kendaraan2)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.Txt_kendaraan3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_kendaraan3.setObjectName("Txt_kendaraan3")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.Txt_kendaraan3)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.Txt_kendaraan4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_kendaraan4.setObjectName("Txt_kendaraan4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.Txt_kendaraan4)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.Txt_kendaraan5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_kendaraan5.setObjectName("Txt_kendaraan5")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.Txt_kendaraan5)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.Txt_iuran = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_iuran.setObjectName("Txt_iuran")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.Txt_iuran)
        self.PB_add = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PB_add.setObjectName("PB_add")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.PB_add)
        self.PB_update = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PB_update.setObjectName("PB_update")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.PB_update)
        self.PB_del = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PB_del.setObjectName("PB_del")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.PB_del)
        self.PB_exit = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PB_exit.setObjectName("PB_exit")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.PB_exit)
        FrmUnit.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmUnit)
        QtCore.QMetaObject.connectSlotsByName(FrmUnit)

    def retranslateUi(self, FrmUnit):
        _translate = QtCore.QCoreApplication.translate
        FrmUnit.setWindowTitle(_translate("FrmUnit", "Form Unit"))
        self.label.setText(_translate("FrmUnit", "UNIT"))
        self.nounitlabel.setText(_translate("FrmUnit", "No Unit"))
        self.namaLabel.setText(_translate("FrmUnit", "Tipe"))
        self.passwordLabel.setText(_translate("FrmUnit", "Luas"))
        self.roleLabel.setText(_translate("FrmUnit", "ID OWNER"))
        self.label_2.setText(_translate("FrmUnit", "IdAksesCard1"))
        self.label_3.setText(_translate("FrmUnit", "IdAksesCard2"))
        self.label_4.setText(_translate("FrmUnit", "IdAksesCard3"))
        self.label_5.setText(_translate("FrmUnit", "IdAksesCard4"))
        self.label_6.setText(_translate("FrmUnit", "IdAksesCard5"))
        self.label_7.setText(_translate("FrmUnit", "IdKendaraan1"))
        self.label_8.setText(_translate("FrmUnit", "IdKendaraan2"))
        self.label_9.setText(_translate("FrmUnit", "IdKendaraan3"))
        self.label_10.setText(_translate("FrmUnit", "IdKendaraan4"))
        self.label_11.setText(_translate("FrmUnit", "IdKendaraan5"))
        self.label_12.setText(_translate("FrmUnit", "IuranStatus"))
        self.PB_add.setText(_translate("FrmUnit", "Add"))
        self.PB_update.setText(_translate("FrmUnit", "Update"))
        self.PB_del.setText(_translate("FrmUnit", "Delete"))
        self.PB_exit.setText(_translate("FrmUnit", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmUnit = QtWidgets.QMainWindow()
    ui = Ui_FrmUnit()
    ui.setupUi(FrmUnit)
    FrmUnit.show()
    sys.exit(app.exec_())
