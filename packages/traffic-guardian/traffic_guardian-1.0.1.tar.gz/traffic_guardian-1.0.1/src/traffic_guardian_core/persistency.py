import json
import os

PROXY_RULES_JSON_FILENAME = "proxy_rules.json"


def get_proxy_rules_json_filename():
    return PROXY_RULES_JSON_FILENAME


def write_proxy_rules_form_json(filename, conent):
    with open(filename, "w") as f:
        json.dump(conent, f)


def read_proxy_rules_form_json(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    else:
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}