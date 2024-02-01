#
#   Copyright (C) 2024 Sellers Industries, Inc.
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Wed Jan 31 2024
#   file: model.py
#   project: TikTok Meme Bot
#   purpose: ENV File Validation Structure
#
#


"""
[{
    "isRequired": True, # If the group is required
    "primary":  [],     # If one of the primary is present, rest are required
    "optional": []      # Optional properties
}]
"""

CONFIG_STRUCTURE = [{
    "isRequired": True,
    "primary":  ["REDDIT_CLIENT_ID", "REDDIT_SECRET", "REDDIT_USERNAME", "REDDIT_PASSWORD"],
    "optional": []
}]


# This is what the Lord says to Israel: "Seek me and live."
# - Amos 5:4
