from typing import List, Optional, Tuple

from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from schemdraw import Drawing
from src.models.amplifier import Amplifier
from src.ui.main.view_model import MainViewModel
from src.ui.main.widgets.amplifier_input_widget import AmplifierInputWidget
from src.ui.main.widgets.amplifier_output_widget import AmplifierOutputWidget
from src.ui.main.window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    __view_model: MainViewModel
    amplifier_input_widget: AmplifierInputWidget
    amplifier_output_widget: AmplifierOutputWidget
    amplifier: Optional[Amplifier] = None

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
        self.render_circuits_svg()

    def configure_events(self):
        self.amplifier_polarizations_combo_box.currentTextChanged.connect(
            self.on_change_polarization)
        self.calculate_push_button.clicked.connect(self.calculate)

    def on_change_polarization(self):
        self.amplifier = None
        polarization = self.amplifier_polarizations_combo_box.currentText()
        self.__view_model.set_amplifier_class_by_polarization_name(
            polarization)
        self.render_inputs()
        self.render_circuit_void_svg()
        self.amplifier_output_widget.clear()

    def calculate(self):
        try:
            parameters = self.amplifier_input_widget.get_parameters_dict()
            self.amplifier = self.__view_model.get_amplifier(parameters)
            output = self.amplifier()
            self.amplifier_output_widget.output = output
            self.render_circuits_svg()
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

    def render_circuits_svg(self):
        for i in reversed(range(self.circuits_layout.count())):
            self.circuits_layout.itemAt(i).widget().setParent(None)

        drawings_and_paths: List[Tuple[str, Drawing]] = []
        if self.amplifier is not None:
            drawings_and_paths.append((
                'data/circuit.svg',
                self.amplifier.draw()
            ))
            drawings_and_paths.append((
                'data/circuit_equivalent.svg',
                self.amplifier.draw_equivalent()
            ))
        else:
            drawings_and_paths.append((
                'data/circuit.svg',
                self.__view_model.amplifier_class.draw_void()
            ))

        for path, drawing in drawings_and_paths:
            drawing.save(path)
            svg_widget = QtSvg.QSvgWidget(path)
            svg_widget.renderer().setAspectRatioMode(QtCore.Qt.KeepAspectRatio)
            self.circuits_layout.addWidget(svg_widget)
