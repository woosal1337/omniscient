import requests
import json

import rich
from rich import pretty
from rich.console import Console

console = Console()

user = requests.get("https://api.github.com/users/woosal1337").json()
console.print(json.dumps(user, sort_keys=True, indent=4))
