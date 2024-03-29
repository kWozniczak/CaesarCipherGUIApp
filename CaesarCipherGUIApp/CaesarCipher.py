﻿import tkinter as tk
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
        self.row1_container.columnconfigure(0, weight=6)
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


        self.key_label = tk.Label(
            self.row1_container,
            bg=self.color1,
            fg=self.color2,
            font=('Calibri', 16),
            text=f'Key (1-{self.num_letters - 1})',
            justify=tk.CENTER
            )
        
        self.key_label.grid(column=1, row=1, sticky=tk.N, padx=20)
        
        self.key_entry_validation_command = self.row1_container.register(self.key_entry_validation)
        
        self.key_entry = tk.Entry(
            self.row1_container,
            bg=self.color2,
            fg=self.color3,
            selectbackground=self.color1,
            selectforeground=self.color2,
            font=('Calibri', 15),
            width=6,
            highlightthickness=0,
            border=0,
            justify=tk.CENTER,
            validate='key',
            validatecommand=(self.key_entry_validation_command, '%P')
            )
        
        self.key_entry.grid(column=1, row=1, padx=20, ipadx=6,ipady=10)
        
        
        self.button_encrypt = tk.Button(
            self.main_frame,
            bg=self.color2,
            fg=self.color1,
            activebackground=self.color3,
            activeforeground=self.color1,
            font=('Calibri', 15),
            text='Encrypt',
            width=6,
            height=1,
            cursor='hand1',
            highlightthickness=0,
            border=0,
            state=tk.DISABLED,
            command=lambda: [self.encrypt_text(), self.display_in_encrypted_text_label()]
            
        )

        self.button_encrypt.grid(column=0, row=2, pady=20, ipadx=15, ipady=5)
        
        self.encrypted_text_title = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color2,
            font=('Calibri', 14),
            text='Encrypted text',
            justify=tk.CENTER
            )
        
        self.encrypted_text_title.grid(column=0, row=3, sticky=tk.W, padx=70)
     

        self.encrypted_text_label = tk.Label(
            self.main_frame,
            anchor=tk.NW,
            bg=self.color2,
            fg=self.color3,
            font=('Calibri', 15),
            height=4,
            width=65,
            padx=10,
            pady=10,
            justify=tk.LEFT
            )
        
        self.encrypted_text_label.grid(column=0, row=4)
        

        self.button_decrypt = tk.Button(
            self.main_frame,
            bg=self.color2,
            fg=self.color1,
            activebackground=self.color3,
            activeforeground=self.color1,
            font=('Calibri', 15),
            text='Decrypt',
            width=6,
            height=1,
            cursor='hand1',
            highlightthickness=0,
            border=0,
            state=tk.DISABLED,
            command=lambda: [self.decrypt_text(), self.display_in_decrypted_text_label()]
        )

        self.button_decrypt.grid(column=0, row=5, pady=20, ipadx=15, ipady=5)


        self.decrypted_text_title = tk.Label(
            self.main_frame,
            bg=self.color1,
            fg=self.color2,
            font=('Calibri', 14),
            text='Decrypted text',
            justify=tk.CENTER
            )
        
        self.decrypted_text_title.grid(column=0, row=6, sticky=tk.W, padx=70)


        self.decrypted_text_label = tk.Label(
            self.main_frame,
            anchor=tk.NW,
            bg=self.color2,
            fg=self.color3,
            font=('Calibri', 15),
            height=4,
            width=65,
            padx=10,
            pady=10,
            justify=tk.LEFT
            )
        
        self.decrypted_text_label.grid(column=0, row=7)
        

    def encrypt_text(self):
        ciphertext = self.plaintext_text_widget.get('1.0', tk.END)
        result = ''
        alpha= self.letters
        key = self.key_entry.get()
        
        for c in ciphertext:
            if c.isupper():
                alphabet = alpha.upper()
            elif c.islower():
                alphabet = alpha.lower()
            else:
                result += c
                continue
        
            position = alphabet.find(c)
            shifted_position = (position + int(key)) % len(alpha)
            plaintext_letter = alphabet[shifted_position]
            result += plaintext_letter

        return result
    
    def display_in_encrypted_text_label(self):
        my_text = ''
        my_text = self.encrypted_text_label.config(text=self.encrypt_text())


    def decrypt_text(self):
        ciphertext = self.encrypted_text_label.cget('text')
        result = ''
        alpha= self.letters
        key = self.key_entry.get()
        
        for c in ciphertext:
            if c.isupper():
                alphabet = alpha.upper()
            elif c.islower():
                alphabet = alpha.lower()
            else:
                result += c
                continue
        
            position = alphabet.find(c)
            shifted_position = (position - int(key)) % len(alpha)
            encrypted_text_letter = alphabet[shifted_position]
            result += encrypted_text_letter
            
        return result


    def display_in_decrypted_text_label(self):
        my_text = ''
        my_text = self.decrypted_text_label.config(text=self.decrypt_text())


    def key_entry_validation(self, value):
        if value == '':
            self.button_encrypt['state'] = tk.DISABLED
            self.button_decrypt['state'] = tk.DISABLED
            return True
        
        try:
            value = int(value)
        except ValueError:
            return False
        
        if value <= 0 or value >= self.num_letters:
            return False
        
        self.button_encrypt['state'] = tk.NORMAL
        self.button_decrypt['state'] = tk.NORMAL
        
        return True
    

root = tk.Tk()
caesar_cipher_app = CaesarCipher(root)
root.title("Caesar Cipher")
root.geometry('800x720')
root.resizable(width=False, height=False)
root.mainloop()