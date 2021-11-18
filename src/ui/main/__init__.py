from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from src.ui.main.view_model import MainViewModel
from src.ui.main.window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))
