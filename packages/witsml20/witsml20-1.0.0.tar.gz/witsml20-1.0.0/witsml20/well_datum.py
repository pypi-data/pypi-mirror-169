from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_vertical_crs import AbstractVerticalCrs
from witsml20.abstract_well_location import AbstractWellLocation
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.ref_wellbore import RefWellbore
from witsml20.ref_wellbore_rig import RefWellboreRig
from witsml20.well_elevation_coord import WellElevationCoord
from witsml20.wellbore_datum_reference import WellboreDatumReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class WellDatum:
    """
    Defines the vertical datums associated with elevation, vertical depth and
    measured depth coordinates within the context of a well.

    :ivar name: The human-understandable contextual name of the
        reference datum.
    :ivar code: The code value that represents the type of reference
        datum. This may represent a point on a device (e.g., kelly
        bushing) or it may represent a vertical reference datum (e.g.,
        mean sea level).
    :ivar kind: Because various activities may use different points as
        measurement datums, it is useful to characterize the point based
        on its usage. A well reference datum may have more than one such
        characterization. For example, it may be the datum used by the
        driller and logger for measuring their depths. Example usage
        values would be 'permanent','driller', 'logger' 'WRP' (well
        reference point) and 'SRP' (site reference point).
    :ivar measured_depth: The measured depth coordinate of this
        reference datum as measured from another datum. The measured
        depth datum should either be the same as the elevation datum or
        it should be relatable to the elevation datum through other
        datums. Positive moving toward the bottomhole from the measured
        depth datum. This should be given when a local reference is
        "downhole", such as a kickoff point or ocean bottom template,
        and the borehole may not be vertical. If a depth is given, then
        an elevation should also be given.
    :ivar comment: A contextual description of the well reference datum.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar wellbore:
    :ivar rig:
    :ivar elevation:
    :ivar horizontal_location:
    :ivar crs: Points to one of the optional for a geodetic vertical
        CRS, Allows the datum to be positioned in real-world space.l
    :ivar uid: A unique identifier for an instance of a well datum.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    code: Optional[WellboreDatumReference] = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    kind: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    measured_depth: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MeasuredDepth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
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
    wellbore: Optional[RefWellbore] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rig: Optional[RefWellboreRig] = field(
        default=None,
        metadata={
            "name": "Rig",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    elevation: Optional[WellElevationCoord] = field(
        default=None,
        metadata={
            "name": "Elevation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    horizontal_location: Optional[AbstractWellLocation] = field(
        default=None,
        metadata={
            "name": "HorizontalLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    crs: Optional[AbstractVerticalCrs] = field(
        default=None,
        metadata={
            "name": "Crs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
