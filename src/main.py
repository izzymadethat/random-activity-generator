import tkinter as tk
from tkinter import ttk
from layout import Segment

# window
window = tk.Tk()
window.title('KillBore v1.0')
window.geometry('500x550')
window.minsize(width=500, height=550)
window.maxsize(width=500, height=550)

# widgets
Segment(window,
        'Generate 10 random activities',
        'Generate')

# run app
window.mainloop()
