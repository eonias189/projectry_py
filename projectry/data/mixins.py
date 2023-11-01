import dearpygui.dearpygui as dpg


class WindowMixin:
    tag: str

    def update(self) -> None:
        pass

    def is_shown(self) -> bool:
        return dpg.is_item_shown(self.tag)

    def hide(self) -> None:
        if self.is_shown():
            dpg.hide_item(self.tag)

    def show(self) -> None:
        if not self.is_shown():
            dpg.show_item(self.tag)
