from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.md_interval import MdInterval
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportPerfInfo:
    """
    General information about a perforation interval related to the drill
    report period.

    :ivar dtim_open: The date and time at which the well perforation
        interval is opened.
    :ivar dtim_close: The date and time at which the well perforation
        interval is closed.
    :ivar perforation_md_interval: Measured depth interval between the
        top and the base of the perforations.
    :ivar perforation_tvd_interval: True vertical depth interval between
        the top and the base of the perforations.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportPerfInfo.
    """
    dtim_open: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimOpen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_close: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimClose",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    perforation_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    perforation_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "PerforationTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
