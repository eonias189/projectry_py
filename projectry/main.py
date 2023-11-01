from projectry.view import App
from projectry.controller import Controller


def main() -> None:
    app = App()
    controller = Controller()
    app.connect_controller(controller)
    App.run()
