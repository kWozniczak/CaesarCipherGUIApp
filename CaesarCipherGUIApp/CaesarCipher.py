import tkinter as tk
import sys

class CaesarCipher(tk.Frame):
    def __init__(self, root):
        self.color1 = "#B5A8B8"
        self.color2 = "#FEF7FF"
        self.color3 = "#807483"

        self.letters = 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'
        self.num_letters = len(self.letters)
        
        super().__init__(root, bg=self.color1)
        
        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.render_widgets()
        

    def render_widgets(self):  
        self.title = tk.Label(
        self.main_frame,
        bg=self.color1,
        fg=self.color2,
        font=('MS Sans Serif', 22, 'bold'),
        text='Caesar Cipher'
        )
        
        self.title.grid(column=0, row=0, sticky=tk.EW, pady=20)

        self.row1_container = tk.Frame(self.main_frame, bg=self.color1)
        self.row1_container.columnconfigure(0, weight=1)
        self.row1_container.columnconfigure(1, weight=0)
        self.row1_container.grid(column=0, row=1, sticky=tk.NSEW, padx=70)
        
        self.plantext_label = tk.Label(
            self.row1_container,
            bg=self.color1,
            fg=self.color2,
            font=('Calibri', 14),
            text='Plain text',
            justify=tk.CENTER
            )
        
        self.plantext_label.grid(column=0, row=0, sticky=tk.W)
        

        self.plaintext_text_widget = tk.Text(
            self.row1_container,
            bg=self.color2,
            fg=self.color3,
            selectbackground=self.color1,
            selectforeground=self.color2,
            font=('Calibri', 15),
            height=4,
            padx=10,
            pady=10,
            highlightthickness=0,
            border=0
            )
        
        self.plaintext_text_widget.grid(column=0, row=1)



root = tk.Tk()
caesar_cipher_app = CaesarCipher(root)
root.title("Caesar Cipher")
root.geometry('800x500')
root.resizable(width=False, height=False)
root.mainloop()