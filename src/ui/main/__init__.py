from typing import List

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.ui.main.view_model import MainViewModel
from src.ui.main.widgets.amplifier_input_widget import AmplifierInputWidget
from src.ui.main.window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel
    amplifier_input_widget: AmplifierInputWidget

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = MainViewModel()

        amplifier_names = self.__view_model.amplifier_names
        self.amplifier_polarizations_combo_box.addItems(amplifier_names)

        self.amplifier_input_widget = AmplifierInputWidget(self)
        self.input_vertical_layout.addWidget(self.amplifier_input_widget)

        self.configure_events()
        self.render_inputs()

    def configure_events(self):
        self.amplifier_polarizations_combo_box.currentTextChanged.connect(
            self.on_change_polarization)

    def on_change_polarization(self):
        polarization = self.amplifier_polarizations_combo_box.currentText()
        self.__view_model.set_amplifier_class_by_polarization_name(
            polarization)
        self.render_inputs()

    def render_inputs(self):
        parameter_names = self.__view_model.amplifier_class.input.get_parameter_names()
        self.amplifier_input_widget.parameter_names = parameter_names
