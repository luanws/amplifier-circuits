from PyQt5 import QtWidgets


class AmplifierOutputWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.__layout = QtWidgets.QVBoxLayout()
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)

        self.setLayout(self.__layout)
