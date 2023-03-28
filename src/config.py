import tkinter as tk
from tkinter import ttk

class ConfigMenu(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        screenSize = (self.winfo_screenwidth(), self.winfo_screenheight())

        self.__resolution = tk.StringVar(self)
        self.__windowed = tk.IntVar(self)
        self.__graphics = tk.StringVar(self)

        tk.Label(self, text="Screen resolution").grid(row=0, column=0)
        self.__resolutionDropDown = ttk.Combobox(self, state="readonly", values=["1440x900", "2560x1440", "1920x1080"]).grid(row=0, column=1)
        self.__windowedCheckButton = tk.Checkbutton(self, text="Windowed", variable=self.__windowed).grid(row=0, column=2)
        tk.Label(self, text="Graphics quality").grid(row=1, column=0)
        self.__graphicsDropDown = ttk.Combobox(self, state="readonly", values=["High", "Medium", "Low"]).grid(row=1, column=1)

        tk.Button(self, text="Play!").grid(row=2, column=2)
        tk.Button(self, text="Quit", command=self.destroy).grid(row=2, column=3)

        self.mainloop()

ConfigMenu()