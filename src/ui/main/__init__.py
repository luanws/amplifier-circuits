from typing import List

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.ui.main.view_model import MainViewModel
from src.ui.main.widgets.parameter_widget import ParameterWidget
from src.ui.main.window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel
    parameter_widgets: List[ParameterWidget] = []

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
        for parameter_widget in self.parameter_widgets:
            self.input_vertical_layout.removeWidget(parameter_widget)
        self.parameter_widgets = []

        parameter_names = self.__view_model.amplifier_class.input.get_parameter_names()
        for parameter_name in parameter_names:
            parameter_widget = ParameterWidget(
                self, parameter_name=parameter_name)
            self.parameter_widgets.append(parameter_widget)
            self.input_vertical_layout.addWidget(parameter_widget)
