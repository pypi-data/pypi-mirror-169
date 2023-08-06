from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.cement_pump_schedule_step import CementPumpScheduleStep
from witsml20.dynamic_viscosity_measure import DynamicViscosityMeasure
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.fluid_location import FluidLocation
from witsml20.force_measure import ForceMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.mass_per_volume_measure import MassPerVolumeMeasure
from witsml20.md_interval import MdInterval
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.pressure_measure import PressureMeasure
from witsml20.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from witsml20.time_measure import TimeMeasure
from witsml20.volume_measure import VolumeMeasure
from witsml20.volume_per_time_measure import VolumePerTimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractCementStage:
    """
    Defines the information that is common to the cement job stage design and
    reports.

    :ivar annular_flow_after: Annular flow present after the stage was
        completed?  Values are "true" (or "1") and "false" (or "0").
    :ivar reciprocation_slackoff: Slackoff for reciprocation.
    :ivar bot_plug: Bottom plug used?  Values are "true" (or "1") and
        "false" (or "0").
    :ivar bot_plug_number: Amount of bottom plug used.
    :ivar dia_tail_pipe: Tail pipe size (diameter).
    :ivar displacement_fluid_ref_id: Reference to displacement fluid
        properties.
    :ivar etim_pres_held: Time the pressure was held.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar flowrate_mud_circ: Rate the mud was circulated during the
        stage.
    :ivar gel10_min: Gels-10Min (in hole at start of job).
    :ivar gel10_sec: Gels-10Sec (in hole at start of job).
    :ivar md_circ_out: Circulate out measured depth.
    :ivar md_coil_tbg: Measured depth of coil tubing (multi-stage cement
        job).
    :ivar md_string: Measured depth of string (multi-stage cement job).
    :ivar md_tool: Measured depth of the tool (multi-stage cement job).
    :ivar mix_method: Mix method.
    :ivar num_stage: Stage number.
    :ivar reciprocation_overpull: Overpull amount for reciprocation.
    :ivar pill_below_plug: Pill below plug?  Values are "true" (or "1")
        and "false" (or "0").
    :ivar plug_catcher: Plug catcher?  Values are "true" (or "1") and
        "false" (or "0").
    :ivar pres_back_pressure: Constant back pressure applied while
        pumping the job (can be superseded by a back pressure per
        pumping stage).
    :ivar pres_bump: Pressure plug bumped.
    :ivar pres_coil_tbg_end: Pressure coiled tubing end.
    :ivar pres_coil_tbg_start: Pressure coiled tubing start
    :ivar pres_csg_end: Casing pressure at the end of the job.
    :ivar pres_csg_start: Casing pressure at the start of the job.
    :ivar pres_displace: Final displacement pressure.
    :ivar pres_held: Pressure held to.
    :ivar pres_mud_circ: Mud circulation pressure.
    :ivar pres_tbg_end: Tubing pressure at the end of the job (not
        coiled tubing).
    :ivar pres_tbg_start: Tubing pressure at the start of the job (not
        coiled tubing).
    :ivar pv_mud: Plastic viscosity (in the hole at the start of the
        job).
    :ivar squeeze_objective: Squeeze objective.
    :ivar stage_md_interval: Measured depth interval for the cement
        stage.
    :ivar tail_pipe_perf: Tail pipe perforated?  Values are "true" (or
        "1") and "false" (or "0").
    :ivar tail_pipe_used: Tail pipe used?  Values are "true" (or "1")
        and "false" (or "0").
    :ivar temp_bhct: Bottomhole temperature: circulating.
    :ivar temp_bhst: Bottomhole temperature: static.
    :ivar top_plug: Top plug used?  Values are "true" (or "1") and
        "false" (or "0").
    :ivar type_original_mud: Type of mud in the hole.
    :ivar type_stage: Stage type.
    :ivar vol_circ_prior: Total volume circulated before starting the
        job/stage.
    :ivar vol_csg_in: Total volume inside the casing for this stage
        placement.
    :ivar vol_csg_out: Total volume outside casing for this stage
        placement.
    :ivar vol_displace_fluid: Volume of displacement fluid.
    :ivar vol_excess: Excess volume.
    :ivar vol_excess_method: Method to estimate excess volume.
    :ivar vol_mud_lost: Total mud lost.
    :ivar vol_returns: Volume of returns.
    :ivar wt_mud: Mud density.
    :ivar yp_mud: Yield point (in the hole at the start of the job).
    :ivar original_fluid_location:
    :ivar ending_fluid_location:
    :ivar step:
    """
    annular_flow_after: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AnnularFlowAfter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    reciprocation_slackoff: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ReciprocationSlackoff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bot_plug: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BotPlug",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bot_plug_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "BotPlugNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    dia_tail_pipe: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DiaTailPipe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    displacement_fluid_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "DisplacementFluidRefId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    etim_pres_held: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "ETimPresHeld",
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
    flowrate_mud_circ: Optional[VolumePerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "FlowrateMudCirc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel10_min: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10Min",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gel10_sec: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Gel10Sec",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_circ_out: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdCircOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_coil_tbg: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdCoilTbg",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_string: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    md_tool: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdTool",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mix_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "MixMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    num_stage: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumStage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    reciprocation_overpull: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "ReciprocationOverpull",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pill_below_plug: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PillBelowPlug",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    plug_catcher: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PlugCatcher",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_back_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBackPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_bump: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresBump",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_coil_tbg_end: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCoilTbgEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_coil_tbg_start: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCoilTbgStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_csg_end: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCsgEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_csg_start: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresCsgStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_displace: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresDisplace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_held: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresHeld",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_mud_circ: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresMudCirc",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_tbg_end: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresTbgEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pres_tbg_start: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PresTbgStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    pv_mud: Optional[DynamicViscosityMeasure] = field(
        default=None,
        metadata={
            "name": "PvMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    squeeze_objective: Optional[str] = field(
        default=None,
        metadata={
            "name": "SqueezeObjective",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    stage_md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "StageMdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tail_pipe_perf: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TailPipePerf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tail_pipe_used: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TailPipeUsed",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_bhct: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempBHCT",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    temp_bhst: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TempBHST",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    top_plug: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TopPlug",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type_original_mud: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeOriginalMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    type_stage: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeStage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    vol_circ_prior: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolCircPrior",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_csg_in: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolCsgIn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_csg_out: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolCsgOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_displace_fluid: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolDisplaceFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_excess: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolExcess",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_excess_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "VolExcessMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    vol_mud_lost: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolMudLost",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_returns: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolReturns",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    wt_mud: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WtMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    yp_mud: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "YpMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    original_fluid_location: List[FluidLocation] = field(
        default_factory=list,
        metadata={
            "name": "OriginalFluidLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ending_fluid_location: List[FluidLocation] = field(
        default_factory=list,
        metadata={
            "name": "EndingFluidLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    step: List[CementPumpScheduleStep] = field(
        default_factory=list,
        metadata={
            "name": "Step",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
