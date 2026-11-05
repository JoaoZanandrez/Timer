import tkinter as tk
from tkinter import messagebox


def criar_janela_escondido():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
