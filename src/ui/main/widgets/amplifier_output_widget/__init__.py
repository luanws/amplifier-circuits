from typing import List, Optional

from PyQt5 import QtWidgets
from src.models.amplifier.output import Output
from src.ui.main.widgets.amplifier_output_widget.amplifier_output_field_widget import \
    AmplifierOutputFieldWidget


class AmplifierOutputWidget(QtWidgets.QWidget):
    __parameter_names: List[str] = []
    __output: Optional[Output] = None
    __output_field_widgets: List[AmplifierOutputFieldWidget] = []
    __layout: QtWidgets.QVBoxLayout

    def __init__(self, parent=None):
        super().__init__(parent)

        self.__layout = QtWidgets.QVBoxLayout()
        self.__layout.setContentsMargins(0, 0, 0, 0)
        self.__layout.setSpacing(0)
        self.setLayout(self.__layout)
        self.render()

    def render(self):
        for output_field_widget in self.__output_field_widgets:
            self.__layout.removeWidget(output_field_widget)
        self.__output_field_widgets = []

        for parameter_name in self.__parameter_names:
            output_field_widget = AmplifierOutputFieldWidget(
                self,
                parameter_name=parameter_name,
            )
            if self.__output is not None:
                value = self.output.__dict__[parameter_name]
                output_field_widget.value = value
            self.__output_field_widgets.append(output_field_widget)
            self.__layout.addWidget(output_field_widget)

    @property
    def parameter_names(self):
        return self.__parameter_names

    @property
    def output(self) -> Optional[Output]:
        return self.__output

    @output.setter
    def output(self, output: Output):
        self.__output = output
        self.__parameter_names = output.get_parameter_names()
        self.render()

    def clear(self):
        self.__output = None
        self.render()
