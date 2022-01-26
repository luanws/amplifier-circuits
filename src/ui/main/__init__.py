import traceback

from PyQt5 import QtCore, QtGui, QtSvg, QtWidgets
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

        self.circuits_layout = QtWidgets.QHBoxLayout()
        self.graphics_widget.setLayout(self.circuits_layout)

        self.configure_events()
        self.render_inputs()
        self.render_outputs()
        self.amplifier_output_widget.clear()
        self.render_svg_graphics()

    def configure_events(self):
        self.amplifier_polarizations_combo_box.currentTextChanged.connect(
            self.on_change_polarization)
        self.calculate_push_button.clicked.connect(self.calculate)

    def on_change_polarization(self):
        self.__view_model.amplifier = None
        polarization = self.amplifier_polarizations_combo_box.currentText()
        self.__view_model.set_amplifier_class_by_polarization_name(
            polarization)
        self.render_inputs()
        self.render_outputs()
        self.render_svg_graphics()
        self.amplifier_output_widget.clear()

    def calculate(self):
        try:
            parameters = self.amplifier_input_widget.get_parameters_dict()
            self.__view_model.amplifier = self.__view_model.get_amplifier(
                parameters)
            output = self.__view_model.amplifier()
            self.amplifier_output_widget.output = output
            self.render_svg_graphics()
        except ValueError:
            self.show_error(
                'Dados de entrada incorretos',
                'Preencha os dados de entrada corretamente'
            )
        except ZeroDivisionError:
            self.show_error(
                'Divisão por 0',
                'Não é possível dividir por zero'
            )
        except Exception:
            traceback.print_exc()
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

    def render_outputs(self):
        output = self.__view_model.amplifier_class.output
        self.amplifier_output_widget.output = output

    def render_svg_graphics(self):
        for i in reversed(range(self.circuits_layout.count())):
            self.circuits_layout.itemAt(i).widget().setParent(None)

        paths: list[str] = []
        amplifier = self.__view_model.amplifier
        if amplifier is not None:
            paths.append('data/circuit.svg')
            amplifier.draw().save(paths[-1])

            paths.append('data/circuit_equivalent.svg')
            amplifier.draw_equivalent().save(paths[-1])

            paths.append('data/graph.svg')
            self.__view_model.generate_graphic(paths[-1])
        else:
            paths.append('data/circuit.svg')
            self.__view_model.amplifier_class.draw_void().save(paths[-1])

        for path in paths:
            svg_widget = QtSvg.QSvgWidget(path)
            svg_widget.renderer().setAspectRatioMode(QtCore.Qt.KeepAspectRatio)
            svg_widget.setSizePolicy(
                QtWidgets.QSizePolicy.Expanding,
                QtWidgets.QSizePolicy.Expanding
            )
            self.circuits_layout.addWidget(svg_widget)
