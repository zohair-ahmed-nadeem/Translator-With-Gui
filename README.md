# 🌍 Translator App by ZAN

A simple yet powerful GUI-based language translator built using Python. Powered by `customtkinter`, `translate`, and `pyperclip`, this app allows you to translate text between over 100 languages with just a few clicks!

## ✨ Features

- 🔍 Auto language detection for input text  
- 🌐 Translate to 100+ languages  
- 📋 One-click copy to clipboard  
- 🖼️ Custom app icon and sleek UI  
- 🧩 Easy to use with a dropdown for target language selection  

## 📸 Preview

![App Screenshot](https://media.discordapp.net/attachments/1265694796308283515/1362891010346320042/image.png?ex=68040aaa&is=6802b92a&hm=2f47face2d3217603fc10eab788df074ab085e42e93faa2e7f13046b2ab46e8f&=&format=webp&quality=lossless&width=442&height=346)

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed.

Install the required packages:

```bash
pip install customtkinter translate pyperclip pillow
```

### Project Structure

```folder map
translator-app/
│
├── main.py             # GUI logic
├── _trans_.py          # Translation logic
├── translator_icon.png # App icon
└── README.md           # Project documentation
```

## 🧠 Usage
Run the application using:
```
python main.py
```

1. Enter the text you want to translate.
2. Select the target language from the dropdown.
3. Click Translate to get the result.
4. Use Copy to clipboard! to quickly copy the translated text.

##🌐 Supported Languages
The app supports over 100 languages including:

- English
- Spanish
- French
- German
- Chinese
- Japanese
- Arabic
- Hindi
...and many more!

Full list is included in the source code via a dictionary called lang_dict.

## 📦 Dependencies

- customtkinter
- translate
- pyperclip
- Pillow (PIL)
Install all at once:
```
pip install -r requirements.txt
```

## 🔧 Customization |For Dev|
You can change the appearance mode or color theme via:
```
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
```
Add or remove languages by modifying the `lang_dict` in `main.py`.

## 📌 Notes

- The translate module may use online services and may require internet access.
- Language detection is handled automatically using "autodetect" as the source language.

## 🧑‍💻 Author
**ZAN**
Feel free to fork, modify, and enhance!

## 📄 License
This project is open-source.
