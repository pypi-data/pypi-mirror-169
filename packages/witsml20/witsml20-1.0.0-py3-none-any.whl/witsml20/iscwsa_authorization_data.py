from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.authorization_status import AuthorizationStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaAuthorizationData:
    """Authorization state of some entity.

    The main goal of the Industry Steering Committee on Wellbore Survey
    Accuracy (ISCWSA) is to to produce and maintain standards for the
    industry relating to wellbore survey accuracy.

    :ivar author: Person responsible for the information.
    :ivar source: Source from which the information is derived.
    :ivar authority: Person or collective body responsible for
        authorizing the information.
    :ivar status: Authorization state of the information.
    :ivar version: Version name or number.
    :ivar comment: A comment about the object. This should include
        information regarding the derivation of the information.
    """
    author: Optional[str] = field(
        default=None,
        metadata={
            "name": "Author",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    source: Optional[str] = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    status: Optional[AuthorizationStatus] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
