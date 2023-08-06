from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TrajStationType(Enum):
    """
    Specifies the type of directional survey station.

    :cvar AZIMUTH_ON_PLANE: Section terminates at a given azimuth on a
        given plane target; requires target ID.
    :cvar BUILDRATE_TO_DELTA_MD: Section follows a given build rate to a
        specified delta measured depth.
    :cvar BUILDRATE_TO_INCL: Section follows a given build rate to a
        specified inclination.
    :cvar BUILDRATE_TO_MD: Section follows a given build rate to a
        specified measured depth.
    :cvar BUILDRATE_AND_TURNRATE_TO_AZI: Section follows a given build
        rate and turn rate to a specified azimuth.
    :cvar BUILDRATE_AND_TURNRATE_TO_DELTA_MD: Section follows a given
        build rate and turn rate to a specified delta measured depth.
    :cvar BUILDRATE_AND_TURNRATE_TO_INCL: Section follows a given build
        rate and turn rate to a specified inclination.
    :cvar BUILDRATE_AND_TURNRATE_TO_INCL_AND_AZI: Section follows a
        given build rate and turn rate to a specified inclination and
        azimuth.
    :cvar BUILDRATE_AND_TURNRATE_TO_MD: Section follows a given build
        rate and turn rate to a specified measured depth.
    :cvar BUILDRATE_AND_TURNRATE_TO_TVD: Section follows a given build
        rate and turn rate to a specified TVD.
    :cvar BUILDRATE_TVD: Section follows a given build rate to a
        specified TVD.
    :cvar CASING_MD: Measured depth casing point; can also be inserted
        within actual survey stations.
    :cvar CASING_TVD: TVD casing point; can also be inserted within
        actual survey stations.
    :cvar DLS: Section follows a given dogleg severity.
    :cvar DLS_TO_AZI_AND_MD: Section follows a given dogleg severity to
        a specified measured depth and azimuth.
    :cvar DLS_TO_AZI_TVD: Section follows a given dogleg severity until
        a specified TVD and azimuth.
    :cvar DLS_TO_INCL: Section follows a given dogleg severity until a
        specified inclination.
    :cvar DLS_TO_INCL_AND_AZI: Section follows a given dogleg severity
        to a specified inclination and azimuth.
    :cvar DLS_TO_INCL_AND_MD: Section follows a given dogleg severity to
        a specified measured depth and inclination.
    :cvar DLS_TO_INCL_AND_TVD: Section follows a given dogleg severity
        until a specified TVD and inclination.
    :cvar DLS_TO_NS: Section follows a given dogleg severity for a given
        north, south distance.
    :cvar DLS_AND_TOOLFACE_TO_AZI: Section follows a given toolface
        angle and  dogleg severity to a specified azimuth.
    :cvar DLS_AND_TOOLFACE_TO_DELTA_MD: Section follows a given toolface
        angle and dogleg severity to a specified delta measured depth.
    :cvar DLS_AND_TOOLFACE_TO_INCL: Section follows a given toolface
        angle and dogleg severity to a specified inclination.
    :cvar DLS_AND_TOOLFACE_TO_INCL_AZI: Section follows a given toolface
        angle and dogleg severity to a specified inclination and
        azimuth.
    :cvar DLS_AND_TOOLFACE_TO_MD: Section follows a given toolface angle
        and dogleg severity to a specified measured depth.
    :cvar DLS_AND_TOOLFACE_TO_TVD: Section follows a given toolface
        angle and dogleg severity to a specified TVD.
    :cvar FORMATION_MD: Measured depth formation; can be inserted within
        actual survey stations also .
    :cvar FORMATION_TVD: TVD formation; can be inserted within actual
        survey stations also.
    :cvar HOLD_TO_DELTA_MD: Section holds angle and azimuth to a
        specified delta measured depth.
    :cvar HOLD_TO_MD: Section holds angle and azimuth to a specified
        measured depth.
    :cvar HOLD_TO_TVD: Section holds angle and azimuth to a specified
        TVD.
    :cvar INCL_AZI_AND_TVD: Section follows a continuous curve to a
        specified inclination, azimuth and true vertical depth.
    :cvar INTERPOLATED: Derived by interpolating between stations with
        entered values (either planned or surveyed).
    :cvar MARKER_MD: Measured depth marker; can be inserted within
        actual survey stations also.
    :cvar MARKER_TVD: TVD marker; can be inserted within actual survey
        stations also.
    :cvar MD_AND_INCL: An old style drift indicator by Totco /
        inclination-only survey.
    :cvar MD_INCL_AND_AZI: A normal MWD / gyro survey.
    :cvar N_E_AND_TVD: A point on a computed trajectory with northing,
        easting and true vertical depth.
    :cvar NS_EW_AND_TVD: Specified as TVD, NS, EW; could be used for
        point or drilling target (non-geological target).
    :cvar TARGET_CENTER: Specified as TVD, NS, EW of target center;
        requires target ID association.
    :cvar TARGET_OFFSET: Specified as TVD, NS, EW of target offset;
        requires target ID association.
    :cvar TIE_IN_POINT: Tie-in point for the survey.
    :cvar TURNRATE_TO_AZI: Section follows a given turn rate to an
        azimuth.
    :cvar TURNRATE_TO_DELTA_MD: Section follows a given turn rate to a
        given delta measured depth.
    :cvar TURNRATE_TO_MD: Section follows a given turn rate to a given
        measured depth.
    :cvar TURNRATE_TO_TVD: Section follows a given turn rate to a given
        TVD.
    :cvar UNKNOWN: The value is not known. Avoid using this value. All
        reasonable attempts should be made to determine the appropriate
        value. Use of this value may result in rejection in some
        situations.
    """
    AZIMUTH_ON_PLANE = "azimuth on plane"
    BUILDRATE_TO_DELTA_MD = "buildrate to delta-MD"
    BUILDRATE_TO_INCL = "buildrate to INCL"
    BUILDRATE_TO_MD = "buildrate to MD"
    BUILDRATE_AND_TURNRATE_TO_AZI = "buildrate and turnrate to AZI"
    BUILDRATE_AND_TURNRATE_TO_DELTA_MD = "buildrate and turnrate to delta-MD"
    BUILDRATE_AND_TURNRATE_TO_INCL = "buildrate and turnrate to INCL"
    BUILDRATE_AND_TURNRATE_TO_INCL_AND_AZI = "buildrate and turnrate to INCL and AZI"
    BUILDRATE_AND_TURNRATE_TO_MD = "buildrate and turnrate to MD"
    BUILDRATE_AND_TURNRATE_TO_TVD = "buildrate and turnrate to TVD"
    BUILDRATE_TVD = "buildrate TVD"
    CASING_MD = "casing MD"
    CASING_TVD = "casing TVD"
    DLS = "DLS"
    DLS_TO_AZI_AND_MD = "DLS to AZI and MD"
    DLS_TO_AZI_TVD = "DLS to AZI-TVD"
    DLS_TO_INCL = "DLS to INCL"
    DLS_TO_INCL_AND_AZI = "DLS to INCL and AZI"
    DLS_TO_INCL_AND_MD = "DLS to INCL and MD"
    DLS_TO_INCL_AND_TVD = "DLS to INCL and TVD"
    DLS_TO_NS = "DLS to NS"
    DLS_AND_TOOLFACE_TO_AZI = "DLS and toolface to AZI"
    DLS_AND_TOOLFACE_TO_DELTA_MD = "DLS and toolface to delta-MD"
    DLS_AND_TOOLFACE_TO_INCL = "DLS and toolface to INCL"
    DLS_AND_TOOLFACE_TO_INCL_AZI = "DLS and toolface to INCL-AZI"
    DLS_AND_TOOLFACE_TO_MD = "DLS and toolface to MD"
    DLS_AND_TOOLFACE_TO_TVD = "DLS and toolface to TVD"
    FORMATION_MD = "formation MD"
    FORMATION_TVD = "formation TVD"
    HOLD_TO_DELTA_MD = "hold to delta-MD"
    HOLD_TO_MD = "hold to MD"
    HOLD_TO_TVD = "hold to TVD"
    INCL_AZI_AND_TVD = "INCL AZI and TVD"
    INTERPOLATED = "interpolated"
    MARKER_MD = "marker MD"
    MARKER_TVD = "marker TVD"
    MD_AND_INCL = "MD and INCL"
    MD_INCL_AND_AZI = "MD INCL and AZI"
    N_E_AND_TVD = "N E and TVD"
    NS_EW_AND_TVD = "NS EW and TVD"
    TARGET_CENTER = "target center"
    TARGET_OFFSET = "target offset"
    TIE_IN_POINT = "tie in point"
    TURNRATE_TO_AZI = "turnrate to AZI"
    TURNRATE_TO_DELTA_MD = "turnrate to delta-MD"
    TURNRATE_TO_MD = "turnrate to MD"
    TURNRATE_TO_TVD = "turnrate to TVD"
    UNKNOWN = "unknown"
