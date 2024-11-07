
from enum import Enum
from pydantic import EmailStr

from .account import Account
from .group import Group
from ._entity import Entity
from .organization import Organization
from .ldap_person import LDAPPerson, LDAPManagerPerson

class UserTypeId(Enum):
    """
    The account type identifier.
    """
    Unknown: int = 0
    User: int = 1 # Regular user account.
    Admin: int = 2 # Admin/root user account.
    System: int = 3 # System account. For example, Windows computer accounts with a trailing dollar sign ($).
    Other: int = 99

class User(Entity):
    """
    The User object describes the characteristics of a user/person or a security
    principal
    """

    # Recommended:
    name: str | None = None # The username. For example, `janedoe1`.
    type_id: UserTypeId | None = None # The account type identifier.
    uid: str | None = None # The unique user identifier. For example, the Windows user SID,
                           # ActiveDirectory DN or AWS user ARN.

    # Optional:
    account: Account | None = None # The user's account or the account associated with the user.
    credential_uid: str | None = None
    domain: str | None = None # The domain where the user is defined. For example: the LDAP or Active
                              # Directory domain.
    email_addr: EmailStr | None = None
    full_name: str | None = None
    groups: list[Group] | None = None # The administrative groups to which the user belongs.
    ldap_person: LDAPPerson | None = None # The additional LDAP attributes that describe a person.
    org: Organization | None = None # Organization and org unit related to the user.
    risk_level: str | None = None
    risk_level_id: int | None = None
    risk_score: int | None = None
    type: str | None = None # The type of the user. For example, System, AWS IAM User, etc.
    uid_alt: str | None = None # The alternate user identifier. For example, the Active Directory user
                               # GUID or AWS user Principal ID.

class ManagerUser(User):
    ldap_person: LDAPManagerPerson
