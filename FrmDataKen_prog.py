from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
from FrmDataKen import *
from FrmFasilitas_prog import signals

def signals(self):
    pass

Ui_FrmDataKen.signals=signals

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmDataKen = QtWidgets.QMainWindow()
    ui = Ui_FrmDataKen()
    ui.setupUi(FrmDataKen)
    ui.signals()
    FrmDataKen.show()
    sys.exit(app.exec_())