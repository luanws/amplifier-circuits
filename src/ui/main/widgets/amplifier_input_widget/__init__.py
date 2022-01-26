from PyQt5 import QtWidgets
from src.ui.main.widgets.amplifier_input_widget.amplifier_input_field_widget import \
    AmplifierInputFieldWidget
from src.utils import numerize


class AmplifierInputWidget(QtWidgets.QWidget):
    __parameter_names: list[str] = []
    __parameter_units: list[str] = []
    __input_field_widgets: list[AmplifierInputFieldWidget] = []
    __layout: QtWidgets.QVBoxLayout

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__layout = QtWidgets.QVBoxLayout()
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)
        self.setLayout(self.__layout)
        self.render()

    def render(self):
        for parameter_widget in self.__input_field_widgets:
            self.__layout.removeWidget(parameter_widget)

        self.__input_field_widgets = []
        for parameter_name, unit in zip(self.__parameter_names, self.__parameter_units):
            parameter_widget = AmplifierInputFieldWidget(
                self, parameter_name=parameter_name, unit=unit)
            self.__input_field_widgets.append(parameter_widget)
            self.__layout.addWidget(parameter_widget)

    @property
    def parameters(self):
        return self.__parameter_names

    def set_parameters(self, parameter_names: list[str], parameter_units: list[str]):
        self.__parameter_names = parameter_names
        self.__parameter_units = parameter_units
        self.render()

    def get_parameters_dict(self) -> dict[str, float]:
        parameters_dict = {}
        for input_field_widget in self.__input_field_widgets:
            value = input_field_widget.value
            parameter_name = input_field_widget.parameter_name
            parameters_dict[parameter_name] = value
        return parameters_dict

    def format_parameters(self):
        for input_field_widget in self.__input_field_widgets:
            input_field_widget.format()
