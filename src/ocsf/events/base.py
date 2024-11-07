from datetime import datetime
from enum import Enum

from pydantic import BaseModel, computed_field, field_serializer

from ocsf.objects.api import API
from ocsf.objects.cloud import Cloud
from ocsf.objects.enrichment import Enrichment
from ocsf.objects.metadata import Metadata
from ocsf.objects.observable import Observable
from ocsf.util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE


class SeverityID(Enum):
    Unknown: int = 0
    Informational: int = 1
    Low: int = 2
    Medium: int = 3
    High: int = 4
    Critical: int = 5
    Fatal: int = 6
    Other: int = 99

class StatusID(Enum):
    Unknown: int = 0
    Success: int = 1
    Failure: int = 2
    Other: int = 99

class CategoryId(Enum):
    Unknown: int = 0
    System_Activity: int = 1
    Findings: int = 2
    Identity_Access_Management: int = 3
    Network_Activity: int = 4
    Discovery: int = 5
    Application_Activity: int = 6

class ActivityId(Enum):
    Unknown: int = 0
    Other: int = 99

class BaseEvent(BaseModel):

    metadata: Metadata

    category_uid: CategoryId = CategoryId.Unknown

    class_uid: int = 0
    class_name: str = 'Base Event'

    activity_id: ActivityId = ActivityId.Unknown
    activity_name: str | None = None

    severity_id: SeverityID = SeverityID.Unknown
    severity: str | None = None

    count: int | None = None

    time: int
    timezone_offset: int | None = None

    start_time: int | None = None
    end_time: int | None = None
    duration: int | None = None

    status_code: str | None = None
    status_detail: str | None = None
    status_id: StatusID = StatusID.Unknown
    status: str | None = None

    cloud: Cloud | None = None
    api: API | None = None

    observables: list[Observable] | None = None
    enrichments: list[Enrichment] | None = None

    message: str | None = None
    raw_data: str | None = None
    unmapped: object | None = None

    @computed_field
    @property
    def category_name(self) -> str:
        return self.category_uid.name.replace('_', ' ')

    @computed_field
    @property
    def type_uid(self) -> int:
        return self.class_uid * 100 + self.activity_id.value

    @computed_field
    @property
    def type_name(self) -> str:
        return f'{self.class_name}: {self.activity_name}'

    @field_serializer("unmapped", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def unmapped_serializer(self, value: object):
        return jsonable_object_serializer(value)
