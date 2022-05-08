import json
import yaml

def read_json(file_path):
    with open(file_path) as file:
        data = file.read()
        return json.loads(data)

def load_config(filename):
    with open(filename, 'r') as config:
        return yaml.full_load(config)