# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmLogin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmLoginMainWindow(object):
    def setupUi(self, FrmLoginMainWindow):
        FrmLoginMainWindow.setObjectName("FrmLoginMainWindow")
        FrmLoginMainWindow.resize(571, 284)
        self.centralwidget = QtWidgets.QWidget(FrmLoginMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(210, 120, 194, 112))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.userNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.userNameLabel.setObjectName("userNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.userNameLabel)
        self.Txt_username = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_username.setObjectName("Txt_username")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.Txt_username)
        self.passwordLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.Txt_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.Txt_password.setInputMask("")
        self.Txt_password.setObjectName("Txt_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.Txt_password)
        self.PB_login = QtWidgets.QPushButton(self.formLayoutWidget)
        self.PB_login.setObjectName("PB_login")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.PB_login)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 40, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 70, 311, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.PB_testcon = QtWidgets.QPushButton(self.centralwidget)
        self.PB_testcon.setGeometry(QtCore.QRect(260, 330, 127, 28))
        self.PB_testcon.setObjectName("PB_testcon")
        self.PB_msgbox = QtWidgets.QPushButton(self.centralwidget)
        self.PB_msgbox.setGeometry(QtCore.QRect(120, 320, 93, 28))
        self.PB_msgbox.setObjectName("PB_msgbox")
        FrmLoginMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmLoginMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FrmLoginMainWindow)

    def retranslateUi(self, FrmLoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FrmLoginMainWindow.setWindowTitle(_translate("FrmLoginMainWindow", "Login"))
        self.userNameLabel.setText(_translate("FrmLoginMainWindow", "UserName"))
        self.passwordLabel.setText(_translate("FrmLoginMainWindow", "Password"))
        self.PB_login.setText(_translate("FrmLoginMainWindow", "Login"))
        self.label.setText(_translate("FrmLoginMainWindow", "WELCOME TO F3 APARTMENT"))
        self.label_2.setText(_translate("FrmLoginMainWindow", "MANAGEMENT SYSTEM"))
        self.PB_testcon.setText(_translate("FrmLoginMainWindow", "Login"))
        self.PB_msgbox.setText(_translate("FrmLoginMainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmLoginMainWindow = QtWidgets.QMainWindow()
    ui = Ui_FrmLoginMainWindow()
    ui.setupUi(FrmLoginMainWindow)
    FrmLoginMainWindow.show()
    sys.exit(app.exec_())
