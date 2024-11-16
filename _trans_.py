from translate import Translator


def trans(f_l,t_l,text):
    translator = Translator(from_lang=f_l,to_lang=t_l)

    translated_text = translator.translate(text)

    #
    # print(f"Original text: {text}")
    # print(f"Translated text: {translated_text}")
    return translated_text


# trans("en","ur","reminder")