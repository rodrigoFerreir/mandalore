from enum import IntEnum

class StatusPayment(IntEnum):
    PENDING = 1
    COMPLETE = 2
    CANCELED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]