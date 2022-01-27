from src.models.amplifier.output import Output
from src.ui.main.widgets.amplifier_fields_widget import AmplifierFieldsWidget
from src.ui.main.widgets.amplifier_output_widget.amplifier_output_field_widget import \
    AmplifierOutputFieldWidget


class AmplifierOutputWidget(AmplifierFieldsWidget):
    __output: Output | None = None

    def get_field_widget(self, parameter_name: str, unit: str) -> AmplifierOutputFieldWidget:
        return AmplifierOutputFieldWidget(parent=self, parameter_name=parameter_name, unit=unit)

    @property
    def output(self) -> Output | None:
        return self.__output

    @output.setter
    def output(self, output: Output):
        self.__output = output
        parameter_names = output.get_parameter_names()
        parameter_units = output.get_parameter_units()
        self.set_parameters(
            parameter_names=parameter_names,
            parameter_units=parameter_units
        )
        self.render()

        for field_widget in self._field_widgets:
            parameter_name = field_widget.parameter_name
            value = self.output.__dict__[parameter_name]
            field_widget.value = value

    def clear(self):
        self.__output = None
        self.render()
