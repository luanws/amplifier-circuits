from PyQt5 import QtCore, QtWidgets


class AmplifierInputFieldWidget(QtWidgets.QWidget):
    __parameter_name: str

    def __init__(self, parent=None, *, parameter_name: str):
        super().__init__(parent)

        self.__parameter_name = parameter_name

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignLeft)

        self.label = QtWidgets.QLabel()
        self.label.setText(parameter_name)
        self.label.setFixedWidth(32)

        self.line_edit = QtWidgets.QLineEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.setLayout(self.layout)

    @property
    def parameter_name(self) -> str:
        return self.__parameter_name

    @property
    def value(self) -> str:
        return self.line_edit.text()
