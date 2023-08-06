from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.azi_ref import AziRef
from witsml20.channel_status import ChannelStatus
from witsml20.data_object_reference import DataObjectReference
from witsml20.length_measure import LengthMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.trajectory_station import TrajectoryStation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Trajectory(AbstractObject):
    """The trajectory object is used to capture information about a directional
    survey in a wellbore.

    It contains many trajectory stations to capture the information
    about individual survey points. This object is uniquely identified
    within the context of one wellbore object.

    :ivar growing_status: Describes the growing status of the
        trajectory, whether active, inactive or closed
    :ivar dtim_traj_start: Start date and time of trajectory station
        measurements. Note that this is NOT a server query parameter.
    :ivar dtim_traj_end: End date and time of trajectory station
        measurements. Note that this is NOT a server query parameter.
    :ivar md_mn: Minimum measured depth of this object. This is an API
        "structural-range" query parameter for growing objects. See the
        relevant API specification for the query behavior related to
        this element.
    :ivar md_mx: Maximum measured depth of this object. This is an API
        "structural-range" query parameter for growing objects. See the
        relevant API specification for the query behavior related to
        this element.
    :ivar service_company: Name of contractor who provided the service.
    :ivar mag_decl_used: Magnetic declination used to correct a Magnetic
        North referenced azimuth to a True North azimuth.  Magnetic
        declination angles are measured positive clockwise from True
        North to Magnetic North (or negative in the anti-clockwise
        direction). To convert a Magnetic azimuth to a True North
        azimuth, the magnetic declination should be added. Starting
        value if stations have individual values.
    :ivar grid_con_used: Magnetic declination (convergence) used to
        correct a Magnetic North referenced azimuth to a True North
        azimuth.  Magnetic declination angles are measured positive
        clockwise from True North to Magnetic North (or negative in the
        anti-clockwise direction). To convert a Magnetic azimuth to a
        True North azimuth, the magnetic declination should be added.
        Starting value if stations have individual values.
    :ivar azi_vert_sect: Azimuth used for vertical section
        plot/computations.
    :ivar disp_ns_vert_sect_orig: Origin north-south used for vertical
        section plot/computations.
    :ivar disp_ew_vert_sect_orig: Origin east-west used for vertical
        section plot/computations.
    :ivar definitive: True ("true" or "1") indicates that this
        trajectory is definitive for this wellbore. False ("false" or
        "0") or not given indicates otherwise. There can only be one
        trajectory per wellbore with definitive=true and it must define
        the geometry of the whole wellbore (surface to bottom). The
        definitive trajectory may represent a composite of information
        in many other trajectories. A query requesting a subset of the
        possible information can provide a simplistic view of the
        geometry of the wellbore.
    :ivar memory: Is trajectory a result of a memory dump from a tool?
        Values are "true" (or "1") and "false" (or "0").
    :ivar final_traj: Is trajectory a final or intermediate/preliminary?
        Values are "true" (or "1") and "false" (or "0").
    :ivar azi_ref: Specifies the definition of north. While this is
        optional because of legacy data, it is strongly recommended that
        this always be specified.
    :ivar trajectory_station:
    :ivar wellbore:
    :ivar parent_trajectory:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    growing_status: Optional[ChannelStatus] = field(
        default=None,
        metadata={
            "name": "GrowingStatus",
            "type": "Element",
            "required": True,
        }
    )
    dtim_traj_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimTrajStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_traj_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimTrajEnd",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    md_mn: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdMn",
            "type": "Element",
        }
    )
    md_mx: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdMx",
            "type": "Element",
        }
    )
    service_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
            "type": "Element",
            "max_length": 64,
        }
    )
    mag_decl_used: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MagDeclUsed",
            "type": "Element",
        }
    )
    grid_con_used: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "GridConUsed",
            "type": "Element",
        }
    )
    azi_vert_sect: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "AziVertSect",
            "type": "Element",
        }
    )
    disp_ns_vert_sect_orig: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispNsVertSectOrig",
            "type": "Element",
        }
    )
    disp_ew_vert_sect_orig: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispEwVertSectOrig",
            "type": "Element",
        }
    )
    definitive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Definitive",
            "type": "Element",
        }
    )
    memory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Memory",
            "type": "Element",
        }
    )
    final_traj: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinalTraj",
            "type": "Element",
        }
    )
    azi_ref: Optional[AziRef] = field(
        default=None,
        metadata={
            "name": "AziRef",
            "type": "Element",
        }
    )
    trajectory_station: List[TrajectoryStation] = field(
        default_factory=list,
        metadata={
            "name": "TrajectoryStation",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
    parent_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentTrajectory",
            "type": "Element",
        }
    )
