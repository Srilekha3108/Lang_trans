import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from PIL import Image, ImageTk

class LanguageTranslatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Language Translator")
        self.master.geometry("950x700")

        # Load background images
        self.primary_color_image = Image.open("Translator2.jpg")
        self.secondary_color_image = Image.open("Translator2.jpg")

        # Resize background images to match window dimensions
        self.primary_color_image = self.primary_color_image.resize((950, 700))
        self.secondary_color_image = self.secondary_color_image.resize((950, 700))

        # Create labels to display background images
        self.primary_background_image = ImageTk.PhotoImage(self.primary_color_image)
        self.primary_background_label = tk.Label(master, image=self.primary_background_image)
        self.primary_background_label.place(x=0, y=0)

        self.secondary_background_image = ImageTk.PhotoImage(self.secondary_color_image)
        self.secondary_background_label = tk.Label(master, image=self.secondary_background_image)
        self.secondary_background_label.place(x=400, y=0)
        
        # Define languages and their codes
        self.langs=["English","French","German","Italian","Spanish","Tamil","Hindi","Chinese","Korean","Thai","Japanese"]
        self.lang_codes={"English":"en","French":"fr","German":"de","Italian":"it","Spanish":"es","Tamil":"ta","Hindi":"hi","Chinese":"zh-cn","Korean":"ko","Thai":"th","Japanese":"ja"}
        
        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Title label
        self.title_label = ttk.Label(self.master, text="Language Translator", style='Title.TLabel')
        self.title_label.place(relx=0.5, y=20, anchor='center')

        # Content frame
        self.content_frame = ttk.Frame(self.master, padding=(20, 20, 20, 20))
        self.content_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Styled image
        self.style_image = Image.open("Translator.jpg")
        self.style_image = self.style_image.resize((400, 400))  # Resize the image
        self.style_image = ImageTk.PhotoImage(self.style_image)
        self.image_label = tk.Label(self.content_frame, image=self.style_image)
        self.image_label.grid(row=0, column=1, rowspan=8, padx=20, pady=20, sticky="nsew")
        
        # Input widgets
        self.label1 = ttk.Label(self.content_frame, text="Enter text to translate:", style='Text.TLabel')
        self.label1.grid(row=0, column=0, padx=5, pady=10, sticky="w")
        
        self.textbox1 = tk.Text(self.content_frame, height=4, font=('Arial', 12))
        self.textbox1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.textbox1.configure(background="purple", foreground="white")  # Styling text widget
        
        self.label2 = ttk.Label(self.content_frame, text="Select source language:", style='Text.TLabel')
        self.label2.grid(row=2, column=0, padx=5, pady=10, sticky="w")
        
        self.source_lang = ttk.Combobox(self.content_frame, values=self.langs, state="readonly", font=('Arial', 12))
        self.source_lang.current(0)
        self.source_lang.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        
        self.label3 = ttk.Label(self.content_frame, text="Select target language:", style='Text.TLabel')
        self.label3.grid(row=4, column=0, padx=5, pady=10, sticky="w")
        
        self.dest_lang = ttk.Combobox(self.content_frame, values=self.langs, state="readonly", font=('Arial', 12))
        self.dest_lang.current(1)
        self.dest_lang.grid(row=5, column=0, padx=5, pady=5, sticky="ew")
        
        # Translate button
        self.button1 = ttk.Button(self.content_frame, text="Translate", command=self.translate, style='TButton')
        self.button1.grid(row=6, column=0, padx=5, pady=20, sticky="ew")
        
        # Bind mouse-over events to the translate button
        self.button1.bind("<Enter>", self.on_enter_button)
        self.button1.bind("<Leave>", self.on_leave_button)
        
        # Translated text display
        self.label4 = ttk.Label(self.content_frame, text="Translated text:", style='Text.TLabel')
        self.label4.grid(row=7, column=0, padx=5, pady=10, sticky="w")
        
        self.textbox2 = tk.Text(self.content_frame, height=4, state="disabled", font=('Arial', 12))
        self.textbox2.grid(row=8, column=0, padx=5, pady=5, sticky="ew")
        self.textbox2.configure(background="purple", foreground="white")  # Styling text widget

    def translate(self):
        try:
            translate = Translator()
            text = self.textbox1.get("1.0", tk.END)
            src_lang = self.lang_codes[self.source_lang.get()]
            dest_lang = self.lang_codes[self.dest_lang.get()]
            translation = translate.translate(text, src=src_lang, dest=dest_lang)
            self.update_translation(translation.text)
        except Exception as e:
            self.update_translation("Translation failed. Please try again.")

    def update_translation(self, translated_text):
        self.textbox2.config(state="normal")
        self.textbox2.delete("1.0", tk.END)
        self.textbox2.insert(tk.END, translated_text)
        self.textbox2.config(state="disabled")

    def on_enter_button(self, event):
        self.button1.config(foreground='red')

    def on_leave_button(self, event):
        self.button1.config(foreground='black')

if __name__ == "__main__":
    # Initialize Tkinter
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    
    # Define styles
    style = ttk.Style()
    style.configure('TButton', foreground='black', font=('Arial', 12, 'bold'))
    style.configure('Title.TLabel', font=('Arial', 30, 'bold'), foreground='blue')
    style.configure('Text.TLabel', font=('Arial', 12))

    # Run the application
    root.mainloop()
