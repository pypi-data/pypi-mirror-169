import re
from typing import Any, Type
from rest_framework import generics
from rest_framework.serializers import Serializer
from .exceptions import InvalidAPIVersion


class GenericAPIView(generics.GenericAPIView):
    """
    Extends GenericAPIView to add support for resolving serializer class based on the requested API version.
    """

    VERSION_FORMAT = re.compile("\d+\.\d+")

    def get_serializer_class(self, *args: Any, **kwargs: Any) -> Type[Serializer]:
        assert (
            self.serializer_class is not None
        ), "serializer_class attribute is required to support version-less requests."
        version_attribute = "serializer_class_v{}".format(self.get_formatted_version())
        return getattr(self, version_attribute, self.serializer_class)

    def invalid_api_version(self) -> None:
        raise InvalidAPIVersion()

    def get_formatted_version(self) -> str:
        if self.request.version is None:
            raise InvalidAPIVersion()

        if self.VERSION_FORMAT.match(self.request.version) is None:
            raise InvalidAPIVersion()

        return self.request.version.replace(".", "_")
