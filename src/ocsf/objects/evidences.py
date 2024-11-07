from pydantic import BaseModel, field_serializer

from .network_endpoint import NetworkEndpoint
from .process import Process
from .file import File
from .database import Database
from .container import Container
from .dns_query import DNSQuery
from .network_connection_info import NetworkConnectionInformation
from .api import API
from .actor import Actor
from .databucket import Databucket
from ..util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE


class EvidenceArtifacts(BaseModel):
    """
    A collection of evidence artifacts associated to the activity/activities that
    triggered a security detection.
    """

    # Recommended:
    actor: Actor | None = None # Describes details about the user/role/process that was the source of
                               # the activity that triggered the detection.
    api: API | None = None # Describes details about the API call associated to the activity that
                           # triggered the detection.
    container: Container | None = None # Describes details about the container associated to the
                                       # activity that triggered the detection.
    connection_info: NetworkConnectionInformation | None = None # Describes details about the network
                                                         # connection associated to the activity that
                                                         # triggered the detection.
    database: Database | None = None # Describes details about the database associated to the activity
                                     # that triggered the detection.
    databucket: Databucket | None = None # Describes details about the databucket associated to the
                                         # activity that triggered the detection.
    dst_endpoint: NetworkEndpoint | None = None # Describes details about the destination of the
                                                # network activity that triggered the detection.
    file: File | None = None # Describes details about the file associated to the activity that
                             # triggered the detection.
    process: Process | None = None # Describes details about the process associated to the activity
                                   # that triggered the detection.
    query: DNSQuery | None = None # Describes details about the DNS query associated to the activity
                                  # that triggered the detection.
    src_endpoint: NetworkEndpoint | None = None # Describes details about the source of the network
                                                # activity that triggered the detection.

    # Optional:
    data: dict | None = None # Additional evidence data that is not accounted for in the specific
                             # evidence attributes.` Use only when absolutely necessary.`

    @field_serializer("data", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def data_serializer(self, value: object):
        return jsonable_object_serializer(value)
