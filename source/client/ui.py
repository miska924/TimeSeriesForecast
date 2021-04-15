from PyQt5 import QtWidgets, QtGui, QtCore
from design import Ui_MainWindow
import sys
import json

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

 
app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())