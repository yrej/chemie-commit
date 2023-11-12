import tkinter
from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

guiWidth, guiHeight = 600, 600

scene = 1


def akce(scena):
    scena = 2


class GUI(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Chemie")
        self.geometry(f"{guiWidth}x{guiHeight}")
        self.welcomeTitle = ctk.CTkLabel(self, text="CHEMIE", height=50, width=100, anchor=tkinter.CENTER)
        self.welcomeTitle.grid(row=0, column=0, padx=10, pady=10, columnspan=5, sticky="w")
        self.Tlacitko = ctk.CTkButton(self, text="druhe gui", height=100, width=50, command=akce(scene))
        self.Tlacitko.grid(row=1, column=3)


class GUI2(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("POKUS")
        self.geometry(f"{guiWidth}x{guiHeight}")
        self.welcomeTitle = ctk.CTkLabel(self, text="POKUS", height=50, width=100, anchor=tkinter.CENTER)
        self.welcomeTitle.grid(row=0, column=0, padx=10, pady=10, columnspan=5, sticky="w")


if scene == 1:
    app = GUI()
    app.mainloop()

if scene == 2:
    app = GUI2()
    app.mainloop()
