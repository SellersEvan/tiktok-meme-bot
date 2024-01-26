import os
from dotenv import dotenv_values
from src.config.model import CONFIG_STRUCTURE
from src.config.core import CONFIG_PATH
from src.utility.error import LogError


class Config:

    def __init__(self):
        self._configExists()
        self._props = self._getEnvFile()
        self._validateConfigStructure()
        self._validateNoExtraProperties()


    def _validateConfigStructure(self):
        for group in CONFIG_STRUCTURE:
            isRequired    = group.get("isRequired", False)
            propsPrimary  = group.get("primary", [])
            propsOptional = group.get("optional", [])
            propsPresent  = [var for var in propsPrimary if self._props.get(var)]

            if isRequired and len(propsPresent) != len(propsPrimary):
                propMissing = set(propsPrimary) - set(propsPresent)
                raise LogError(f"Config Error - Missing required properties: {propMissing}")
            if not isRequired and 0 < len(propsPresent) < len(propsPrimary):
                propMissing = set(propsPrimary) - set(propsPresent)
                raise LogError(f"Config Error - Missing group of properties: {propMissing}")
            
            for var in propsPrimary + propsOptional:
                setattr(self, var, self._props.get(var))


    def _validateNoExtraProperties(self):
        propsDefined = set()
        for group in CONFIG_STRUCTURE:
            propsDefined.update(group.get("primary", []))
            propsDefined.update(group.get("optional", []))
        propsExtras = set(self._props.keys()) - propsDefined
        if propsExtras:
            raise LogError(f"Config Error - Extra properties found: {propsExtras}")


    def _configExists(self):
        if not os.path.exists(CONFIG_PATH):
            raise LogError(f"Config Error - File not found \"{CONFIG_PATH}\".")


    def _getEnvFile(self):
        return dotenv_values(CONFIG_PATH)


    def __str__(self):
        buffer = "Configurations:\n"
        for attr in dir(self):
            if not attr.startswith("_") and not callable(getattr(self, attr)):
                buffer += f"{attr}: {getattr(self, attr)}\n"
        return buffer

