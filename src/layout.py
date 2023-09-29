import tkinter as tk
from tkinter import ttk

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text):
        super().__init__(master=parent)

        style = ttk.Style()
        style.configure('Text.TLabel', font=('Arial', 15))
        style.configure('Button.TButton', font=('Arial', 12))

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)

        ttk.Label(
            self,
            text=label_text,
            style='Text.TLabel'
            ).grid(row=0, column=0, sticky='nsew')
        ttk.Button(
            self, text=button_text,
            style='Button.TButton'
            ).grid(row=1, column=0, sticky='nsew')

        self.results_box = tk.Text(self, wrap=tk.WORD)
        self.results_box.grid(row=2, column=0, columnspan=2, sticky='news')


        self.pack(padx=50, pady=50)
