from enum import Enum


class RegexEnum(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,24}$',
        [
            'First letter uppercase min 2 max 25 characters',
        ]
    )

    MODEL = (
        r'^[A-Z][a-zA-Z\d]{1,24}$',
        'First letter uppercase min 2 max 20 characters'
    )

    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=(?:.*[`~!@#$%^&*()\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]){2,'
        r'})[a-zA-Z\d`~!@#$%^&*()\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]{8,30}$',
        [
            'min 1 lowercase ch',
            'min 1 uppercase ch',
            'min 1 digit',
            'min 1 special character',
            'length 8-30'
        ]
    )

    NAME = (
        r'^[A-Z][a-zA-Z]{1,19}$',
        'First letter uppercase min 2, max 20',
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
