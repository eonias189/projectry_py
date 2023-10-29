from projectry.view import App


class Controller:
    app: App

    def __init__(self) -> None:
        pass

    def connect_app(self, app: App) -> None:
        self.app = app

    def run(self) -> None:
        self.app.run()
