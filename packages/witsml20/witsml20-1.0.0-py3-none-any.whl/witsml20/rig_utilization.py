from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.bop import Bop
from witsml20.centrifuge import Centrifuge
from witsml20.data_object_reference import DataObjectReference
from witsml20.degasser import Degasser
from witsml20.draw_works_type import DrawWorksType
from witsml20.drive_type import DriveType
from witsml20.force_measure import ForceMeasure
from witsml20.hydrocyclone import Hydrocyclone
from witsml20.length_measure import LengthMeasure
from witsml20.moment_of_force_measure import MomentOfForceMeasure
from witsml20.mud_pump import MudPump
from witsml20.pit import Pit
from witsml20.plane_angle_measure import PlaneAngleMeasure
from witsml20.power_measure import PowerMeasure
from witsml20.shaker import Shaker
from witsml20.surface_equipment import SurfaceEquipment
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RigUtilization(AbstractObject):
    """Rig Utilization Schema.

    Used to capture information related to the usage of a specific rig.
    For information unique to the rig itself, see the Rig object.

    :ivar start_operation_time: Start time of the operation in which the
        rig was used.
    :ivar end_operation_time: End time of the operation in which the rig
        was used.
    :ivar start_hole_depth: Measured depth of the wellbore when
        operations performed with this rig started.
    :ivar end_hole_depth: Measured depth of the wellbore when operations
        performed with this rig ended.
    :ivar datum: Datum for location reference.
    :ivar air_gap: Air gap from the rig floor to the ground or mean sea
        level, depending on the rig location.
    :ivar wt_block: Weight of the block.
    :ivar rating_block: Rating for the block.
    :ivar num_block_lines: Number of block lines.
    :ivar type_hook: Type of hook installed for this rig usage.
    :ivar rating_hkld: Maximum weight rating of the hook as configured
        for this rig usage.
    :ivar size_drill_line: Drill line diameter.
    :ivar type_draw_works: Draw works type.
    :ivar power_draw_works: Draw works horse power.
    :ivar rating_draw_works: Weight rating of the draw works.
    :ivar motor_draw_works: Description of the draw works motor.
    :ivar desc_brake: Rig brake description.
    :ivar type_swivel: Type of swivel.
    :ivar rating_swivel: Maximum swivel rating.
    :ivar rot_system: Work string drive type.
    :ivar desc_rot_system: Description of rotating system.
    :ivar rating_tq_rot_sys: Work string rotational torque rating.
    :ivar rot_size_opening: Rotary size opening.
    :ivar rating_rot_system: Work string rotational torque rating.
    :ivar scr_system: Description of slow circulation rates (SCR)
        system.
    :ivar pipe_handling_system: Name of pipe-handling system.
    :ivar cap_bulk_mud: Bulk/dry mud storage capacity.
    :ivar cap_liquid_mud: Liquid mud storage capacity.
    :ivar cap_drill_water: Drill water capacity.
    :ivar cap_potable_water: Potable water capacity.
    :ivar cap_fuel: Fuel capacity.
    :ivar cap_bulk_cement: Capacity of bulk cement.
    :ivar main_engine: Power system.
    :ivar generator: Description of the electrical power generating
        system.
    :ivar cement_unit: Name of the cement unit on the rig.
    :ivar num_bunks: Number of beds available on the rig.
    :ivar bunks_per_room: Number of bunks per room.
    :ivar num_anch: Number of anchors.
    :ivar moor_type: Mooring type.
    :ivar num_guide_tens: Number of guideline tensioners.
    :ivar num_riser_tens: Number of riser tensioners.
    :ivar var_deck_ld_mx: Variable deck load maximum (offshore rigs
        only).
    :ivar vdl_storm: Variable deck load storm rating (offshore rigs
        only).
    :ivar num_thrusters: Number of thrusters.
    :ivar azimuthing: Are the thrusters azimuth?  Values are "true" (or
        "1") and "false" (or "0").
    :ivar motion_compensation_mn: Minimum motion compensation.
    :ivar motion_compensation_mx: Maximum motion compensation.
    :ivar stroke_motion_compensation: Length of motion compensation
        provided by equipment.
    :ivar riser_angle_limit: Riser angle limit.
    :ivar heave_mx: Maximum allowable heave.
    :ivar gantry: Description of the gantry.
    :ivar flares: Description of flare(s).
    :ivar shaker:
    :ivar wellbore:
    :ivar bop:
    :ivar pit:
    :ivar pump:
    :ivar centrifuge:
    :ivar hydrocyclone:
    :ivar degasser:
    :ivar surface_equipment:
    :ivar bha_run:
    :ivar rig:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    start_operation_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartOperationTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_operation_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndOperationTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    start_hole_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "StartHoleDepth",
            "type": "Element",
        }
    )
    end_hole_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "EndHoleDepth",
            "type": "Element",
        }
    )
    datum: Optional[str] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "max_length": 64,
        }
    )
    air_gap: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "AirGap",
            "type": "Element",
        }
    )
    wt_block: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "WtBlock",
            "type": "Element",
        }
    )
    rating_block: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "RatingBlock",
            "type": "Element",
        }
    )
    num_block_lines: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumBlockLines",
            "type": "Element",
        }
    )
    type_hook: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeHook",
            "type": "Element",
            "max_length": 64,
        }
    )
    rating_hkld: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "RatingHkld",
            "type": "Element",
        }
    )
    size_drill_line: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SizeDrillLine",
            "type": "Element",
        }
    )
    type_draw_works: Optional[DrawWorksType] = field(
        default=None,
        metadata={
            "name": "TypeDrawWorks",
            "type": "Element",
        }
    )
    power_draw_works: Optional[PowerMeasure] = field(
        default=None,
        metadata={
            "name": "PowerDrawWorks",
            "type": "Element",
        }
    )
    rating_draw_works: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "RatingDrawWorks",
            "type": "Element",
        }
    )
    motor_draw_works: Optional[str] = field(
        default=None,
        metadata={
            "name": "MotorDrawWorks",
            "type": "Element",
            "max_length": 64,
        }
    )
    desc_brake: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescBrake",
            "type": "Element",
            "max_length": 64,
        }
    )
    type_swivel: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeSwivel",
            "type": "Element",
            "max_length": 64,
        }
    )
    rating_swivel: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "RatingSwivel",
            "type": "Element",
        }
    )
    rot_system: Optional[DriveType] = field(
        default=None,
        metadata={
            "name": "RotSystem",
            "type": "Element",
        }
    )
    desc_rot_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescRotSystem",
            "type": "Element",
            "max_length": 64,
        }
    )
    rating_tq_rot_sys: Optional[MomentOfForceMeasure] = field(
        default=None,
        metadata={
            "name": "RatingTqRotSys",
            "type": "Element",
        }
    )
    rot_size_opening: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "RotSizeOpening",
            "type": "Element",
        }
    )
    rating_rot_system: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "RatingRotSystem",
            "type": "Element",
        }
    )
    scr_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "ScrSystem",
            "type": "Element",
            "max_length": 64,
        }
    )
    pipe_handling_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "PipeHandlingSystem",
            "type": "Element",
            "max_length": 64,
        }
    )
    cap_bulk_mud: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CapBulkMud",
            "type": "Element",
        }
    )
    cap_liquid_mud: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CapLiquidMud",
            "type": "Element",
        }
    )
    cap_drill_water: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CapDrillWater",
            "type": "Element",
        }
    )
    cap_potable_water: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CapPotableWater",
            "type": "Element",
        }
    )
    cap_fuel: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CapFuel",
            "type": "Element",
        }
    )
    cap_bulk_cement: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CapBulkCement",
            "type": "Element",
        }
    )
    main_engine: Optional[str] = field(
        default=None,
        metadata={
            "name": "MainEngine",
            "type": "Element",
            "max_length": 64,
        }
    )
    generator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Generator",
            "type": "Element",
            "max_length": 64,
        }
    )
    cement_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "CementUnit",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_bunks: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumBunks",
            "type": "Element",
        }
    )
    bunks_per_room: Optional[int] = field(
        default=None,
        metadata={
            "name": "BunksPerRoom",
            "type": "Element",
        }
    )
    num_anch: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumAnch",
            "type": "Element",
        }
    )
    moor_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MoorType",
            "type": "Element",
            "max_length": 64,
        }
    )
    num_guide_tens: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumGuideTens",
            "type": "Element",
        }
    )
    num_riser_tens: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumRiserTens",
            "type": "Element",
        }
    )
    var_deck_ld_mx: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "VarDeckLdMx",
            "type": "Element",
        }
    )
    vdl_storm: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "VdlStorm",
            "type": "Element",
        }
    )
    num_thrusters: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumThrusters",
            "type": "Element",
        }
    )
    azimuthing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Azimuthing",
            "type": "Element",
        }
    )
    motion_compensation_mn: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "MotionCompensationMn",
            "type": "Element",
        }
    )
    motion_compensation_mx: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "MotionCompensationMx",
            "type": "Element",
        }
    )
    stroke_motion_compensation: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "StrokeMotionCompensation",
            "type": "Element",
        }
    )
    riser_angle_limit: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "RiserAngleLimit",
            "type": "Element",
        }
    )
    heave_mx: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "HeaveMx",
            "type": "Element",
        }
    )
    gantry: Optional[str] = field(
        default=None,
        metadata={
            "name": "Gantry",
            "type": "Element",
            "max_length": 64,
        }
    )
    flares: Optional[str] = field(
        default=None,
        metadata={
            "name": "Flares",
            "type": "Element",
            "max_length": 64,
        }
    )
    shaker: List[Shaker] = field(
        default_factory=list,
        metadata={
            "name": "Shaker",
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
    bop: Optional[Bop] = field(
        default=None,
        metadata={
            "name": "Bop",
            "type": "Element",
        }
    )
    pit: List[Pit] = field(
        default_factory=list,
        metadata={
            "name": "Pit",
            "type": "Element",
        }
    )
    pump: List[MudPump] = field(
        default_factory=list,
        metadata={
            "name": "Pump",
            "type": "Element",
        }
    )
    centrifuge: List[Centrifuge] = field(
        default_factory=list,
        metadata={
            "name": "Centrifuge",
            "type": "Element",
        }
    )
    hydrocyclone: List[Hydrocyclone] = field(
        default_factory=list,
        metadata={
            "name": "Hydrocyclone",
            "type": "Element",
        }
    )
    degasser: List[Degasser] = field(
        default_factory=list,
        metadata={
            "name": "Degasser",
            "type": "Element",
        }
    )
    surface_equipment: Optional[SurfaceEquipment] = field(
        default=None,
        metadata={
            "name": "SurfaceEquipment",
            "type": "Element",
        }
    )
    bha_run: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BhaRun",
            "type": "Element",
        }
    )
    rig: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Rig",
            "type": "Element",
            "required": True,
        }
    )
