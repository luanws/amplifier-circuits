from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from src.ui.main.view_model import MainViewModel
from src.ui.main.widgets.amplifier_input_widget import AmplifierInputWidget
from src.ui.main.widgets.amplifier_output_widget import AmplifierOutputWidget
from src.ui.main.window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel
    amplifier_input_widget: AmplifierInputWidget
    amplifier_output_widget: AmplifierOutputWidget

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.setWindowIcon(QtGui.QIcon('icon.ico'))

        self.__view_model = MainViewModel()

        amplifier_names = self.__view_model.amplifier_names
        self.amplifier_polarizations_combo_box.addItems(amplifier_names)

        self.amplifier_input_widget = AmplifierInputWidget(self)
        self.amplifier_output_widget = AmplifierOutputWidget(self)
        self.parameters_layout.addWidget(self.amplifier_input_widget)
        self.parameters_layout.addWidget(self.amplifier_output_widget)

        self.configure_events()
        self.render_inputs()

    def configure_events(self):
        self.amplifier_polarizations_combo_box.currentTextChanged.connect(
            self.on_change_polarization)
        self.calculate_push_button.clicked.connect(self.calculate)

    def on_change_polarization(self):
        polarization = self.amplifier_polarizations_combo_box.currentText()
        self.__view_model.set_amplifier_class_by_polarization_name(
            polarization)
        self.render_inputs()
        self.amplifier_output_widget.clear()

    def calculate(self):
        try:
            parameters = self.amplifier_input_widget.get_parameters_dict()
            output = self.__view_model.calculate(parameters)
            self.amplifier_output_widget.output = output
        except ValueError:
            self.show_error(
                'Dados de entrada incorretos',
                'Preencha os dados de entrada corretamente'
            )

    def show_error(self, error: str, information: str):
        message_box = QtWidgets.QMessageBox()
        message_box.setText(error)
        message_box.setIcon(QtWidgets.QMessageBox.Critical)
        message_box.setWindowTitle('Erro')
        message_box.setDetailedText(information)
        message_box.exec_()

    def render_inputs(self):
        parameter_names = self.__view_model.amplifier_class.input.get_parameter_names()
        self.amplifier_input_widget.parameter_names = parameter_names
