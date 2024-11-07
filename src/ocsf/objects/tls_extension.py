from pydantic import BaseModel, field_serializer
from enum import Enum

from ..util import jsonable_object_serializer, SERIALIZE_VARIABLE_JSON_RETURN_TYPE


class TLSExtensionTypeId(Enum):
    """
    The TLS extension type identifier. See <a target='_blank'
    href='https://datatracker.ietf.org/doc/html/rfc8446#page-35'>The Transport Layer
    Security (TLS) extension page</a>.
    """
    Server_name: int = 0 # The Server Name Indication extension.
    Maximum_fragment_length: int = 1 # The Maximum Fragment Length Negotiation extension.
    Status_request: int = 5 # The Certificate Status Request extension.
    Supported_groups: int = 10 # The Supported Groups extension.
    Signature_algorithms: int = 13 # The Signature Algorithms extension.
    Use_srtp: int = 14 # The Use SRTP data protection extension.
    Heartbeat: int = 15 # The Heartbeat extension.
    Application_layer_protocol_negotiation: int = 16 # The Application-Layer Protocol Negotiation extension.
    Signed_certificate_timestamp: int = 18 # The Signed Certificate Timestamp extension.
    Client_certificate_type: int = 19 # The Client Certificate Type extension.
    Server_certificate_type: int = 20 # The Server Certificate Type extension.
    Padding: int = 21 # The Padding extension.
    Pre_shared_key: int = 41 # The Pre Shared Key extension.
    Early_data: int = 42 # The Early Data extension.
    Supported_versions: int = 43 # The Supported Versions extension.
    Cookie: int = 44 # The Cookie extension.
    Psk_key_exchange_modes: int = 45 # The Pre-Shared Key Exchange Modes extension.
    Certificate_authorities: int = 47 # The Certificate Authorities extension.
    Oid_filters: int = 48 # The OID Filters extension.
    Post_handshake_auth: int = 49 # The Post-Handshake Client Authentication extension.
    Signature_algorithms_cert: int = 50 # The Signature Algorithms extension.
    Key_share: int = 51 # The Key Share extension.

class TLSExtension(BaseModel):
    """
    The TLS Extension object describes additional attributes that extend the base
    Transport Layer Security (TLS) object.
    """

    type_id: TLSExtensionTypeId # The TLS extension type identifier
                                # See: https://datatracker.ietf.org/doc/html/rfc8446#page-35

    # Recommended:
    data: dict | None = None # The data contains information specific to the particular extension type.

    # Optional:
    type: str | None = None # The TLS extension type. For example: `Server Name`.

    @field_serializer("data", return_type=SERIALIZE_VARIABLE_JSON_RETURN_TYPE)
    def data_serializer(self, value: object):
        return jsonable_object_serializer(value)
