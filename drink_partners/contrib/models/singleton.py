from typing import Any, Dict


class SingletonMixin:

    _instances: Dict[Any, Any] = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMixin, cls).__new__(cls, *args, **kwargs)  # noqa
        return cls._instances[cls]
