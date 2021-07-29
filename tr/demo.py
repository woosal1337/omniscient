from googletrans import Translator

translator = Translator()

translation = translator.translate('Katze', dest="en")
print(translation)