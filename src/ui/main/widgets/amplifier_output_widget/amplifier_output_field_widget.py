from PyQt5 import QtCore, QtWidgets
from src.utils import numerize


class AmplifierOutputFieldWidget(QtWidgets.QWidget):
    __value: float | None
    unit: str

    def __init__(self, parent=None, *, parameter_name: str, unit: str = ''):
        super().__init__(parent)

        self.unit = unit

        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setAlignment(QtCore.Qt.AlignLeft)

        self.label = QtWidgets.QLabel()
        self.label.setText(parameter_name)
        self.label.setFixedWidth(32)

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setReadOnly(True)

        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.setLayout(self.main_layout)

    @property
    def value(self) -> float | None:
        return self.__value

    @value.setter
    def value(self, value: float | None):
        self.__value = value
        value_str = numerize.format(value, unit=self.unit)
        self.line_edit.setText(value_str)
