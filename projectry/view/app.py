import dearpygui.dearpygui as dpg
from typing import List
from projectry.controller import Controller
from projectry.data.interfaces.view import Window
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
        for window in self.windows:
            window.setup_ui()
        dpg.create_viewport(title='Custom Title', width=self.width, height=self.height)
        dpg.setup_dearpygui()
    
    def connect_controller(self, controller: Controller) -> None:
        self.controller = controller

    @staticmethod
    def run() -> None:
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
