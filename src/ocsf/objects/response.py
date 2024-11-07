from pydantic import BaseModel, field_serializer

from .container import Container
from ..util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE


class ResponseElements(BaseModel):
    """
    The Response Elements object describes characteristics of an API response.
    """

    # Recommended:
    code: int | None = None
    error: str | None = None
    error_message: str | None = None
    message: str | None = None

    # Optional:
    containers: list[Container] | None = None
    data: dict | None = None # The additional data that is associated with the api response.
    flags: list[str] | None = None

    @field_serializer("data", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def data_serializer(self, value: object):
        return jsonable_object_serializer(value)
