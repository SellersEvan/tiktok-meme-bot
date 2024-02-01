#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: index.py
#   project: TikTok Meme Bot
#   purpose: Dajavu - Prevent Duplicated Generation
#
#


from ctypes import Array
import datetime
import json
from typing import Mapping
from src.utility.error import LogError
from src.static import DAJAVU_PATH


class Dajavu():


    @staticmethod
    def Add(properties:Mapping[str, str]):
        if Dajavu.Contains(properties):
            raise LogError("Duplicated asset being created...")
        entries   = Dajavu._getFile()
        timestamp = str(datetime.datetime.now())
        properties["timestamp"] = timestamp
        entries.append(properties)
        with open(DAJAVU_PATH, "w") as file:
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
            with open(DAJAVU_PATH, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


# Whoever walks in integrity walks securely, but whoever takes crooked paths
# will be found out.
# - Proverbs 10:9
