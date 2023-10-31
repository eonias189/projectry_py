import dearpygui.dearpygui as dpg
from projectry.data.interfaces.view import Window


class MainWindow(Window):
    def __init__(self):
        pass

    def setup_ui(self) -> None:
        with dpg.window(tag="Primary Window"):
            dpg.add_button(label="button")
        dpg.set_primary_window("Primary Window", True)
