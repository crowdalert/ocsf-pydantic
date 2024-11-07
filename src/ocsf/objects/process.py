from enum import Enum
from datetime import datetime

from pydantic import field_serializer

from ._entity import Entity

from .container import Container
from .user import User
from .file import File
from .session import Session
from ..util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE


class ProcessIntegrityId(Enum):
    Unknown: int = 0
    Untrusted: int = 1
    Low: int = 2
    Medium: int = 3
    High: int = 4
    System: int = 5
    Protected: int = 6
    Other: int = 99

class Process(Entity, Container):
    """
    The Process object describes a running instance of a launched program
    """

    # Recommended:
    cmd_line: str | None = None
    created_time: datetime | None = None # The time when the process was created/started.
    file: File | None = None # The process file object.
    parent_process: 'Process | None' = None
    pid: int | None = None
    user: User | None = None # The user under which this process is running.

    # Optional:
    integrity: str | None = None
    integrity_id: ProcessIntegrityId | None = None
    lineage: list[str] | None = None
    loaded_modules: list[str] | None = None
    name: str | None = None # The friendly name of the process, for example: `Notepad++`.
    sandbox: str | None = None
    session: Session | None = None # The user session under which this process is running.
    terminated_time: datetime | None = None # The time when the process was terminated.
    tid: int | None = None
    uid: str | None = None # A unique identifier for this process assigned by the producer (tool).
                           # Facilitates correlation of a process event with other events for that
                           # process.
    xattributes: object | None = None # An unordered collection of zero or more name/value pairs that
                                      # represent a process extended attribute.

    @field_serializer("xattributes", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def xattributes_serializer(self, value: object):
        return jsonable_object_serializer(value)