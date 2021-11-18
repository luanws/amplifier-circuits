from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.ui.main.view_model import MainViewModel
from src.ui.main.window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = MainViewModel()

        amplifier_names = self.__view_model.amplifier_names
        self.amplifier_polarizations_combo_box.addItems(amplifier_names)

        self.configure_events()
        self.configure_inputs()

    def configure_events(self):
        self.amplifier_polarizations_combo_box.currentTextChanged.connect(
            self.on_change_polarization)

    def on_change_polarization(self):
        polarization = self.amplifier_polarizations_combo_box.currentText()
        self.__view_model.set_amplifier_class_by_polarization_name(
            polarization)
        self.configure_inputs()

    def configure_inputs(self):
        for i in reversed(range(self.input_vertical_layout.count())):
            self.input_vertical_layout.itemAt(i).widget().setParent(None)

        parameter_names = self.__view_model.amplifier_class.input.get_parameter_names()
        for parameter_name in parameter_names:
            label = QtWidgets.QLabel(self)
            label.setText(parameter_name)
            self.input_vertical_layout.addWidget(label)
