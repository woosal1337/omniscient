import os
import requests, json
from dotenv import load_dotenv

import rich
from rich import pretty
from rich.console import Console

console = Console()

load_dotenv()


class water():
    def __init__(self):
        self.setup()

    def setup(self):

        """
        Setup and configuration
        :return:
        """

        self.base = "http://api.openweathermap.org/data/2.5/weather?"
        self.api_key = os.environ["API_KEY"]

    def temp(self, city):

        """
        Gets a city/country as an argument and returns the weather regarding information of it
        :param city:
        :return:
        """

        try:

            if city:

                complete_url = self.base + "appid=" + self.api_key + "&q=" + city
                response = requests.get(complete_url)
                response = response.json()["main"]

                console.print(f"{city}:", style="yellow")
                console.print(f"Temperature: {round(int(response['temp']) - 273.15, 3)}", style="green")
                console.print(f'Max Temperature {round(int(response["temp_max"]) - 273.15, 3)}', style="green")
                console.print(f'Min Temperature {round(int(response["temp_min"]) - 273.15, 3)}', style="green")
                console.print(f'Pressure {response["pressure"]}', style="green")
                console.print(f'Humidity {response["humidity"]}', style="green")

            else:

                city = "Istanbul"

                complete_url = self.base + "appid=" + self.api_key + "&q=" + city
                response = requests.get(complete_url)
                response = response.json()["main"]

                console.print(f"{city}:", style="yellow")
                console.print(f"Temperature: {round(int(response['temp']) - 273.15, 3)}", style="green")
                console.print(f'Max Temperature {round(int(response["temp_max"]) - 273.15, 3)}', style="green")
                console.print(f'Min Temperature {round(int(response["temp_min"]) - 273.15, 3)}', style="green")
                console.print(f'Pressure {response["pressure"]}', style="green")
                console.print(f'Humidity {response["humidity"]}', style="green")

            return True

        except:

            console.print("An Error Occurred in the Weather Feature", style="red")
            return False