from pydantic import BaseModel, field_serializer
from .container import Container
from ..util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE
class RequestElements(BaseModel):
    """
    The Request Elements object describes characteristics of an API request.
    """

    uid: str  # The unique request identifier.

    # Optional:
    containers: list[Container] | None = None
    data: dict = None # The additional data that is associated with the api request.
    flags: list[str] | None = None

    @field_serializer("data", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def data_serializer(self, value: object):
        return jsonable_object_serializer(value)
