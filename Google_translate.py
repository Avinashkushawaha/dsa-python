


from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type", src="english", dest="hindi"):
    translator = Translator()
    try:
        translation = translator.translate(text, src=src.lower(), dest=dest.lower())
        return translation.text
    except Exception as e:
        return "Error: Translation failed. Check language selection or internet connection."

def data():
    # Get source and destination languages from dropdowns
    source_lang = comb_sor.get()
    dest_lang = comb_dest.get()
    # Get the text from the source text box
    text_to_translate = Sor_txt.get(1.0, END).strip()
    
    # Perform the translation
    translated_text = change(text=text_to_translate, src=source_lang, dest=dest_lang)
    
    # Display the translated text in the destination text box
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, translated_text)

# Initialize main application window
root = Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg='Green')

# Application title
lab_txt = Label(root, text="Translator", font=("Times New Roman", 40, "bold"), bg='Green', fg='White')
lab_txt.place(x=100, y=40, height=50, width=300)

# Source Text Label
lab_src_txt = Label(root, text="Source Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="green")
lab_src_txt.place(x=100, y=100, height=20, width=300)

# Source Text Box
Sor_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
Sor_txt.place(x=10, y=130, height=150, width=480)

# Language options
languages = list(LANGUAGES.values())

# Source language dropdown
comb_sor = ttk.Combobox(root, value=languages, font=("Times New Roman", 12))
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

# Translate Button
button_translate = Button(root, text="Translate", font=("Times New Roman", 14, "bold"), relief=RAISED, command=data)
button_translate.place(x=170, y=300, height=40, width=150)

# Destination language dropdown
comb_dest = ttk.Combobox(root, value=languages, font=("Times New Roman", 12))
comb_dest.place(x=330, y=300, height=40, width=150)
comb_dest.set("hindi")

# Destination Text Label
lab_dest_txt = Label(root, text="Translated Text", font=("Times New Roman", 20, "bold"), fg="Black", bg="green")
lab_dest_txt.place(x=100, y=360, height=20, width=300)

# Destination Text Box
dest_txt = Text(root, font=("Times New Roman", 20, "bold"), wrap=WORD)
dest_txt.place(x=10, y=400, height=150, width=480)

# Instructions to install the correct googletrans version
module_name = Label(root,  font=("Times New Roman", 20, "bold"), bg="Green", fg="White")
module_name.place(x=100, y=570, height=50, width=300)
module_name_info = Label(root,  bg="Green", font=("Times New Roman", 16, "italic"), fg="White")
module_name_info.place(x=0, y=620, height=50, width=500)

root.mainloop()
