from translate import Translator


def trans(f_l,t_l,text):
    translator = Translator(from_lang=f_l,to_lang=t_l)

    translated_text = translator.translate(text)

    return translated_text
