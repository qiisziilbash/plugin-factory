import yaml

import factory
import loader

with open("config.yaml", "r") as file:
    agent_names = yaml.safe_load(file)["agent_names"]
    loader.load_plugins(agent_names)


def chat_with(agent_name: str):
    return factory.create({"agent_name": agent_name, "name": "Mario"}).respond()
