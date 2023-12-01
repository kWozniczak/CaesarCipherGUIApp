import tkinter as tk
import sys

class CaesarCipher(tk.Frame):
    def __init__(self, root):
        self.color1 = "#B5A8B8"
        self.color2 = "#FEF7FF"
        self.color3 = "#807483"

        self.letters = 'a¹bcædeêfghijkl³mnñoópqrsœtuvwxyzŸ¿'
        self.num_letters = len(self.letters)
        
        super().__init__(root, bg=self.color1)
        
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        

root = tk.Tk()
caesar_cipher_app = CaesarCipher(root)
root.title("Caesar Cipher")
root.geometry('800x500')
root.resizable(width=False, height=False)
root.mainloop()