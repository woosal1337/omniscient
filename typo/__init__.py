from gingerit.gingerit import GingerIt

import rich
from rich import pretty
from rich.console import Console

console = Console()

class typos():

    def __init__(self):
        self.setup()

    def setup(self):

        """
        Declares a parser variable, which is being used in the other class functions
        :return:
        """

        self.parser = GingerIt()

    def check(self, text):

        """
        Gets a text as an input argument and checks whether it has any typos or not
        :param text:
        :return:
        """

        try:
            console.print(self.parser.parse(text)["result"][1:], style="green")
            return True

        except:
            console.print("An error has occurred while trying to parse the typo!", style="red")
            return False