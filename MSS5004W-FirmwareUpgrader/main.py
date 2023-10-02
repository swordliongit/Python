
import tkinter
import tkinter.messagebox

from configparser import ConfigParser
import threading
from time import sleep
import customtkinter
import json
import os
from crawler import initiate

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class Gui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    
        self.title("Firmware Upgrader")
        self.geometry(f"{550}x{550}")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.pack(pady=20, padx=40, fill="both", expand=True)
        
        self.ModemCountEntry = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Modem Count")
        self.ModemCountEntry.pack(pady=10, padx=10)
        
        self.button_1 = customtkinter.CTkButton(master=self.frame_1, command=self.initiate_action, text="Start Firmware Upgrades")
        self.button_1.pack(pady=10, padx=10)
        
        self.console = customtkinter.CTkTextbox(master=self.frame_1, width=500, height=500)
        self.console.pack(pady=10, padx=10)
        
        
    def on_closing(self):
        """Called when you press the X button to close the program. Kills the GUI and the opened chromedriver threads
        """
        sleep(0.5)

        import psutil
        PROCNAME = "MSS5004W Firmware Upgrader.exe"
        DRIVER = "chromedriver.exe"
        for proc in psutil.process_iter():
            # check whether the process name matches
            if proc.name() == PROCNAME or proc.name() == DRIVER:
                proc.kill()
        sleep(1)
        self.destroy()
          
    def initiate_action(self):
        main_thread = threading.Thread(target=initiate, args=(self.console, int(self.ModemCountEntry.get())))   
        main_thread.start()
        
    def dummy2(self):
        pass
    
    def dummy3(self):
        pass
        
    
    
if __name__ == "__main__":
    # initate the gui
    FUGui = Gui()
    # start the gui
    FUGui.mainloop()