from typing import Optional

from PyQt5 import QtCore, QtWidgets


class AmplifierOutputFieldWidget(QtWidgets.QWidget):
    __value: Optional[float]

    def __init__(self, parent=None, *, parameter_name: str):
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignLeft)

        self.label = QtWidgets.QLabel()
        self.label.setText(parameter_name)
        self.label.setFixedWidth(32)

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setReadOnly(True)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.setLayout(self.layout)

    @property
    def value(self) -> Optional[float]:
        return self.__value

    @value.setter
    def value(self, value: Optional[float]):
        self.__value = value
        value_str = '%.4g' % value
        self.line_edit.setText(value_str)
