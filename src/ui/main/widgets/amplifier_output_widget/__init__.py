from PyQt5 import QtWidgets
from src.models.amplifier.output import Output
from src.ui.main.widgets.amplifier_output_widget.amplifier_output_field_widget import \
    AmplifierOutputFieldWidget


class AmplifierOutputWidget(QtWidgets.QWidget):
    __parameter_names: list[str] = []
    __parameter_units: list[str] = []
    __output: Output | None = None
    __output_field_widgets: list[AmplifierOutputFieldWidget] = []
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

        for parameter_name, parameter_unit in zip(self.__parameter_names, self.__parameter_units):
            output_field_widget = AmplifierOutputFieldWidget(
                self,
                parameter_name=parameter_name,
                unit=parameter_unit
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
    def output(self) -> Output | None:
        return self.__output

    @output.setter
    def output(self, output: Output):
        self.__output = output
        self.__parameter_names = output.get_parameter_names()
        self.__parameter_units = output.get_parameter_units()
        self.render()

    def clear(self):
        self.__output = None
        self.render()
