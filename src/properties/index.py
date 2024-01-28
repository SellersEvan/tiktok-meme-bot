import os
from dotenv import dotenv_values
from src.properties.model import PROPERTIES_DEFAULTS, PROPERTIES_TYPES
from src.static import PROPERTIES_PATH
from src.utility.error import LogError


class Properties:

    def __init__(self):
        if not self._configExists():
            self._createDefaultFile()
        else:
            self._addDefaultsForMissingProperties()
        self._props = self._getEnvFile()
        self._validatePropertiesStructure()


    def _validatePropertiesStructure(self):
        for key, expected_type in PROPERTIES_TYPES.items():
            value = self._props.get(key)
            if value is not None:
                try:
                    setattr(self, key, expected_type(value))
                except ValueError:
                    raise LogError(f"Error Properties - Invalid value for \"{key}\": Expected type {expected_type.__name__}.")
            else:
                setattr(self, key, PROPERTIES_DEFAULTS[key])


    def _addDefaultsForMissingProperties(self):
        with open(PROPERTIES_PATH, "r") as file:
            lines = file.readlines()
            lines = [line for line in lines if line.split("=")[0] in PROPERTIES_TYPES]
        with open(PROPERTIES_PATH, "w") as file:
            for line in lines:
                file.write(line)
            for key, value in PROPERTIES_DEFAULTS.items():
                if not any(line.startswith(f"{key}=") for line in lines):
                    file.write(f"{key}={value}\n")


    def _configExists(self):
        return os.path.exists(PROPERTIES_PATH)


    def _createDefaultFile(self):
        with open(PROPERTIES_PATH, "w") as file:
            for key, value in PROPERTIES_DEFAULTS.items():
                file.write(f"{key}={value}\n")


    def _getEnvFile(self):
        return dotenv_values(PROPERTIES_PATH)


    def __str__(self):
        buffer = "Properties:\n"
        for attr in dir(self):
            if not attr.startswith("_") and not callable(getattr(self, attr)):
                buffer += f"{attr}: {getattr(self, attr)}\n"
        return buffer

