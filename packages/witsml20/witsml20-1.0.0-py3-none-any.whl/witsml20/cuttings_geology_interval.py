from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.citation import Citation
from witsml20.custom_data import CustomData
from witsml20.cuttings_interval_lithology import CuttingsIntervalLithology
from witsml20.dimensionless_measure import DimensionlessMeasure
from witsml20.existence_kind import ExistenceKind
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.illuminance_measure import IlluminanceMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.md_interval import MdInterval
from witsml20.object_alias import ObjectAlias
from witsml20.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CuttingsGeologyInterval:
    """
    A depth range along the wellbore containing one or more lithology types and
    information about how the cuttings were sampled.

    :ivar aliases:
    :ivar md_interval: The measured depth interval that is represented
        by the cuttings described in this instance.
    :ivar custom_data:
    :ivar extension_name_value:
    :ivar object_version:
    :ivar schema_version:
    :ivar uuid:
    :ivar existence_kind: A lifecycle state like actual, required,
        planned, predicted, etc. This is used to qualify any top-level
        element (from Epicentre -2.1).
    :ivar citation: An ISO 19115 EIP-derived set of metadata attached to
        ensure the traceability of the CuttingsGeologyInterval.
    :ivar dens_bulk: Sample bulk density for the interval.
    :ivar dens_shale: Shale density for the interval.
    :ivar calcite: Calcimetry calcite percentage.
    :ivar calc_stab: Calcimetry stabilized percentage.
    :ivar cec: Cuttings cationic exchange capacity. Temporarily calling
        this a DimensionlessMeasure.
    :ivar dolomite: Calcimetry dolomite percentage.
    :ivar size_min: Minimum size.
    :ivar size_max: Maximum size.
    :ivar qft: Fluorescence as measured using a device licensed for the
        Quantitative Fluorescence Technique.
    :ivar cleaning_method: Sample treatment: cleaning method.
    :ivar drying_method: Sample treatment: drying method.
    :ivar cuttings_interval_lithology:
    :ivar uid: Unique identifier for this instance of
        CuttingsGeologyInterval.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    aliases: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "Aliases",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
        }
    )
    custom_data: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "CustomData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    object_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectVersion",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    existence_kind: Optional[ExistenceKind] = field(
        default=None,
        metadata={
            "name": "existenceKind",
            "type": "Attribute",
        }
    )
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
        }
    )
    dens_bulk: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensBulk",
            "type": "Element",
        }
    )
    dens_shale: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensShale",
            "type": "Element",
        }
    )
    calcite: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Calcite",
            "type": "Element",
        }
    )
    calc_stab: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CalcStab",
            "type": "Element",
        }
    )
    cec: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Cec",
            "type": "Element",
        }
    )
    dolomite: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Dolomite",
            "type": "Element",
        }
    )
    size_min: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeMin",
            "type": "Element",
        }
    )
    size_max: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeMax",
            "type": "Element",
        }
    )
    qft: Optional[IlluminanceMeasure] = field(
        default=None,
        metadata={
            "name": "Qft",
            "type": "Element",
        }
    )
    cleaning_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "CleaningMethod",
            "type": "Element",
            "max_length": 64,
        }
    )
    drying_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "DryingMethod",
            "type": "Element",
            "max_length": 64,
        }
    )
    cuttings_interval_lithology: List[CuttingsIntervalLithology] = field(
        default_factory=list,
        metadata={
            "name": "CuttingsIntervalLithology",
            "type": "Element",
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
