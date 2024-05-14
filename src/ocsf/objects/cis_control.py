from pydantic import BaseModel

class CISControl(BaseModel):
    """
    The CIS Control (aka Critical Security Control) object describes a prioritized
    set of actions to protect your organization and data from cyber-attack vectors.
    The <a target='_blank' href='https://www.cisecurity.org/controls'>CIS
    Controls</a> are defined by the Center for Internet Security.
    """

    name: str # The CIS Control name. For example: <i>4.8 Uninstall or Disable
              # Unnecessary Services on Enterprise Assets and Software.</i>

    # Recommended:
    version: str | None = None # The CIS Control version. For example: <i>v8</i>.

    # Optional:
    desc: str | None = None # The CIS Control description. For example: <i>Uninstall or disable
                            # unnecessary services on enterprise assets and software, such as an unused
                            # file sharing service, web application module, or service function.</i>
