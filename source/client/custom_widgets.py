from PyQt5 import QtWidgets, QtCore

class List(QtWidgets.QListWidget):
    delete = QtCore.pyqtSignal()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Delete:
            self.delete.emit()