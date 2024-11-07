from enum import Enum
from datetime import datetime

from pydantic import field_serializer

from .data_classification import DataClassification

from ._entity import Entity

from .user import User
from .product import Product
from .digital_signature import DigitalSignature
from .fingerprint import Fingerprint
from ..util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE

class FileTypeId(Enum):
    """
    The file type ID.
    """
    Unknown: int = 0
    Regular_File: int = 1
    Folder: int = 2
    Character_Device: int = 3
    Block_Device: int = 4
    Local_Socket: int = 5
    Named_Pipe: int = 6
    Symbolic_Link: int = 7
    Other: int = 99

class File(Entity, DataClassification):
    """
    The File object represents the metadata associated with a file stored in a
    computer system. It encompasses information about the file itself, including its
    attributes, properties, and organizational details. Defined by D3FEND <a
    target='_blank'
    href='https://next.d3fend.mitre.org/dao/artifact/d3f:File/'>d3f:File</a>.
    """

    name: str # The name of the file. For example: `svchost.exe`
    type_id: FileTypeId # The file type ID.

    # Recommended:
    ext: str | None = None # The extension of the file, excluding the leading dot. For example:
                           # `exe` from `svchost.exe`, or `gz` from
                           # `export.tar.gz`.
    hashes: list[Fingerprint] | None = None
    path: str | None = None # The full path to the file. For example:
                            # `c:\windows\system32\svchost.exe`.

    # Optional:
    accessed_time: datetime | None = None
    accessor: User | None = None
    attributes: int | None = None
    company_name: str | None = None
    confidentiality: str | None = None
    confidentiality_id: int | None = None
    created_time: datetime | None = None # The time when the file was created.
    creator: User | None = None # The user that created the file.
    desc: str | None = None # The description of the file, as returned by file system. For example: the
                            # description as returned by the Unix file command or the Windows file
                            # type.
    is_system: bool | None = None
    mime_type: str | None = None
    modified_time: datetime | None = None # The time when the file was last modified.
    modifier: User | None = None # The user that last modified the file.
    owner: User | None = None
    parent_folder: str | None = None
    product: Product | None = None # The product that created or installed the file.
    security_descriptor: str | None = None
    signature: DigitalSignature | None = None
    size: int | None = None
    type: str | None = None # The file type.
    uid: str | None = None # The unique identifier of the file as defined by the storage system, such
                           # the file system file ID.
    version: str | None = None # The file version. For example: `8.0.7601.17514`.
    xattributes: object | None = None

    @field_serializer("xattributes", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def xattributes_serializer(self, value: object):
        return jsonable_object_serializer(value)
