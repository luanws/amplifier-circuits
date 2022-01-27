from PyQt5 import QtCore, QtWidgets
from src.utils import numerize


class AmplifierFieldWidget(QtWidgets.QWidget):
    __parameter_name: str
    __unit: str

    def __init__(self, parent=None, *, parameter_name: str, unit: str = ''):
        super().__init__(parent)

        self.__parameter_name = parameter_name
        self.__unit = unit

        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignLeft)

        self.label = QtWidgets.QLabel()
        self.label.setText(parameter_name)
        self.label.setFixedWidth(32)

        self.line_edit = QtWidgets.QLineEdit()

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.setLayout(self.main_layout)

    @property
    def parameter_name(self) -> str:
        return self.__parameter_name

    @property
    def value(self) -> float:
        value_str = self.line_edit.text()
        value = numerize.revert(value_str, unit=self.__unit)
        return value

    @value.setter
    def value(self, value: float):
        value_str = numerize.format(value, unit=self.__unit, precision=4)
        self.line_edit.setText(value_str)

    def format(self):
        self.value = self.value
