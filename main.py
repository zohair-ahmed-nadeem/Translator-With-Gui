import tkinter as tk
from tkinter import ttk
from _trans_ import trans
import pyperclip

lang_dict = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb",
    "Chinese (Simplified)": "zh",
    "Chinese (Traditional)": "zh-TW",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw",
    "Hebrew": "he",
    "Hindi": "hi",
    "Hmong": "hmn",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Korean": "ko",
    "Kurdish (Kurmanji)": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar (Burmese)": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Chichewa": "ny",
    "Odia (Oriya)": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots Gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Filipino": "tl",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"
}
def enter():
    global tl
    global translated
    lang = tl_combo.get()
    tl = lang_dict.get(lang)
    text = text_var.get()
    # t_l = tl_combo.get()
    translated = trans("autodetect", tl, text)
    f_result.set(translated)


def copy():
    pyperclip.copy(translated)
root = tk.Tk()
root.geometry("650x400")
root.title("Translator By ZAN")



head = tk.Label(root,text="Translator...",font=("Arial",20))
head.grid(row=0,column=1,padx=5,pady=5)

ip_l = tk.Label(root,text="Enter Text:",font=("Arial",14))
ip_l.grid(row=1,column=1,pady=10)

text_var = tk.StringVar()
ip_e = tk.Entry(root,textvariable=text_var,font=("Arial",14))
ip_e.grid(row=1,column=2)

tl_combo = ttk.Combobox(root, values=list(lang_dict.keys()))
tl_combo.grid(row=1,column=3)

translate_btn = tk.Button(root,text="Translate",command=enter)
translate_btn.grid(row=2,column=1)

f_result = tk.StringVar()
result = tk.Label(root,textvariable=f_result)
result.grid(row=3,column=1, pady=20)

copy_btn = tk.Button(root,text="copied to clipboard!",command=copy)
copy_btn.grid(row=4,column=2)

root.mainloop()