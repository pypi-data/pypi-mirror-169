from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_cement_stage import AbstractCementStage
from witsml20.pressure_measure import PressureMeasure
from witsml20.time_measure import TimeMeasure
from witsml20.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class CementStageReport(AbstractCementStage):
    """
    Report of key parameters for a stage of cement job.

    :ivar dtim_mix_start: Date and time when mixing of cement started.
    :ivar dtim_pump_start: Date and time when pumping cement started.
    :ivar dtim_pump_end: Date and time when pumping cement ended.
    :ivar dtim_displace_start: Date and time when displacing of cement
        started.
    :ivar pres_break_down: Breakdown pressure.
    :ivar flowrate_break_down: Breakdown rate.
    :ivar flowrate_displace_av: Average displacement rate.
    :ivar flowrate_displace_mx: Maximum displacement rate.
    :ivar pres_squeeze_av: Squeeze pressure average.
    :ivar pres_squeeze_end: Squeeze pressure final.
    :ivar pres_squeeze_held: Squeeze pressure held.  Values are "true"
        (or "1") and "false" (or "0").
    :ivar etim_mud_circulation: Elapsed time of mud circulation before
        the job/stage.
    :ivar pres_squeeze: Squeeze pressure left on pipe.
    :ivar flowrate_squeeze_av: Squeeze job average rate.
    :ivar flowrate_squeeze_mx: Squeeze job maximum rate.
    :ivar flowrate_end: Final displacement pump rate.
    :ivar flowrate_pump_start: Pump rate at the start of the job.
    :ivar flowrate_pump_end: Pump rate at the end of the job.
    :ivar vis_funnel_mud: Funnel viscosity in seconds (in hole at start
        of job/stage).
    :ivar plug_bumped: Plug bumped? Values are "true" (or "1") and
        "false" (or "0").
    :ivar squeeze_obtained: Squeeze obtained.  Values are "true" (or
        "1") and "false" (or "0").
    :ivar pres_prior_bump: Pressure before bumping plug / pressure at
        the end of  the displacement.
    :ivar float_held: Float held?  Values are "true" (or "1") and
        "false" (or "0").
    :ivar uid: Unique identifier for this instance of CementStageReport
    """
    dtim_mix_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimMixStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pump_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPumpStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_pump_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimPumpEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_displace_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimDisplaceStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    pres_break_down: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBreakDown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_break_down: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateBreakDown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_displace_av: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateDisplaceAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_displace_mx: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateDisplaceMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_squeeze_av: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresSqueezeAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_squeeze_end: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresSqueezeEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_squeeze_held: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PresSqueezeHeld",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    etim_mud_circulation: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimMudCirculation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_squeeze: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresSqueeze",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_squeeze_av: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateSqueezeAv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_squeeze_mx: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateSqueezeMx",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_end: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_pump_start: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowratePumpStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    flowrate_pump_end: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowratePumpEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vis_funnel_mud: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "VisFunnelMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    plug_bumped: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlugBumped",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    squeeze_obtained: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SqueezeObtained",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_prior_bump: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresPriorBump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    float_held: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FloatHeld",
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
