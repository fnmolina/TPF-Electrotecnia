import tkinter as tk
import Config
import Menus.MenuSelectOrder                    #WE COMPLEATELY THE CALLER FRAME TO PREVENT CYCLE!
from Menus.MenuLowPass import MenuLowPass
from Menus.MenuHighPass import MenuHighPass
from Menus.MenuAllPass import MenuAllPass
from Menus.MenuBandPass import MenuBandPass
from Menus.MenuNotch import MenuNotch
from Menus.MenuArbitraryPoleZero import MenuArbitraryPoleZero
from UserInput import userInput

separation = 20

class MenuSecondOrder(tk.Frame):  # heredamos de tk.Frame, padre de MenuPrimerOrden
    def __init__(self, parent, controller):
        # parent representa el Frame principal del programa, tenemos que indicarle
        # cuando MenuInputOutput será dibujado

        # controller lo utilizamos cuando necesitamos que el controlador principal del programa haga algo

        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.parent = parent

        # creamos widgets y los agregamos a la pantalla con pack CHANGE SIZE
        self.title = tk.Label(
            self,
            height=1,
            width=50,
            text="2nd Order Filter",
            font=Config.LARGE_FONT,
            background="#ffccd5"
        )

        self.title.pack(side=tk.TOP, fill=tk.BOTH, pady=separation +20)
#LOW PASS FILTER BUTTON
        self.buttonLowPass = tk.Button(
            self,
            height=1,
            width=50,
            text="Low-pass filter",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.lowPassMenu
        )
        self.buttonLowPass.pack( expand=0, fill=tk.NONE, pady=separation)

#HIGH PASS FILTER BUTTON
        self.buttonHighPass = tk.Button(
            self,
            height=1,
            width=50,
            text="High-pass filter",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.highPassMenu
        )
        self.buttonHighPass.pack(expand=0, fill=tk.NONE, pady=separation)

#ALL PASS FILTER BUTTON
        self.buttonAllPass = tk.Button(
            self,
            height=1,
            width=50,
            text="All-pass filter",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.allPassMenu
        )
        self.buttonAllPass.pack(expand=0, fill=tk.NONE, pady=separation)

# BAND PASS FILTER BUTTON
        self.buttonBandPass = tk.Button(
            self,
            height=1,
            width=50,
            text="Band-pass filter",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.bandPassMenu
        )
        self.buttonBandPass.pack(expand=0, fill=tk.NONE, pady=separation)

# NOTCH FILTER BUTTON
        self.buttonNotch = tk.Button(
            self,
            height=1,
            width=50,
            text="Notch filter",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.notchMenu
        )
        self.buttonNotch.pack(expand=0, fill=tk.NONE, pady=separation)
#ARBITRARY POLE ZERO
        self.buttonArbitraryPoleZero = tk.Button(
            self,
            height=1,
            width=50,
            text="(Experimental) Enter Pole/Zero",
            font=Config.SMALL_FONT,
            background="#ccffd5",
            command=self.arbitraryMenu
        )
        self.buttonArbitraryPoleZero.pack(expand=0, fill=tk.NONE, pady=separation)
#Previous Screen
        self.buttonBackFromSecond = tk.Button(
            self,
            height=1,
            width=50,
            text="Select Order",
            font=Config.SMALL_FONT,
            background="#eb1717",
            command=self.backFromSecond
        )
        self.buttonBackFromSecond.pack(side=tk.LEFT, expand=0, fill=tk.NONE, pady=separation+30)

    def lowPassMenu(self):
        # cambiamos de frame
        self.controller.showFrame(MenuLowPass)
        userInput["type"] = "low"

    def highPassMenu(self):
        # cambiamos de frame
        self.controller.showFrame(MenuHighPass)
        userInput["type"] = "high"

    def allPassMenu(self):
        # cambiamos de frame
        self.controller.showFrame(MenuAllPass)
        userInput["type"] = "all"

    def arbitraryMenu(self):
        # cambiamos de frame
        self.controller.showFrame(MenuArbitraryPoleZero)
        userInput["type"] = "guess"

    def bandPassMenu(self):
        # cambiamos de frame
        self.controller.showFrame(MenuBandPass)
        userInput["type"] = "band"

    def notchMenu(self):
        # cambiamos de frame
        self.controller.showFrame(MenuNotch)
        userInput["type"] = "notch"

    def backFromSecond(self):
        # cambiamos de frame
        self.controller.showFrame(Menus.MenuSelectOrder.MenuSelectOrder)

    def focus(self):
        pass

