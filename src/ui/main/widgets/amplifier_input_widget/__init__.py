from PyQt5 import QtWidgets
from src.ui.main.widgets.amplifier_input_widget.amplifier_input_field_widget import \
    AmplifierInputFieldWidget
from src.utils import numerize


class AmplifierInputWidget(QtWidgets.QWidget):
    __parameter_names: list[str] = []
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

        for parameter_name in self.__parameter_names:
            parameter_widget = AmplifierInputFieldWidget(
                self, parameter_name=parameter_name)
            self.__input_field_widgets.append(parameter_widget)
            self.__layout.addWidget(parameter_widget)

    @property
    def parameter_names(self):
        return self.__parameter_names

    @parameter_names.setter
    def parameter_names(self, parameter_names: list[str]):
        self.__parameter_names = parameter_names
        self.render()

    def get_parameters_dict(self) -> dict[str, float]:
        parameters_dict = {}
        for input_field_widget in self.__input_field_widgets:
            value_str: str = input_field_widget.value
            value = numerize.revert(value_str)
            parameters_dict[input_field_widget.parameter_name] = value
        return parameters_dict
