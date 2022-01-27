from src.ui.main.widgets.amplifier_fields_widget.amplifier_field_widget import \
    AmplifierFieldWidget


class AmplifierOutputFieldWidget(AmplifierFieldWidget):
    def __init__(self, parent=None, *, parameter_name: str, unit: str = ''):
        super().__init__(parent, parameter_name=parameter_name, unit=unit)
        self.line_edit.setReadOnly(True)
