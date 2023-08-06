import uuid
from typing import Any
from django.db import models
from .validators import validate_number


class StringField(models.CharField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["max_length"] = 150
        super().__init__(*args, **kwargs)


class PrimaryKeyField(models.CharField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["editable"] = False
        kwargs["primary_key"] = True
        kwargs["max_length"] = 40
        kwargs["default"] = uuid.uuid4
        super().__init__(*args, **kwargs)


class PhoneNumberField(models.CharField):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        kwargs["max_length"] = 40
        kwargs["validators"] = [validate_number]
        super().__init__(*args, **kwargs)
