from collections.abc import Callable

from src.ui.main.widgets.amplifier_fields_widget import AmplifierFieldsWidget
from src.ui.main.widgets.amplifier_input_widget.amplifier_input_field_widget import \
    AmplifierInputFieldWidget


class AmplifierInputWidget(AmplifierFieldsWidget):
    __on_return_pressed_callable: Callable[[], None] | None = None

    def get_field_widget(self, parameter_name: str, unit: str) -> AmplifierInputFieldWidget:
        return AmplifierInputFieldWidget(parent=self, parameter_name=parameter_name, unit=unit)

    def render(self):
        result = super().render()
        self.configure_return_pressed()
        return result

    def on_return_pressed(self, callback: Callable[[], None]):
        self.__on_return_pressed_callable = callback

    def configure_return_pressed(self):
        callback = self.__on_return_pressed_callable
        if callback is not None:
            for field_widget in self._field_widgets:
                field_widget.line_edit.returnPressed.connect(callback)
