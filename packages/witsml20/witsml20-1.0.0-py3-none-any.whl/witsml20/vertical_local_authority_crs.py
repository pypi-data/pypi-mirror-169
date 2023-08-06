from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_vertical_crs import AbstractVerticalCrs
from witsml20.authority_qualified_name import AuthorityQualifiedName

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalLocalAuthorityCrs(AbstractVerticalCrs):
    """This class contains a code for a vertical CRS according to a local
    authority.

    This would be used in a case where a company or regulatory regime
    has chosen not to use EPSG codes.
    """
    local_authority_crs_name: Optional[AuthorityQualifiedName] = field(
        default=None,
        metadata={
            "name": "LocalAuthorityCrsName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
