import dearpygui.dearpygui as dpg
from .interfaces import Application


class WindowMixin:
    app: Application
    tag: str | int
    width: int
    height: int

    def __init__(self, width: int, height: int, app: Application):
        self.width = width
        self.height = height
        self.app = app

    def is_shown(self) -> bool:
        return dpg.is_item_shown(self.tag)

    def hide(self) -> None:
        if self.is_shown():
            dpg.hide_item(self.tag)

    def show(self) -> None:
        if not self.is_shown():
            dpg.show_item(self.tag)
