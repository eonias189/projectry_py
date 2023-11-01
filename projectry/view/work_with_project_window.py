import dearpygui.dearpygui as dpg
from projectry.data.interfaces import Window
from projectry.data.mixins import WindowMixin


class WorkWithProjectWindow(WindowMixin, Window):
    tag = "Work With Project Window"

    def setup_ui(self) -> None:
        with dpg.window(tag=self.tag, width=self.width, height=self.height):
            self.btn = dpg.add_button(
                label="Go To Choose Project", callback=self.handle_btn)
        self.hide()

    def handle_btn(self, sender, sender_data) -> None:
        choose_project_window = self.app.get_window_by_name("choose_project")
        self.app.set_main_window(choose_project_window)
