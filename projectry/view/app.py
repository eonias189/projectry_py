import dearpygui.dearpygui as dpg
from typing import Dict
from projectry.model import get_screen_size
from projectry.controller import Controller
from projectry.data.interfaces import Window, Application
from .__all_windows__ import WorkWithProjectWindow, ChooseProjectWindow

type WindowName = str


class App(Application):
    controller: Controller
    windows: Dict[WindowName, Window]
    main_window: Window

    def __init__(self):
        screen_size = get_screen_size()
        self.width = screen_size.width
        self.height = screen_size.height

        self.windows = {
            "work_with_project": WorkWithProjectWindow(self.width, self.height, self),
            "choose_project": ChooseProjectWindow(self.width, self.height, self),
        }
        self.main_window = None
        self.setup_ui()

    def setup_ui(self) -> None:
        dpg.create_context()
        dpg.create_viewport(title="projectry",
                            width=self.width, height=self.height)
        dpg.setup_dearpygui()
        self.setup_windows()
        self.set_main_window(self.windows["work_with_project"])

    def get_window_by_name(self, name: str) -> Window:
        return self.windows[name]

    def set_main_window(self, window: Window) -> None:
        if self.main_window is not None:
            dpg.set_primary_window(self.main_window.tag, False)
            self.main_window.hide()
        self.main_window = window
        dpg.set_primary_window(self.main_window.tag, True)
        self.main_window.show()

    def setup_windows(self) -> None:
        for window in self.windows.values():
            window.setup_ui()

    def connect_controller(self, controller: Controller) -> None:
        self.controller = controller

    @staticmethod
    def run() -> None:
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
