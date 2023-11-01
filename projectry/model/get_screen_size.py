import tkinter as tk
from projectry.data.dataclasses import ScreenSize


def get_screen_size() -> ScreenSize:
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    return ScreenSize(width, height)
