import json

queries = None
prompts = None
menu = None


filepath = "C:/Users/pkatiyar/OneDrive - WatchGuard Technologies Inc/Desktop/Myyyy proj/src/config.json"
with open(filepath, "r") as file:
    get_data = json.load(file)
    queries = get_data["queries"]
    menu = get_data["menu"]
    prompts = get_data["prompts"]
    constants = get_data["constants"]