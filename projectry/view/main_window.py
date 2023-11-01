import dearpygui.dearpygui as dpg
from projectry.data.interfaces import Window
from projectry.data.mixins import WindowMixin


class MainWindow(WindowMixin, Window):
    tag = "Primaty Window"

    def __init__(self):
        pass

    def setup_ui(self) -> None:
        with dpg.window(tag=self.tag):
            dpg.add_button(label="button")
        dpg.set_primary_window(self.tag, True)
