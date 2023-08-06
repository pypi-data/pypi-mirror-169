from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RefWellboreRig:
    """A reference to a rig within a wellbore.

    The wellbore may be defined within the context of another well. This
    value represents a foreign key from one node to another.

    :ivar rig_reference: A pointer to the rig with which there is a
        relationship.
    :ivar wellbore_parent: A pointer to the wellbore that contains the
        rigReference. This is not needed unless the referenced rig is
        outside the context of a common parent wellbore.
    :ivar well_parent: A pointer to the well that contains the
        wellboreParent. This is not needed unless the referenced
        wellbore is outside the context of a common parent well.
    """
    rig_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "RigReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    wellbore_parent: Optional[str] = field(
        default=None,
        metadata={
            "name": "WellboreParent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
