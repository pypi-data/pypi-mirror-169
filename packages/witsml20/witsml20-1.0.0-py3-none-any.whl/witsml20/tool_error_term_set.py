from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.iscwsa_authorization_data import IscwsaAuthorizationData
from witsml20.iscwsa_error_term import IscwsaErrorTerm
from witsml20.iscwsa_nomenclature import IscwsaNomenclature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ToolErrorTermSet(AbstractObject):
    """Captures a set of surveying tool error terms which may be used in a
    toolErrorModel.

    This object is globally unique.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    authorization: Optional[IscwsaAuthorizationData] = field(
        default=None,
        metadata={
            "name": "Authorization",
            "type": "Element",
        }
    )
    nomenclature: Optional[IscwsaNomenclature] = field(
        default=None,
        metadata={
            "name": "Nomenclature",
            "type": "Element",
        }
    )
    error_term: List[IscwsaErrorTerm] = field(
        default_factory=list,
        metadata={
            "name": "ErrorTerm",
            "type": "Element",
        }
    )
