import json

queries = None
prompts = None
menu = None

with open("config.json", "r") as file:
    get_data = json.load(file)
    queries = get_data["queries"]
    menu = get_data["menu"]
    prompts = get_data["prompts"]
    constants = get_data["constants"]