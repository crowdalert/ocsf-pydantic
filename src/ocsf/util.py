import os
import json

OCSF_PYDANTIC_SERIALIZE_VARIABLE_JSON_TO_STR = os.getenv(
    "OCSF_PYDANTIC_SERIALIZE_VARIABLE_JSON_TO_STR", "False"
).lower() in ("true", "1", "t")

SERIALIZE_VARIABLE_JSON_RETURN_TYPE = object
if OCSF_PYDANTIC_SERIALIZE_VARIABLE_JSON_TO_STR:
    SERIALIZE_VARIABLE_JSON_RETURN_TYPE = str

def jsonable_object_serializer(value: object) -> object:
    """
    Serialize a JSON-able field that contains a type of `object` to `str` by dumping as JSON.

    For fields that contain a type of 'object' a reasonable schema for conversion to AWS Glue column
    type definitions cannot be provided by Pydantic, which when providing a JSON schema will use an
    entry of type "object" but with no "properties" key, which if we convert to Glue schema, will
    type as `struct<>` which is not valid.

    The workaround is to use a string typed column, and store as a string, and then parse and query
    the JSON in the query engine you use, such as the AWS Athena support for querying JSON data.

    References:
    - https://docs.aws.amazon.com/athena/latest/ug/querying-JSON.html
    - https://repost.aws/questions/QU0CQ6q_tkSwGCd_vQ36M0TA/best-glue-catalog-table-column-type-to-store-variable-json-docs
    """
    if OCSF_PYDANTIC_SERIALIZE_VARIABLE_JSON_TO_STR:
        return json.dumps(value)
    else:
        return value
