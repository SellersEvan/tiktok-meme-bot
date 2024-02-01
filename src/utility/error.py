#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Thu Feb 01 2024
#   file: error.py
#   project: TikTok Meme Bot
#   purpose: Error
#
#


class LogError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


# If it is possible, as far as it depends on you, live at peace with everyone.
# - Romans 12:18
