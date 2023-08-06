from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.citation import Citation
from witsml20.data_object_reference import DataObjectReference
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.hole_casing_type import HoleCasingType
from witsml20.length_measure import LengthMeasure
from witsml20.mass_per_length_measure import MassPerLengthMeasure
from witsml20.md_interval import MdInterval
from witsml20.tvd_interval import TvdInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellboreGeometrySection:
    """Wellbore Geometry Component Schema.

    Defines the "fixed" components in a wellbore. It does not define the
    "transient" drilling strings or the "hanging" production components.

    :ivar citation: An ISO 19115 EIP-derived set of metadata attached to
        ensure the traceability of the WellGeometrySection.
    :ivar type_hole_casing: Type of fixed component.
    :ivar section_md_interval: Measured depth interval for this wellbore
        geometry section.
    :ivar section_tvd_interval: True vertical depth interval for this
        wellbore geometry section.
    :ivar id_section: Inner diameter.
    :ivar od_section: Outer diameter. Only for casings and risers.
    :ivar wt_per_len: Weight per unit length for casing sections.
    :ivar grade: Material grade for the tubular section.
    :ivar curve_conductor: Curved conductor? Values are "true" (or "1")
        and "false" (or "0").
    :ivar dia_drift: The drift diameter is the inside diameter (ID) that
        the pipe manufacturer guarantees per specifications. Note that
        the nominal inside diameter is not the same as the drift
        diameter, but is always slightly larger. The drift diameter is
        used by the well planner to determine what size tools or casing
        strings can later be run through the casing, whereas the nominal
        inside diameter is used for fluid volume calculations, such as
        mud circulating times and cement slurry placement calculations.
        Source: www.glossary.oilfield.slb.com
    :ivar fact_fric: Friction factor.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar bha_run:
    :ivar uid: Unique identifier of this WbGeometrySection within the
        WbGeometry object.
    """
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_hole_casing: Optional[HoleCasingType] = field(
        default=None,
        metadata={
            "name": "TypeHoleCasing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    section_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "SectionMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    section_tvd_interval: Optional[TvdInterval] = field(
        default=None,
        metadata={
            "name": "SectionTvdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    id_section: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "IdSection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    od_section: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OdSection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_per_len: Optional[MassPerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "WtPerLen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grade: Optional[str] = field(
        default=None,
        metadata={
            "name": "Grade",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    curve_conductor: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CurveConductor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_drift: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaDrift",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fact_fric: Optional[float] = field(
        default=None,
        metadata={
            "name": "FactFric",
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
    bha_run: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BhaRun",
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
