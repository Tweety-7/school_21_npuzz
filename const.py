from enum import Enum

EPSILON = 0.000001
OPERATORS = r"\*\/\-\+\^"
DIGITS = "0123456789"
VALID_ARGS = ["--debug", "--vis"]


class Mode:
    DEBUG_MODE = False
    VIS_MODE = False


BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

FONT_FILEPATH = "resources/OpenSans-Regular.ttf"