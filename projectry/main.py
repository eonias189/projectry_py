from projectry.view import App
from projectry.controller import Controller


def main() -> None:
    width, height = 600, 400
    app = App(600, 400)
    controller = Controller()
    app.connect_controller(controller)
    app.run()
