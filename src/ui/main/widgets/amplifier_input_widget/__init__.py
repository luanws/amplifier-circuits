from src.ui.main.widgets.amplifier_fields_widget import AmplifierFieldsWidget
from src.ui.main.widgets.amplifier_input_widget.amplifier_input_field_widget import \
    AmplifierInputFieldWidget


class AmplifierInputWidget(AmplifierFieldsWidget):
    def get_field_widget(self, parameter_name: str, unit: str) -> AmplifierInputFieldWidget:
        return AmplifierInputFieldWidget(parent=self, parameter_name=parameter_name, unit=unit)
