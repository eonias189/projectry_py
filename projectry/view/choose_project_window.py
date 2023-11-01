import dearpygui.dearpygui as dpg
from projectry.data.interfaces import Window
from projectry.data.mixins import WindowMixin


class ChooseProjectWindow(WindowMixin, Window):
    tag = "Choose Project Window"

    def setup_ui(self) -> None:
        with dpg.window(tag=self.tag, width=self.width, height=self.height):
            self.btn = dpg.add_button(
                label="Go To Work With Project Window", callback=self.handle_btn)
        self.hide()

    def handle_btn(self, sender, sender_data) -> None:
        work_with_project_window = self.app.get_window_by_name(
            "work_with_project")
        self.app.set_main_window(work_with_project_window)
