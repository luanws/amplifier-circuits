from abc import abstractmethod
from typing import Type

from PyQt5 import QtWidgets
from src.ui.main.widgets.amplifier_fields_widget.amplifier_field_widget import \
    AmplifierFieldWidget


class AmplifierFieldsWidget(QtWidgets.QWidget):
    __parameter_names: list[str] = []
    __parameter_units: list[str] = []
    _field_widgets: list[AmplifierFieldWidget] = []
    __layout: QtWidgets.QVBoxLayout

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedWidth(240)
        self.__layout = QtWidgets.QVBoxLayout()
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)
        self.setLayout(self.__layout)
        self.render()

    @abstractmethod
    def get_field_widget(self, parameter_name: str, unit: str) -> AmplifierFieldWidget:
        pass

    def render(self):
        for parameter_widget in self._field_widgets:
            self.__layout.removeWidget(parameter_widget)

        self._field_widgets = []
        for parameter_name, unit in zip(self.__parameter_names, self.__parameter_units):
            parameter_widget = self.get_field_widget(
                parameter_name=parameter_name, unit=unit)
            self._field_widgets.append(parameter_widget)

        for field_widget in self._field_widgets:
            self.__layout.addWidget(field_widget)

    @ property
    def parameters(self):
        return self.__parameter_names

    def set_parameters(self, parameter_names: list[str], parameter_units: list[str]):
        self.__parameter_names = parameter_names
        self.__parameter_units = parameter_units
        self.render()

    def get_parameters_dict(self) -> dict[str, float]:
        parameters_dict = {}
        for field_widget in self._field_widgets:
            value = field_widget.value
            parameter_name = field_widget.parameter_name
            parameters_dict[parameter_name] = value
        return parameters_dict

    def format_parameters(self):
        for field_widget in self._field_widgets:
            field_widget.format()
