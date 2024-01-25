

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

    # you may move or create new object to store the default values below
    # just ensure all the values are loaded from the file when __init__ is done
    # make all private functions begin with underscore
    # keep code clean as possible, flexible, and functions no more than 5-6 lines per
    def __init__(self):
        self.CLIP_LENGTH_MIN:int = 20
        self.CLIP_LENGTH_MAX:int = 60
        self.SCREEN_RATIO:float  = 9 / 16
        self.IMAGE_PADDING:int   = 15

