from PyQt5 import QtCore, QtWidgets


class ParameterWidget(QtWidgets.QWidget):
    def __init__(self, parent=None, *, parameter_name: str):
        super().__init__(parent)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setAlignment(QtCore.Qt.AlignLeft)

        self.label = QtWidgets.QLabel()
        self.label.setText(parameter_name)
        self.label.setFixedWidth(32)

        self.line_edit = QtWidgets.QLineEdit()
        self.line_edit.setFixedWidth(160)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)
        self.setLayout(self.layout)
