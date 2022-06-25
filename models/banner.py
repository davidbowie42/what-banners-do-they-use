from enum import Enum


class Banner(Enum):
    FORBIDDEN = -3
    NOT_FOUND = -2
    TIMEOUT = -1
    UNKNOWN = 0
    COOKIEBOT = 1
    CLICKSKEKS = 2
