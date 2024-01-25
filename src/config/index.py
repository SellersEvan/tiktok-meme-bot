import os
from dotenv import dotenv_values
from src.config.core import CONFIG_PATH

class Config:
    """
        - "_config.env" added as global varible to src.config.core
        - add env file to gitignore
        - Load from env file from "_config.env", if doesn't exist throw an error with friendly message
        - Make it super flexible so more can be added in the future
        - Load each value in from the env file (more could be added in future)
        - Error if extra properties provided in env file
        - Error if required properties are missing
        - Error if one grouped related property is included but not another
            - for example "INSTAGRAM_USERNAME" is included but not "INSTAGRAM_PASSWORD" throw error, but if neither are included, no error needs to be thrown
        - Let's do this by creating an object to define required, optional, and groupped properties
        - you can put this object in another file in the same directory if you want
        
        something like this...
        [
            {
                "isRequired": True,   # requires that all primary exist or throw errors
                "primary": [
                    "REDDIT_CLIENT_ID",
                    "REDDIT_SECRET",
                    "REDDIT_USERNAME",
                    "REDDIT_PASSWORD",
                ],
                "optional": [
                    "REDDIT_USER_AGENT"
                ]
            }, {
                "primary": [           # requires if one exists, the rest must exists
                    "INSTAGRAM_USERNAME",
                    "INSTAGRAM_PASSWORD"
                ],
            }
        ]
    """

    # Modify code below and add extra functions as needed
    # Just ensure these values are accessable if successful after __init__
    # make all private functions begin with underscore
    # keep code clean as possible, flexible, and functions no more than 5-6 lines per

    def __init__(self):
        self._path_exists()
        self.env_vars = self._load_env_file()
        self._validate_and_set_env_vars()

    @staticmethod
    def _path_exists():
        if not os.path.exists(CONFIG_PATH):
            raise ValueError("_config.env not found")

    @staticmethod
    def _load_env_file():
        return dotenv_values(CONFIG_PATH)

    def _validate_and_set_env_vars(self):
        config_structure = [
            {
                "isRequired": True,
                "primary": ["REDDIT_CLIENT_ID", "REDDIT_SECRET", "REDDIT_USERNAME", "REDDIT_PASSWORD"],
                "optional": ["REDDIT_USER_AGENT"]
            },
            {
                "primary": ["INSTAGRAM_USERNAME", "INSTAGRAM_PASSWORD"],
            }
        ]
        self._process_config_structure(config_structure)
        self._check_for_extra_vars(config_structure)

    def _process_config_structure(self, structure):
        for group in structure:
            primary_vars = group.get("primary", [])
            optional_vars = group.get("optional", [])
            is_required = group.get("isRequired", False)

            present_vars = [var for var in primary_vars if self.env_vars.get(var)]
            if is_required and len(present_vars) != len(primary_vars):
                missing_vars = set(primary_vars) - set(present_vars)
                raise ValueError(f"Missing required environment variables: {missing_vars}")
            if not is_required and 0 < len(present_vars) < len(primary_vars):
                missing_vars = set(primary_vars) - set(present_vars)
                raise ValueError(f"Incomplete group of environment variables. Missing: {missing_vars}")

            for var in primary_vars + optional_vars:
                setattr(self, var, self.env_vars.get(var))

    def _check_for_extra_vars(self, structure):
        defined_vars = set()
        for group in structure:
            defined_vars.update(group.get("primary", []))
            defined_vars.update(group.get("optional", []))
        extra_vars = set(self.env_vars.keys()) - defined_vars
        if extra_vars:
            raise ValueError(f"Extra undefined environment variables found in _config.env: {extra_vars}")

    def __str__(self):
        config_str = "Configurations:\n"
        for attr in dir(self):
            if not attr.startswith("_") and not callable(getattr(self, attr)):
                config_str += f"{attr}: {getattr(self, attr)}\n"
        return config_str

if __name__=="__main__":
    try:
        config = Config()
        print(config)
    except ValueError as e:
        print(e)