import os
from yaml import load, Loader


def get_oss_config_file():
    base_path = os.path.abspath(".")
    return os.path.join(base_path, "oss.config.yml")


def get_token():
    oss_file = get_oss_config_file()
    with open(oss_file, 'r', encoding="utf-8") as f:
        return load(f, Loader=Loader).get('alioss')

