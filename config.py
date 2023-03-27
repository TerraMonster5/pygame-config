import tkinter as tk

class ConfigMenu(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        screenSize = (self.winfo_screenwidth(), self.winfo_screenheight())

        self.__resolution = tk.StringVar(self)
        self.__windowed = tk.IntVar(self)
        self.__graphics = tk.StringVar(self)

        self.__resolutionDropDown = tk.OptionMenu(self, self.__resolution, "1440x900", "2560x1440", "1920x1080").grid(row=0, column=0)
        self.__windowedCheckButton = tk.Checkbutton(self, text="Windowed", variable=self.__windowed).grid(row=0, column=1)
        self.__graphicsDropDown = tk.OptionMenu(self, self.__graphics, "High", "Medium", "Low").grid(row=1, column=0)

        self.mainloop()

ConfigMenu()