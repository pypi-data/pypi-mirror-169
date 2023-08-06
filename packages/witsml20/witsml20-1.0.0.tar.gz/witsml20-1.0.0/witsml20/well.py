from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.abstract_well_location import AbstractWellLocation
from witsml20.dimensionless_measure import DimensionlessMeasure
from witsml20.geodetic_well_location import GeodeticWellLocation
from witsml20.length_measure import LengthMeasure
from witsml20.public_land_survey_system import PublicLandSurveySystem
from witsml20.reference_point import ReferencePoint
from witsml20.well_datum import WellDatum
from witsml20.well_direction import WellDirection
from witsml20.well_elevation_coord import WellElevationCoord
from witsml20.well_fluid import WellFluid
from witsml20.well_purpose import WellPurpose
from witsml20.well_status import WellStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Well(AbstractObject):
    """Used to capture the general information about a well.

    Sometimes  called a "well header". Contains all information that is
    the same for all wellbores (sidetracks).

    :ivar name_legal: Legal name of the well.
    :ivar num_license: License number of the well.
    :ivar num_govt: Government assigned well number.
    :ivar dtim_license: Date and time the license  was issued.
    :ivar field_value: Name of the field in which the well is located.
    :ivar country: Country in which the well is located.
    :ivar state: State or province in which the well is located.
    :ivar county: County in which the well is located.
    :ivar region: Geo-political region in which the well is located.
    :ivar district: Geo-political district name.
    :ivar block: Block name in which the  well is located.
    :ivar time_zone: The time zone in which the well is located. It is
        the deviation in hours and minutes from UTC. This should be the
        normal time zone at the well and not a seasonally-adjusted
        value, such as daylight savings time.
    :ivar operator: Operator company name.
    :ivar operator_div: Division of the operator company.
    :ivar original_operator: Original operator of the well. This may be
        different than the current operator.
    :ivar pc_interest: Interest for operator. Commonly in percent.
    :ivar num_api: American Petroleum Institute well number.
    :ivar status_well: POSC well status.
    :ivar purpose_well: POSC well purpose.
    :ivar fluid_well: POSC well fluid. The type of fluid being produced
        from or injected into a well facility.
    :ivar direction_well: POSC well direction. The direction of the flow
        of the fluids in a well facility (generally, injected or
        produced, or some combination).
    :ivar dtim_spud: Date and time at which the well was spudded.
    :ivar dtim_pa: Date and time at which the well was plugged and
        abandoned.
    :ivar water_depth: Depth of water (not land rigs).
    :ivar geographic_location_wgs84: The latitude (in coordinate1) and
        longitude (in coordinate2) of the well location in the WGS84
        coordinate system (equivalent to EPSG:4326). Units are in
        decimal degrees. Coordinate 1 and 2 refer to the
        ProjectedWellLocation.
    :ivar well_location:
    :ivar well_public_land_survey_system_location:
    :ivar reference_point:
    :ivar wellhead_elevation:
    :ivar well_datum:
    :ivar ground_elevation:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    name_legal: Optional[str] = field(
        default=None,
        metadata={
            "name": "NameLegal",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_license: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumLicense",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_govt: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumGovt",
            "type": "Element",
            "max_length": 64,
        }
    )
    dtim_license: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimLicense",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    field_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Field",
            "type": "Element",
            "max_length": 64,
        }
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "max_length": 64,
        }
    )
    state: Optional[str] = field(
        default=None,
        metadata={
            "name": "State",
            "type": "Element",
            "max_length": 64,
        }
    )
    county: Optional[str] = field(
        default=None,
        metadata={
            "name": "County",
            "type": "Element",
            "max_length": 64,
        }
    )
    region: Optional[str] = field(
        default=None,
        metadata={
            "name": "Region",
            "type": "Element",
            "max_length": 64,
        }
    )
    district: Optional[str] = field(
        default=None,
        metadata={
            "name": "District",
            "type": "Element",
            "max_length": 64,
        }
    )
    block: Optional[str] = field(
        default=None,
        metadata={
            "name": "Block",
            "type": "Element",
            "max_length": 64,
        }
    )
    time_zone: Optional[str] = field(
        default=None,
        metadata={
            "name": "TimeZone",
            "type": "Element",
            "max_length": 64,
            "pattern": r"[Z]|([\-+](([01][0-9])|(2[0-3])):[0-5][0-9])",
        }
    )
    operator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "max_length": 64,
        }
    )
    operator_div: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperatorDiv",
            "type": "Element",
            "max_length": 64,
        }
    )
    original_operator: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginalOperator",
            "type": "Element",
            "max_length": 64,
        }
    )
    pc_interest: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "PcInterest",
            "type": "Element",
        }
    )
    num_api: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumAPI",
            "type": "Element",
            "max_length": 64,
        }
    )
    status_well: Optional[WellStatus] = field(
        default=None,
        metadata={
            "name": "StatusWell",
            "type": "Element",
        }
    )
    purpose_well: Optional[WellPurpose] = field(
        default=None,
        metadata={
            "name": "PurposeWell",
            "type": "Element",
        }
    )
    fluid_well: Optional[WellFluid] = field(
        default=None,
        metadata={
            "name": "FluidWell",
            "type": "Element",
        }
    )
    direction_well: Optional[WellDirection] = field(
        default=None,
        metadata={
            "name": "DirectionWell",
            "type": "Element",
        }
    )
    dtim_spud: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimSpud",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pa: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPa",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    water_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "WaterDepth",
            "type": "Element",
        }
    )
    geographic_location_wgs84: Optional[GeodeticWellLocation] = field(
        default=None,
        metadata={
            "name": "GeographicLocationWGS84",
            "type": "Element",
        }
    )
    well_location: List[AbstractWellLocation] = field(
        default_factory=list,
        metadata={
            "name": "WellLocation",
            "type": "Element",
        }
    )
    well_public_land_survey_system_location: Optional[PublicLandSurveySystem] = field(
        default=None,
        metadata={
            "name": "WellPublicLandSurveySystemLocation",
            "type": "Element",
        }
    )
    reference_point: List[ReferencePoint] = field(
        default_factory=list,
        metadata={
            "name": "ReferencePoint",
            "type": "Element",
        }
    )
    wellhead_elevation: Optional[WellElevationCoord] = field(
        default=None,
        metadata={
            "name": "WellheadElevation",
            "type": "Element",
        }
    )
    well_datum: List[WellDatum] = field(
        default_factory=list,
        metadata={
            "name": "WellDatum",
            "type": "Element",
        }
    )
    ground_elevation: Optional[WellElevationCoord] = field(
        default=None,
        metadata={
            "name": "GroundElevation",
            "type": "Element",
        }
    )
