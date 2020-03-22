import requests

from hogwarts_httprunner1.loader import load_yaml

def run_yaml(yaml_file):
    load_json = load_yaml(yaml_file)
    method = load_json.pop("method")
    url = load_json.pop("url")
    resp = requests.request(method, url, **load_json)
    return resp