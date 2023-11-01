import dearpygui.dearpygui as dpg
from typing import List
from projectry.controller import Controller
from projectry.data.interfaces import Window
from .main_window import MainWindow


class App:
    controller: Controller
    windows: List[Window]

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.windows = [MainWindow()]
        self.setup_ui()

    def setup_ui(self) -> None:
        dpg.create_context()
        self.setup_windows()
        self.update_windows()
        dpg.create_viewport(title='Custom Title',
                            width=self.width, height=self.height)
        dpg.setup_dearpygui()

    def setup_windows(self) -> None:
        for window in self.windows:
            window.setup_ui()

    def update_windows(self) -> None:
        for window in self.windows:
            window.update()

    def connect_controller(self, controller: Controller) -> None:
        self.controller = controller

    @staticmethod
    def run() -> None:
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
