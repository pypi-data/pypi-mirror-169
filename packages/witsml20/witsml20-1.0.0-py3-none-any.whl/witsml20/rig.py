from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlPeriod
from witsml20.abstract_object import AbstractObject
from witsml20.derrick_type import DerrickType
from witsml20.force_measure import ForceMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.length_per_time_measure import LengthPerTimeMeasure
from witsml20.rig_type import RigType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Rig(AbstractObject):
    """Rig Schema.

    Used to capture information unique to a drilling rig. For
    information about the usage of a rig in a specific operation, see
    the RigUtilization object.

    :ivar owner: The name of the company that owns the rig.
    :ivar type_rig: The type of rig (e.g., semi-submersible, jack-up,
        etc.)
    :ivar manufacturer: The company that manufactured the rig.
    :ivar year_ent_service: The year the rig entered service.
    :ivar class_rig: Classification of the rig.
    :ivar approvals: Rig approvals/certification.
    :ivar registration: Rig registration location.
    :ivar tel_number: Telephone number on the rig.
    :ivar fax_number: Fax number on the rig.
    :ivar email_address: Email address of the contact person.
    :ivar name_contact: Name of the contact person.
    :ivar rating_drill_depth: Maximum hole depth rating for the rig.
    :ivar rating_water_depth: Maximum water depth rating for the rig.
    :ivar is_offshore: Flag to indicate that the rig is an offshore rig
        (drill ship, semi-submersible, jack-up, platform, TADU). Values
        are "true" (or "1") and "false" (or "0").
    :ivar type_derrick: Derrick type.
    :ivar rating_derrick: Derrick rating.
    :ivar ht_derrick: Height of the derrick.
    :ivar cap_wind_derrick: Derrick wind capacity.
    :ivar num_cranes: Number of cranes on the rig.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Element",
            "max_length": 64,
        }
    )
    type_rig: Optional[RigType] = field(
        default=None,
        metadata={
            "name": "TypeRig",
            "type": "Element",
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "max_length": 64,
        }
    )
    year_ent_service: Optional[XmlPeriod] = field(
        default=None,
        metadata={
            "name": "YearEntService",
            "type": "Element",
        }
    )
    class_rig: Optional[str] = field(
        default=None,
        metadata={
            "name": "ClassRig",
            "type": "Element",
            "max_length": 64,
        }
    )
    approvals: Optional[str] = field(
        default=None,
        metadata={
            "name": "Approvals",
            "type": "Element",
            "max_length": 64,
        }
    )
    registration: Optional[str] = field(
        default=None,
        metadata={
            "name": "Registration",
            "type": "Element",
            "max_length": 64,
        }
    )
    tel_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "TelNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    fax_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "FaxNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    email_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "EmailAddress",
            "type": "Element",
            "max_length": 64,
        }
    )
    name_contact: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameContact",
            "type": "Element",
            "max_length": 64,
        }
    )
    rating_drill_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "RatingDrillDepth",
            "type": "Element",
        }
    )
    rating_water_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "RatingWaterDepth",
            "type": "Element",
        }
    )
    is_offshore: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsOffshore",
            "type": "Element",
        }
    )
    type_derrick: Optional[DerrickType] = field(
        default=None,
        metadata={
            "name": "TypeDerrick",
            "type": "Element",
        }
    )
    rating_derrick: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "RatingDerrick",
            "type": "Element",
        }
    )
    ht_derrick: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HtDerrick",
            "type": "Element",
        }
    )
    cap_wind_derrick: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "CapWindDerrick",
            "type": "Element",
        }
    )
    num_cranes: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumCranes",
            "type": "Element",
        }
    )
