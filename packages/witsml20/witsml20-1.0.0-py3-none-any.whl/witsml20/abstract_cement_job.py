from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.angular_velocity_measure import AngularVelocityMeasure
from witsml20.force_measure import ForceMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.md_interval import MdInterval
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.moment_of_force_measure import MomentOfForceMeasure
from witsml20.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractCementJob:
    """
    Defines common elements for both cement job designs and reports.

    :ivar cement_engr: Cementing engineer.
    :ivar etim_waiting_on_cement: Duration for waiting on cement to set.
    :ivar plug_interval: If plug used,  measured depth interval between
        the top and base of the plug.
    :ivar md_hole: Measured depth at the bottom of  the hole.
    :ivar contractor: Name of cementing contractor.
    :ivar rpm_pipe: Pipe rotation rate (commonly in rotations per minute
        (RPM)).
    :ivar tq_init_pipe_rot: Pipe rotation: initial torque.
    :ivar tq_pipe_av: Pipe rotation: average torque.
    :ivar tq_pipe_mx: Pipe rotation: maximum torque.
    :ivar over_pull: String-up weight during reciprocation.
    :ivar slack_off: String-down weight during reciprocation.
    :ivar rpm_pipe_recip: Pipe reciprocation (RPM).
    :ivar len_pipe_recip_stroke: Pipe reciprocation: stroke length.
    :ivar reciprocating: Is the pipe being reciprocated (raised and
        lowered)? Values are "true" (or "1") and "false" (or "0").
    """
    cement_engr: Optional[str] = field(
        default=None,
        metadata={
            "name": "CementEngr",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    etim_waiting_on_cement: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimWaitingOnCement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    plug_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "PlugInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_hole: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    contractor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Contractor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    rpm_pipe: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RpmPipe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_init_pipe_rot: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqInitPipeRot",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_pipe_av: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqPipeAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tq_pipe_mx: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "TqPipeMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    over_pull: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "OverPull",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    slack_off: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "SlackOff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rpm_pipe_recip: Optional[AngularVelocityMeasure] = field(
        default=None,
        metadata={
            "name": "RpmPipeRecip",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    len_pipe_recip_stroke: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "LenPipeRecipStroke",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reciprocating: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Reciprocating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
