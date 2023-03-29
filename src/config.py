import tkinter as tk
from tkinter import ttk

class ConfigMenu(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        screenSize = (self.winfo_screenwidth(), self.winfo_screenheight())

        resolutions = ["2560x1440", "1920x1080", "1280x720", "1138x640", "1024x768", "1024x576", "960x720", "960x540", "800x600", "640x480", "640x360", "600x480", "512x384", "400x300", "320x256", "320x240"]
        compatRes = [res for res in resolutions if int(res.split("x")[0]) <= screenSize[0]]

        self.__resolution = tk.StringVar(self)
        self.__windowed = tk.IntVar(self)
        self.__graphics = tk.StringVar(self)

        resolutionLabel = ttk.Label(self, text="Screen resolution")
        self.__resolutionDropDown = ttk.Combobox(self, state="disabled", values=compatRes)
        self.__windowedCheckButton = ttk.Checkbutton(self, text="Windowed", variable=self.__windowed)
        graphicsLabel = ttk.Label(self, text="Graphics quality")
        self.__graphicsDropDown = ttk.Combobox(self, state="readonly", values=["High", "Medium", "Low"])

        resolutionLabel.grid(row=0, column=0)
        self.__resolutionDropDown.grid(row=0, column=1)
        self.__windowedCheckButton.grid(row=0, column=2)
        graphicsLabel.grid(row=1, column=0)
        self.__graphicsDropDown.grid(row=1, column=1)

        ttk.Button(self, text="Play!").grid(row=2, column=2)
        ttk.Button(self, text="Quit", command=self.destroy).grid(row=2, column=3)

        self.after(1, self.__windowedEnabled)

        self.mainloop()
    
    def __windowedEnabled(self) -> None:
        if self.__windowed.get():
            self.__resolutionDropDown.configure(state="readonly")
        else:
            self.__resolutionDropDown.configure(state="disabled")
        
        self.after(1, self.__windowedEnabled)

ConfigMenu()