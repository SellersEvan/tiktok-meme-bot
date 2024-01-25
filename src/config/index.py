

class Config:

    def __init__(self):
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
        self.REDDIT_CLIENT_ID   = "..."
        self.REDDIT_SECRET      = "..."
        self.REDDIT_USERNAME    = "..."
        self.REDDIT_PASSWORD    = "..."
        self.REDDIT_USER_AGENT  = "..."

        self.INSTAGRAM_USERNAME = "..."
        self.INSTAGRAM_PASSWORD = "..."

