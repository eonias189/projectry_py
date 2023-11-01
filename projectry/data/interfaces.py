class Window:
    def setup_ui(self) -> None:
        raise NotImplementedError

    def hide(self) -> None:
        raise NotImplementedError

    def show(self) -> None:
        raise NotImplementedError


class Application:
    def set_main_window(self, w: Window) -> None:
        raise NotImplementedError

    def get_window_by_name(self, name: str) -> Window:
        raise NotImplementedError
