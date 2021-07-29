import wikipedia

import rich
from rich import pretty
from rich.console import Console

console = Console()


class wikipy():

    def __init__(self):
        pass

    def suggesting(self, *args):

        """
        Take a word/phrase as an input, and try to suggest Wikipedia pages/titles regarding it
        :param args:
        :return:
        """

        try:
            console.print(f"{wikipedia.suggest(f'{args}')}", style="green")
            return True

        except wikipedia.DisambiguationError:
            console.print(wikipedia.DisambiguationError, style="yellow")
            return False

        except:
            console.print(f"An Error has occurred while suggesting for the {args} page on Wikipedia!", style="red")
            return False

    def summarizing(self, *args):

        """
        Take a word/phrase as an input, and return the wikipedia summary of it
        :param args:
        :return:
        """

        try:
            console.print(wikipedia.summary(f"{args}"), style="green")
            return True

        except wikipedia.DisambiguationError:
            console.print(wikipedia.DisambiguationError, style="yellow")
            return False

        except:
            console.print(f"An Error has occurred while searching for the {args} page on Wikipedia!", style="red")
            return False
