from dotenv import dotenv_values
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ENV_PATH = f"{DIR_PATH}/.env"


def get_env():
    return dotenv_values(ENV_PATH)
