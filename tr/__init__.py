from googletrans import Translator
from rich.console import Console

console = Console()


class translateit():

    def __init__(self):
        self.setup()

    def setup(self):
        """
        Declaring a translator object to be used in the other functions
        :return:
        """

        self.translator = Translator()


    def tren(self, lyrics):
        """
        Take the required language and the word(s)/sentence(s) as arguments and return the needed and translated
        version of the given input
        :param args:
        :return:
        """

        translation = self.translator.translate(f"""
        {lyrics}""", dest=f"en")

        return translation.text[2:-3]

    def entr(self, *args):
        """
        Take the required language and the word(s)/sentence(s) as arguments and return the needed and translated
        version of the given input
        :param args:
        :return:
        """


        translation = self.translator.translate(f"{args}", dest=f"en")
        console.print(translation.text[2:-3], style="green")
        return translation.text[2:-3]

    def detr(self, *args):
        """
        Take the required language and the word(s)/sentence(s) as arguments and return the needed and translated
        version of the given input
        :param args:
        :return:
        """

        translation = self.translator.translate(f'{args}', dest=f"de")
        console.print(translation.text[2:-3], style="green")
        return translation.text[2:-3]

    def trtr(self, *args):
        """
        Take the required language and the word(s)/sentence(s) as arguments and return the needed and translated
        version of the given input
        :param args:
        :return:
        """

        translation = self.translator.translate(f'{args}', dest=f"tr")
        console.print(translation.text[2:-3], style="green")
        return translation.text[2:-3]

    def frtr(self, *args):
        """
        Take the required language and the word(s)/sentence(s) as arguments and return the needed and translated
        version of the given input
        :param args:
        :return:
        """

        translation = self.translator.translate(f'{args}', dest=f"fr")
        console.print(translation.text[2:-3], style="green")
        return translation.text[2:-3]
