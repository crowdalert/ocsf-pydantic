from datetime import datetime
from pydantic import AnyUrl, BaseModel

from .analytic import Analytic
from .kill_chain_phase import KillChainPhase

from .related_event import RelatedEvent
from .attack import MITREATTCK

class FindingInformation(BaseModel):
    """
    The Finding Information object describes metadata related to a security finding
    generated by a security tool or system.
    """

    title: str # A title or a brief phrase summarizing the reported finding.
    uid: str # The unique identifier of the reported finding.

    # Recommended:
    analytic: Analytic | None = None

    # Optional:
    attacks: list[MITREATTCK] | None = None # The MITRE ATT&CK technique and associated tactics related to the
                                            # finding.
    created_time: datetime | None = None # The time when the finding was created.
    data_sources: list[str] | None = None
    desc: str | None = None # The description of the reported finding.
    first_seen_time: datetime | None = None # The time when the finding was first observed. e.g. The
                                            # time when a vulnerability was first observed. <p>It can
                                            # differ from the `created_time` timestamp,
                                            # which reflects the time this finding was created.</p>
    kill_chain: list[KillChainPhase] | None = None
    last_seen_time: datetime | None = None # The time when the finding was most recently observed. e.g.
                                           # The time when a vulnerability was most recently observed.
                                           # It can differ from the `modified_time` timestamp, which
                                           # reflects the time this finding was last modified.
    modified_time: datetime | None = None # The time when the finding was last modified.
    product_uid: str | None = None # The unique identifier of the product that reported the finding.
    related_events: list[RelatedEvent] | None = None
    related_analytics: list[Analytic] | None = None # Other analytics related to this finding.
    src_url: AnyUrl | None = None # The URL pointing to the source of the finding.
    types: list[str] | None = None # One or more types of the reported finding.
