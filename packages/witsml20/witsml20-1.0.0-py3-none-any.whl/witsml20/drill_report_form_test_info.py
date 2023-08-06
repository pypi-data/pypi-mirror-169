from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.pressure_measure import PressureMeasure
from witsml20.volume_measure import VolumeMeasure
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DrillReportFormTestInfo:
    """
    General information about a wireline formation test that occurred during
    the drill report period.

    :ivar dtim: Date and time that the wireline formation test was
        completed.
    :ivar md: Measured depth at which the wireline formation test was
        conducted.
    :ivar tvd: True vertical depth at which the wireline formation test
        was conducted.
    :ivar pres_pore: The formation pore pressure. The pressure of fluids
        within the pores of a reservoir, usually hydrostatic pressure,
        or the pressure exerted by a column of water from the
        formation's depth to sea level.
    :ivar good_seal: Was there a good seal for the wireline formation
        test? Values are "true" or "1" or "false" or "0".
    :ivar md_sample: Measured depth where the fluid sample was taken.
    :ivar dominate_component: The dominate component in the fluid
        sample.
    :ivar density_hc: The density of the hydrocarbon component of the
        fluid sample.
    :ivar volume_sample: The volume of the fluid sample.
    :ivar description: A detailed description of the wireline formation
        test.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of
        DrillReportFormTestInfo.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd: Optional[WellVerticalDepthCoord] = field(
        default=None,
        metadata={
            "name": "Tvd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_pore: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresPore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    good_seal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GoodSeal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_sample: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdSample",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dominate_component: Optional[str] = field(
        default=None,
        metadata={
            "name": "DominateComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    density_hc: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityHC",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    volume_sample: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeSample",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
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
