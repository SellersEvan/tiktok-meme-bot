

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

