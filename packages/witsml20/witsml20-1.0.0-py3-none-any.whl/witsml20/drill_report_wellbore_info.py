from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDate
from witsml20.object_alias import ObjectAlias

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportWellboreInfo:
    """
    General information about a wellbore for a drill report period.

    :ivar dtim_spud: Date and time at which the well was spudded. This
        is when the well drilling equipment began to bore into the
        earth's surface for the purpose of drilling a well.
    :ivar dtim_pre_spud: Date and time at which the well was predrilled.
        This is when the well drilling equipment begin to bore into the
        earth's surface for the purpose of drilling a well.
    :ivar date_drill_complete: The date when the drilling activity was
        completed.
    :ivar operator: The name of the drilling Operator company
        responsible for the well being drilled (the company for whom the
        well is being drilled).
    :ivar drill_contractor: The name of the drilling contractor company.
    :ivar rig_alias:
    """
    dtim_spud: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimSpud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pre_spud: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPreSpud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    date_drill_complete: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateDrillComplete",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    drill_contractor: Optional[str] = field(
        default=None,
        metadata={
            "name": "DrillContractor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    rig_alias: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "RigAlias",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
