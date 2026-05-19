import json
import os

# Loads config.json contents into a Python dictionary
def get_config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(current_dir, "..", "config", "config.json")
    with open(filepath, "r") as file:
        return json.load(file)