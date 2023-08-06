from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class AuthorizationStatus(Enum):
    """
    Specifies the status of the current tool error model.

    :cvar DRAFT: Not yet approved.
    :cvar AUTHORIZED: Approved for use.
    :cvar SUPERSEDED: Obsolete; a newer version is available.
    :cvar WITHDRAWN: No longer approved in this or any other version.
    """
    DRAFT = "draft"
    AUTHORIZED = "authorized"
    SUPERSEDED = "superseded"
    WITHDRAWN = "withdrawn"
