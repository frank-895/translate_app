import tkinter as tk
import googletrans
from googletrans import Translator
from tkinter import ttk, messagebox

class translateApp(tk.Tk):
    def __init__(self):
        # main setup
        super().__init__() # call superclass method. Example of multiple inheritance, because class is inheriting from superClass. 
        self.title("Google Translate App") # name window
        self.geometry('1000x400') # change window size
        self.minsize(1000,400)

        # widgets
        self.translate_frame = translateFrame(self)
        self.input_frame = inputFrame(self)
        self.middle_frame = middleFrame(self)

        # run
        self.mainloop()


# SET UP THREE FRAME CLASSES - LEFT MIDDLE RIGHT
class inputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) # call superclass method. Example of multiple inheritance, because class is inheriting from superClass. 
        self.place(x=0, y=0, relwidth=0.4, relheight=1)
        self.create_widgets()

    def create_widgets(self):     
        global original_combo, original_text
        text = ttk.Label(self, text = "Input Text",  font = "Times 15 bold") # title for original textbox
        text.grid(row=0, columnspan=2)

        text = ttk.Label(self, text = "Input Language") # label for input language drop down box
        text.grid(sticky='W', row=2, column=0, padx=15)

        original_text = tk.Text(self, height=10, width=45) # create box for user to input text into
        original_text.grid(row=1, columnspan=2, padx= 15) # column span brings the box across 2 columns

        original_combo = ttk.Combobox(self, width=20, value=language_list)
        original_combo.grid(sticky='W', row=2, column=1, padx=0, pady=5)
        original_combo.current(21) # change default selection to English

class translateFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) # call superclass method. Example of multiple inheritance, because class is inheriting from superClass. 
        self.place(x=600, y=0, relwidth=0.4, relheight=1)
        self.create_widgets()

    def create_widgets(self):      
        global translated_combo, translated_text
        text = ttk.Label(self, text = "Translated Text",  font = "Times 15 bold") # title for translated textbox
        text.grid(row=0, columnspan=2)

        text = ttk.Label(self, text = "Output Language") # label for output language drop down box
        text.grid(sticky='W', row=2, column=0, padx=15)

        translated_text = tk.Text(self, height=10, width=45) # create box for translated text to be displayed in
        translated_text.grid(row=1, columnspan=2, padx=15) # pady brings it down from the top and padx brings it from the left towards the middle

        translated_combo = ttk.Combobox(self, width=20, value=language_list)
        translated_combo.grid(sticky='W', row=2, column=1, padx=0, pady=5)
        translated_combo.current(26) # change default selection to English

class middleFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent) # call superclass method. Example of multiple inheritance, because class is inheriting from superClass. 
        self.place(x=400, y=0, relwidth=0.2, relheight=1)
        self.create_widgets()

    def create_widgets(self):
        translate_button = tk.Button(self, text="TRANSLATE", font="Times 20", command=self.translate_clicked)
        translate_button.grid(row=0, column=0, pady=50)

        clear_button = tk.Button(self, text="CLEAR", font="Times 20", command=self.clear_clicked)
        clear_button.grid(row=1, column=0)

    @staticmethod
    def get_languages():
        """This function retrieves the source and destination language and returns them in a tuple"""
        source_lang = original_combo.get()
        dest_lang = translated_combo.get()
        return (source_lang, dest_lang)        

    @staticmethod
    def translate_clicked():
        source_lang, dest_lang = middleFrame.get_languages() # retrieve languages for translation
        translated_text.delete(1.0, tk.END) # clear text box prior to translation
        translator = Translator() # set up translator
        words = original_text.get(1.0, tk.END) # retrieve words for translation
        words = translator.translate(words, dest=dest_lang, src=source_lang)  # This function translates the text 
        words = words.text # extract the translated text which exists in the attribute text
        translated_text.insert(1.0, words) # This function is the output of the translated text to the screen  

    def clear_clicked(self):
        pass

languages = googletrans.LANGUAGES
language_list = list(languages.values())
language_list =[x.title() for x in language_list] # list of all languages aquired
translateApp()