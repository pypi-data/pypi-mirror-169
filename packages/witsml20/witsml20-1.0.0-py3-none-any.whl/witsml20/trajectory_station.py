from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_well_location import AbstractWellLocation
from witsml20.angle_per_length_measure import AnglePerLengthMeasure
from witsml20.data_object_reference import DataObjectReference
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.length_measure import LengthMeasure
from witsml20.linear_acceleration_measure import LinearAccelerationMeasure
from witsml20.magnetic_flux_density_measure import MagneticFluxDensityMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.ref_wellbore_trajectory_station import RefWellboreTrajectoryStation
from witsml20.stn_traj_cor_used import StnTrajCorUsed
from witsml20.stn_traj_matrix_cov import StnTrajMatrixCov
from witsml20.stn_traj_raw_data import StnTrajRawData
from witsml20.stn_traj_valid import StnTrajValid
from witsml20.traj_station_status import TrajStationStatus
from witsml20.traj_station_type import TrajStationType
from witsml20.traj_stn_calc_algorithm import TrajStnCalcAlgorithm
from witsml20.type_survey_tool import TypeSurveyTool
from witsml20.well_vertical_depth_coord import WellVerticalDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class TrajectoryStation:
    """WITSML - Trajectory Station Component Schema

    :ivar manually_entered: Indicates whether the trajectory station
        information was manually entered by a human.
    :ivar target: A pointer to the intended target of this station.
    :ivar dtim_stn: Date and time the station was measured or created.
    :ivar type_traj_station: Type of survey station.
    :ivar type_survey_tool: The type of tool used for the measurements.
    :ivar calc_algorithm: The type of algorithm used in the position
        calculation.
    :ivar md: Measured depth of measurement from the drill datum. This
        is an API "node-index" query parameter for growing objects. See
        the relevant API specification for the query behavior related to
        this element.
    :ivar tvd: Vertical depth of the measurements.
    :ivar incl: Hole inclination, measured from vertical.
    :ivar azi: Hole azimuth. Corrected to wells azimuth reference.
    :ivar mtf: Toolface angle (magnetic).
    :ivar gtf: Toolface angle (gravity).
    :ivar disp_ns: North-south offset, positive to the North. This is
        relative to wellLocation with a North axis orientation of
        aziRef. If a displacement with respect to a different point is
        desired then define a localCRS and specify local coordinates in
        location.
    :ivar disp_ew: East-west offset, positive to the East. This is
        relative to wellLocation with a North axis orientation of
        aziRef. If a displacement with respect to a different point is
        desired then define a localCRS and specify local coordinates in
        location.
    :ivar vert_sect: Distance along vertical section azimuth plane.
    :ivar dls: Dogleg severity.
    :ivar rate_turn: Turn rate, radius of curvature computation.
    :ivar rate_build: Build Rate, radius of curvature computation.
    :ivar md_delta: Delta measured depth from previous station.
    :ivar tvd_delta: Delta true vertical depth from previous station.
    :ivar grav_total_uncert: Survey tool gravity uncertainty.
    :ivar dip_angle_uncert: Survey tool dip uncertainty.
    :ivar mag_total_uncert: Survey tool magnetic uncertainty.
    :ivar grav_accel_cor_used: Was an accelerometer alignment correction
        applied to survey computation? Values are "true" (or "1") and
        "false" (or "0").
    :ivar mag_xaxial_cor_used: Was a magnetometer alignment correction
        applied to survey computation? Values are "true" (or "1") and
        "false" (or "0").
    :ivar sag_cor_used: Was a bottom hole assembly sag correction
        applied to the survey computation? Values are "true" (or "1")
        and "false" (or "0").
    :ivar mag_drlstr_cor_used: Was a drillstring magnetism correction
        applied to survey computation? Values are "true" (or "1") and
        "false" (or "0").
    :ivar infield_ref_cor_used: Was an In Field Referencing (IFR)
        correction applied to the azimuth value? Values are "true" (or
        "1") and "false" (or "0"). An IFR survey measures the strength
        and direction of the Earth's magnetic field over the area of
        interest. By taking a geomagnetic modelled values away from
        these field survey results, we are left with a local crustal
        correction, which since it is assumed geological in nature, only
        varies over geological timescales. For MWD survey operations,
        these corrections are applied in addition to the geomagnetic
        model to provide accurate knowledge of the local magnetic field
        and hence to improve the accuracy of MWD magnetic azimuth
        measurements.
    :ivar interpolated_infield_ref_cor_used: Was an Interpolated In
        Field Referencing (IIFR) correction applied to the azimuth
        value? Values are "true" (or "1") and "false" (or "0").
        Interpolated In Field Referencing measures the diurnal Earth
        magnetic field variations resulting from electrical currents in
        the ionosphere and effects of magnetic storms hitting the Earth.
        It increases again the accuracy of the magnetic azimuth
        measurement.
    :ivar in_hole_ref_cor_used: Was an In Hole Referencing (IHR)
        correction applied to the inclination and/or azimuth values?
        Values are "true" (or "1") and "false" (or "0"). In-Hole
        Referencing essentially involves comparing gyro surveys to MWD
        surveys in a tangent section of a well. Once a small part of a
        tangent section has been drilled and surveyed using an MWD tool,
        then an open hole (OH) gyro is run. By comparing the Gyro
        surveys to the MWD surveys a correction can be calculated for
        the MWD. This correction is then assumed as valid for the rest
        of the tangent section allowing to have a near gyro accuracy for
        the whole section, therefore reducing the ellipse of uncertainty
        (EOU) size.
    :ivar axial_mag_interference_cor_used: Was an Axial Magnetic
        Interference (AMI) correction applied to the azimuth value?
        Values are "true" (or "1") and "false" (or "0"). Most of the
        BHAs used to drill wells include an MWD tool. An MWD is a
        magnetic survey tool and as such suffer from magnetic
        interferences from a wide variety of sources. Magnetic
        interferences can be categorized into axial and radial type
        interferences. Axial interferences are mainly the result of
        magnetic poles from the drill string steel components located
        below and above the MWD tool. Radial interferences are numerous.
        Therefore, there is a risk that magXAxialCorUsed includes both
        Axial and radial corrections.
    :ivar cosag_cor_used: WWas a Cosag Correction applied to the azimuth
        values? Values are "true" (or "1") and "false" (or "0"). The BHA
        Sag Correction is the same as the Sag Correction except it
        includes the horizontal misalignment (Cosag).
    :ivar msacor_used: Was a correction applied to the survey due to a
        Multi-Station Analysis process? Values are "true" (or "1") and
        "false" (or "0").
    :ivar grav_total_field_reference: Gravitational field
        theoretical/reference value.
    :ivar mag_total_field_reference: Geomagnetic field
        theoretical/reference value.
    :ivar mag_dip_angle_reference: Magnetic dip angle
        theoretical/reference value.
    :ivar mag_model_used: Geomagnetic model used.
    :ivar mag_model_valid: Current valid interval for the geomagnetic
        model used.
    :ivar geo_model_used: Gravitational model used.
    :ivar status_traj_station: Status of the station.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar valid:
    :ivar matrix_cov:
    :ivar location:
    :ivar source_station:
    :ivar raw_data:
    :ivar cor_used:
    :ivar iscwsa_tool_error_model:
    :ivar uid: A unique identifier for an instance of a trajectory
        station.
    """
    manually_entered: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ManuallyEntered",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    target: Optional[str] = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    dtim_stn: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    type_traj_station: Optional[TrajStationType] = field(
        default=None,
        metadata={
            "name": "TypeTrajStation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    type_survey_tool: Optional[TypeSurveyTool] = field(
        default=None,
        metadata={
            "name": "TypeSurveyTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    calc_algorithm: Optional[TrajStnCalcAlgorithm] = field(
        default=None,
        metadata={
            "name": "CalcAlgorithm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
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
    incl: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Incl",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    azi: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Azi",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mtf: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Mtf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gtf: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "Gtf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    disp_ns: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispNs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    disp_ew: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispEw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vert_sect: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "VertSect",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dls: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "Dls",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rate_turn: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "RateTurn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rate_build: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "RateBuild",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_delta: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MdDelta",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tvd_delta: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "TvdDelta",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_total_uncert: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTotalUncert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dip_angle_uncert: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "DipAngleUncert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_total_uncert: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTotalUncert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_accel_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GravAccelCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_xaxial_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MagXAxialCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    sag_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SagCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_drlstr_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MagDrlstrCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    infield_ref_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InfieldRefCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    interpolated_infield_ref_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterpolatedInfieldRefCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    in_hole_ref_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InHoleRefCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    axial_mag_interference_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AxialMagInterferenceCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cosag_cor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CosagCorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    msacor_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MSACorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    grav_total_field_reference: Optional[LinearAccelerationMeasure] = field(
        default=None,
        metadata={
            "name": "GravTotalFieldReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_total_field_reference: Optional[MagneticFluxDensityMeasure] = field(
        default=None,
        metadata={
            "name": "MagTotalFieldReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_dip_angle_reference: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MagDipAngleReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mag_model_used: Optional[str] = field(
        default=None,
        metadata={
            "name": "MagModelUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    mag_model_valid: Optional[str] = field(
        default=None,
        metadata={
            "name": "MagModelValid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    geo_model_used: Optional[str] = field(
        default=None,
        metadata={
            "name": "GeoModelUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    status_traj_station: Optional[TrajStationStatus] = field(
        default=None,
        metadata={
            "name": "StatusTrajStation",
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
    valid: Optional[StnTrajValid] = field(
        default=None,
        metadata={
            "name": "Valid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    matrix_cov: Optional[StnTrajMatrixCov] = field(
        default=None,
        metadata={
            "name": "MatrixCov",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    location: List[AbstractWellLocation] = field(
        default_factory=list,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    source_station: Optional[RefWellboreTrajectoryStation] = field(
        default=None,
        metadata={
            "name": "SourceStation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    raw_data: Optional[StnTrajRawData] = field(
        default=None,
        metadata={
            "name": "RawData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    cor_used: Optional[StnTrajCorUsed] = field(
        default=None,
        metadata={
            "name": "CorUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    iscwsa_tool_error_model: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IscwsaToolErrorModel",
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
