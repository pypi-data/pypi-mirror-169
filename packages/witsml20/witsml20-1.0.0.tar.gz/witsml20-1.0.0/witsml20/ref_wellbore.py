from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RefWellbore:
    """Data that represents a foreign key to a wellbore.

    The wellbore may be defined within the context of another well.

    :ivar wellbore_reference: A pointer the wellbore with which there is
        a relationship.
    :ivar well_parent: A pointer to the well that contains the
        wellboreReference. This is not needed unless the referenced
        wellbore is outside the context of a common parent well.
    """
    wellbore_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellboreReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    well_parent: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellParent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
