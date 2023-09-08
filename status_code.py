from enum import Enum

class StatusCode(Enum):
    OK: int = 2000
    ERROR: int = 5000
    REQUEST_ERROR: int = 4000
    FILE_NOT_FOUND: int = 4040