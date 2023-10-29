import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


class App:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.setup_ui()

    def setup_ui(self) -> None:
        dpg.create_context()
        dpg.create_viewport(title='Custom Title', width=600, height=600)

    def run(self) -> None:
        demo.show_demo()
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
