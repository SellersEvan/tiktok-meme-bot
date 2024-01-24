from ctypes import Array
import datetime
import json
from typing import Mapping


DAJAVU_FILE = "dejavu.json"


class Dajavu():


    @staticmethod
    def Add(properties:Mapping[str, str]):
        entries   = Dajavu._getFile()
        timestamp = datetime.now(datetime.timezone.utc).isoformat()
        properties["timestamp"] = timestamp
        entries.append(properties)
        with open(DAJAVU_FILE, "w") as file:
            json.dump(entries, file, indent=2)


    @staticmethod
    def Contains(properties:Mapping[str, str]) -> type[Mapping[str, str] | None]:
        for entry in Dajavu._getFile():
            for key in properties:
                if key == "timestamp":
                    continue
                if key not in entry:
                    continue
                if entry[key] == properties[key]:
                    return entry
        return None


    @staticmethod
    def _getFile() -> Array[Mapping[str, str]] :
        try:
            with open(DAJAVU_FILE, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

