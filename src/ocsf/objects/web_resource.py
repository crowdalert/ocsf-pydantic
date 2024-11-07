from pydantic import AnyUrl, field_serializer
from ._resource import Resource
from ..util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE

class WebResource(Resource):
    """
    The Web Resource object describes characteristics of a web resource that was
    affected by the activity/event.
    """

    # Recommended:
    url_string: AnyUrl | None = None # The URL pointing towards the source of the web resource.

    # Optional:
    data: dict | None = None # Details of the web resource, e.g, `file` details,
                             # `search` results or application-defined resource.
    desc: str | None = None # Description of the web resource.
    name: str | None = None # The name of the web resource.
    type: str | None = None # The web resource type as defined by the event source.
    uid: str | None = None # The unique identifier of the web resource.

    @field_serializer("data", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def data_serializer(self, value: object):
        return jsonable_object_serializer(value)
