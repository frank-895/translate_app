import tkinter as tk
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

class myTranslator:
    @staticmethod
    def trans(text, src_lang, dest_lang):
        text = translator.translate(text, dest=dest_lang, src=source_lang)
        return text

class translateApp(tk.Tk):
    def __init__(self):
        super().__init__() # call superclass method

        self.title("Google Translate App") # name window
        self.geometry('1000x400') # change window size

    def create_label(self):


    
    
if __name__ == "__main__":
    app = translateApp()
    app.mainloop()