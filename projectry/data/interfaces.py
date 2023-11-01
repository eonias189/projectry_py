class Window:
    tag: str

    def setup_ui(self) -> None:
        raise NotImplementedError

    def hide(self) -> None:
        raise NotImplementedError

    def show(self) -> None:
        raise NotImplementedError
