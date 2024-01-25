from dotenv import load_dotenv
import os
from src.config.core import PROPERTIES_PATH

class Properties:
    """
        - "_properties.env" added as global varible to src.config.core
        - add env file to gitignore
        - Load from env file from "_properties.env"
            - if doesn't exist create the file, and use the default values below...
            - you may move or create new object to store the default values below
            - if the file does exist, load the values
        - validate the values and parse the files as the desired type
            - for example verify the property is an int when it's required and parse it as an int or float
            - there could be string types in the future
            - make the parsing system flexible
            - throw friendly errors with messages with errors, telling person which property is invalid
            - you can create an object to define the values and types for validation and put in seperate file if you would like
            - something like...
            - { "CLIP_LENGTH_MIN": "int", "SCREEN_RATIO": "float", "BLA_BLA": "string" }
            - or what ever makes the most sense to you
        - throw friendly error message if properties missing or extra properties
        - make so it can be extended in future easily
    """

    _default = {
        "CLIP_LENGTH_MIN": 20,
        "CLIP_LENGTH_MAX": 60,
        "SCREEN_RATIO": 9 / 16,
        "IMAGE_PADDING": 15
    }

    _types = {
        "CLIP_LENGTH_MIN": int,
        "CLIP_LENGTH_MAX": int,
        "SCREEN_RATIO": float,
        "IMAGE_PADDING": int
    }

    def __init__(self):
        env_exists = self._path_exists(PROPERTIES_PATH)
        if not env_exists:
            self._create_default_env_file()
        else:
            self._update_env_file_with_defaults()
        load_dotenv(PROPERTIES_PATH)
        self._load_and_validate_properties()

    def _load_and_validate_properties(self):
        for key, expected_type in self._types.items():
            value = os.getenv(key)
            if value is not None:
                try:
                    setattr(self, key, expected_type(value))
                except ValueError:
                    raise ValueError(f"Invalid value for {key}. Expected {expected_type.__name__}.")
            else:
                setattr(self, key, self._default[key])

    def _update_env_file_with_defaults(self):
        with open("_properties.env", "r") as file:
            lines = file.readlines()
        updated_lines = [line for line in lines if line.split('=')[0] in self._types]

        with open("_properties.env", "w") as file:
            for line in updated_lines:
                file.write(line)
            for key, value in self._default.items():
                if not any(line.startswith(f"{key}=") for line in updated_lines):
                    file.write(f"{key}={value}\n")

    @staticmethod
    def _path_exists(path):
        return os.path.exists(path)

    @staticmethod
    def _create_default_env_file():
        with open("_properties.env", "w") as file:
            for key, value in Properties._default.items():
                file.write(f"{key}={value}\n")

    def to_string(self):
        return str({key: getattr(self, key) for key in self._types})

if __name__ == "__main__":
    print(Properties().to_string())


