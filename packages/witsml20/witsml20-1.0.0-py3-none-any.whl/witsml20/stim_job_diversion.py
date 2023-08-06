from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.length_measure import LengthMeasure
from witsml20.stim_job_diversion_method import StimJobDiversionMethod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimJobDiversion:
    """
    Captures the high-level description of the diversion method used in the
    stimulation job.

    :ivar contractor: Name of the diversion contractor.
    :ivar method: The diversion method used.
    :ivar tool_description: A supplier description of the diversion
        tool, such as its commercial name.
    :ivar element_spacing: Spacing between packer elements.
    """
    contractor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contractor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    method: Optional[StimJobDiversionMethod] = field(
        default=None,
        metadata={
            "name": "Method",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tool_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ToolDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    element_spacing: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ElementSpacing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
