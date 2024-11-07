from datetime import datetime

from pydantic import BaseModel, EmailStr

from .location import GeoLocation

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User, ManagerUser


class LDAPPerson(BaseModel):
    """
    The additional LDAP attributes that describe a person.
    """

    # Optional:
    cost_center: str | None = None
    created_time: datetime | None = None # The timestamp when the user was created.
    deleted_time: datetime | None = None
    email_addrs: list[EmailStr] | None = None
    employee_uid: str | None = None
    given_name: str | None = None
    hire_time: datetime | None = None
    job_title: str | None = None
    labels: list[str] | None = None # The labels associated with the user. For example in AD this could
                                    # be the `userType`, `employeeType`. For
                                    # example: `Member, Employee`.
    last_login_time: datetime | None = None
    ldap_cn: str | None = None
    ldap_dn: str | None = None
    leave_time: datetime | None = None
    location: GeoLocation | None = None # The geographical location associated with a user. This is
                                        # typically the user's usual work location.
    manager: 'ManagerUser | None' = None
    modified_time: datetime | None = None # The timestamp when the user entry was last modified.
    office_location: str | None = None
    surname: str | None = None

class LDAPManagerPerson(LDAPPerson):
    manager: None = None # LDAPPerson manager's manager should not be populated https://schema.ocsf.io/1.2.0/objects/ldap_person?extensions=
