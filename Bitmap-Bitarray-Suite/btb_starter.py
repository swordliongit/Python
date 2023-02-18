#
# Author: Kılıçarslan SIMSIKI
#


import threading
from time import sleep
import customtkinter

from bitmap_bitarray_converter import main
from bitmap_bitarray_converter import read_grid_from_file

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

# Bitmap Bitarray Suite
class BBS(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        
        self.grid_columnconfigure((0, 1, 2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=0)
        self.grid_rowconfigure(3, weight=1)

        self.title("Grid Selector")
        self.geometry(f"{260}x{230}")
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.height_label= customtkinter.CTkLabel(master=self ,text="Height:", font=("Roboto", 24))
        self.height_label.grid(row=0, column=0, pady=12, padx=10)
        self.height_input = customtkinter.CTkEntry(master=self, placeholder_text="")
        self.height_input.grid(row=0, column=1, pady=12, padx=10)
        
        self.width_label= customtkinter.CTkLabel(master=self ,text="Width:", font=("Roboto", 24))
        self.width_label.grid(row=1, column=0, pady=12, padx=10)
        self.width_input = customtkinter.CTkEntry(master=self, placeholder_text="")
        self.width_input.grid(row=1, column=1, pady=12, padx=10)
        
        self.start_button = customtkinter.CTkButton(master=self, text="New Bitmap", command=self.start_BBS_new)
        self.start_button.grid(row=2, column=0, pady=12, padx=12, columnspan=3)
        
        self.start_button = customtkinter.CTkButton(master=self, text="Load Bitmap", command=self.start_BBS_loaded)
        self.start_button.grid(row=3, column=0, pady=12, padx=12, columnspan=3)

    def on_closing(self):
        """Called when you press the X button to close the program. Kills the GUI
        """
        self.destroy()
        
          
    def start_BBS_new(self):
        """_summary_
        """
        if self.height_input.get() != "" and self.width_input.get() != "":
            t = threading.Thread(target=main, args=(int(self.height_input.get()), int(self.width_input.get()), []))
            t.start()
            self.destroy()
            
          
    def start_BBS_loaded(self):
        """_summary_
        """
        t = threading.Thread(target=read_grid_from_file)
        t.start()
        self.destroy()
        
    
if __name__ == "__main__":
    # initate the gui
    BBS = BBS()
    # start the gui
    BBS.mainloop()