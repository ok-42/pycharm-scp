import json
from typing import TypedDict


class Mapping(TypedDict):
    local_project_path: str
    remote_project_path: str


class Login(TypedDict):
    user: str
    host: str


class Config(TypedDict):
    mapping: Mapping
    login: Login


def setup(config_path: str) -> Config:
    """Read a config file containing paths and login data for remote machine.

    :param config_path: path to JSON file
    :return: dict with configuration
    """
    with open(config_path, 'r', encoding='utf-8') as file:
        config: Config = json.load(file)
    return config
