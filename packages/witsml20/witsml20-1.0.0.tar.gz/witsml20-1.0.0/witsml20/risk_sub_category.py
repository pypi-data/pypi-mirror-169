from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class RiskSubCategory(Enum):
    """
    Specifies the sub-category of risk, in relation to value of Risk Category.

    :cvar GAS_KICK:
    :cvar SHALLOW_WATER_INFLUX:
    :cvar OTHER_INFLUX_OR_KICKS:
    :cvar LOSS_CIRCULATION:
    :cvar POOR_HOLE_CLEANING:
    :cvar GOOD_HOLE_CLEANING_AT_HIGH_ROP: Rate of Penetration
    :cvar HIGH_MUD_WEIGHT: High mud weight (i.e., greater than 10 parts
        per US gallon).
    :cvar SPECIAL_ADDITIVES_NEEDED:
    :cvar GUMBO_PROBLEMS:
    :cvar HIGH_ECD_RHEOLOGY_RELATED:
    :cvar EXCESSIVE_CIRCULATION: Greater than 2 hours.
    :cvar PERFORMING_A_KILL:
    :cvar MUD_WEIGHT_CHANGE: Greater than 0.5 parts per US gallon.
    :cvar EXCESSIVE_PIPE_CEMENT_SCALING:
    :cvar PIT_GAIN_OR_LOSS: Greater than ten barrles.
    :cvar MUD_STABILITY_PROBLEMS:
    :cvar SHALLOW_GAS_FLOW:
    :cvar TWIST_OFF:
    :cvar STUCK_PIPE: Greater than 30 minutes.
    :cvar WIRELINE_STUCK_IN_HOLE:
    :cvar STICK_AND_SLIP:
    :cvar VIBRATION_AXIAL:
    :cvar VIBRATION_TORSIONAL:
    :cvar VIBRATION_TRANSVERSE:
    :cvar VIBRATION_UNKNOWN_OR_ROUGH_DRILLING:
    :cvar UNEVEN_WEAR_OF_BHA:
    :cvar UNEVEN_WEAR_OF_DRILLSTRING:
    :cvar EXCESSIVE_TORQUE:
    :cvar EXCESSIVE_DRAG:
    :cvar REAMING_GREATER_THAN_2_HOURS: Greater than 2 hours.
    :cvar WASHOUTS:
    :cvar TIGHT_HOLE_OR_OVER_PULL:
    :cvar FAILED_INSPECTIONS_OR_FATIGUE_WEAR:
    :cvar MECHANICAL:
    :cvar DRILLING_GREATER_THAN_1000_FEET_DAY: Greater than 1000 feet
        per day.
    :cvar DRILLING_GREATER_THAN_2000_FEET_DAY: Greater than 2000 feet
        per day.
    :cvar DRILLING_LESS_THAN_20_FEET_DAY: Less than 20 feet per day.
    :cvar TRIPS_GREATER_THAN_24_HOURS: Greater than 24 hours.
    :cvar EXCESSIVE_TIME_FOR_BHA_MAKEUP: Bottom Hole Assembly
    :cvar WAITING_ON_DECISIONS:
    :cvar WAITING_ON_WEATHER:
    :cvar WAITING_ON_TOOLS:
    :cvar SLOUGHING_OR_PACKOFFS:
    :cvar BALLOONING:
    :cvar FRACTURE_PROBLEMS:
    :cvar UNSTABLE_ZONES:
    :cvar FORMATION_INTEGRITY_TEST:
    :cvar LEAK_OFF_TEST:
    :cvar TECTONICS:
    :cvar PORE_PRESSURE:
    :cvar BREAKOUTS:
    :cvar BED_PARALLEL:
    :cvar WELLBORE_STABILITY:
    :cvar EXCESSIVE_DOGLEGS:
    :cvar SIDETRACK:
    :cvar BHA_CHANGE_FOR_DIRECTIONAL: Bottom Hole Assembly
    :cvar WRONG_TOTAL_FLOW_AREA:
    :cvar WELL_COLLISION_ACTUAL:
    :cvar WELL_COLLISION_TECHNICAL:
    :cvar GEOSTEERING:
    :cvar ABNORMAL_TENDENCY_CHANGES:
    :cvar RESURVEYING:
    :cvar IN_FIELD_REFERENCING_IFR_ACTIONS:
    :cvar BIT_OR_BHA_PERFORMANCE: Bottom Hole Assembly
    :cvar DRILLING_OPTIMIZATION:
    :cvar BIT_BALLING:
    :cvar LOST_CONES_OR_BROKEN_CUTTERS:
    :cvar EXCESSIVE_BIT_WEAR_OR_GAUGE:
    :cvar LOW_RATE_OF_BIT_PENETRATION:
    :cvar HIGH_RATE_OF_BIT_PENETRATION:
    :cvar DOWNHOLE_TOOL:
    :cvar SURFACE_SYSTEM:
    :cvar MOTOR_OR_ROTARY_STEERABLE_SYSTEM_FAILURE:
    :cvar TOPDRIVE_FAILURE:
    :cvar HOISTING_EQUIPMENT_FAILURE:
    :cvar CIRCULATING_EQUIPMENT_FAILURE:
    :cvar ELECTRICAL_SYSTEM_FAILURE:
    :cvar BLOW_OUT_PREVENTER_EVENTS:
    :cvar SURFACE_INSTRUMENTATION_PROBLEMS:
    :cvar RIG_COMMUNICATIONS:
    :cvar COMPLETION_EQUIPMENT_FAILURE:
    :cvar MISCELLANEOUS_RIG_EQUIPMENT:
    :cvar TOOL_OR_EQUIPMENT_FAILURE:
    :cvar SQUEEZE_JOBS:
    :cvar CASING_SURGE_LOSSES:
    :cvar STUCK_CASING_OR_COMPLETION:
    :cvar SHOE_FAILURES:
    :cvar EARLY_CEMENT_SETUP:
    :cvar CASING_COLLAPSE:
    :cvar MILLING:
    :cvar EXCESSIVE_CASING_WEAR_OR_CUTTINGS:
    :cvar EXCESSIVE_FORMATION_DAMAGE_OR_SKIN:
    :cvar CASING_ROTATION_OR_RECIPROCATION_RQD:
    :cvar BROACHING:
    :cvar COMPLETION_OR_CASING:
    :cvar STRATIGRAPHY:
    :cvar FISHING:
    :cvar JUNK_IN_HOLE:
    :cvar DELAY_DUE_TO_POLITICAL_UNREST:
    :cvar RIG_MOVE:
    :cvar GAS_HYDRATES:
    :cvar PENDING_ANALYSIS:
    :cvar RISER_DISCONNECT:
    :cvar OTHER:
    :cvar PERSONNEL:
    :cvar ENVIRONMENTAL:
    :cvar AUTOMOTIVE:
    :cvar ASSET:
    :cvar INFORMATION:
    :cvar TIME:
    :cvar HSE: health, safety and environmental
    """
    GAS_KICK = "gas kick"
    SHALLOW_WATER_INFLUX = "shallow water influx"
    OTHER_INFLUX_OR_KICKS = "other influx or kicks"
    LOSS_CIRCULATION = "loss circulation"
    POOR_HOLE_CLEANING = "poor hole cleaning"
    GOOD_HOLE_CLEANING_AT_HIGH_ROP = "good hole cleaning at high ROP"
    HIGH_MUD_WEIGHT = "high mud weight"
    SPECIAL_ADDITIVES_NEEDED = "special additives needed"
    GUMBO_PROBLEMS = "gumbo problems"
    HIGH_ECD_RHEOLOGY_RELATED = "high ECD - rheology related"
    EXCESSIVE_CIRCULATION = "excessive circulation"
    PERFORMING_A_KILL = "performing a kill"
    MUD_WEIGHT_CHANGE = "mud weight change"
    EXCESSIVE_PIPE_CEMENT_SCALING = "excessive pipe cement scaling"
    PIT_GAIN_OR_LOSS = "pit gain or loss"
    MUD_STABILITY_PROBLEMS = "mud stability problems"
    SHALLOW_GAS_FLOW = "shallow gas flow"
    TWIST_OFF = "twist off"
    STUCK_PIPE = "stuck pipe"
    WIRELINE_STUCK_IN_HOLE = "wireline stuck in hole"
    STICK_AND_SLIP = "stick and slip"
    VIBRATION_AXIAL = "vibration - axial"
    VIBRATION_TORSIONAL = "vibration - torsional"
    VIBRATION_TRANSVERSE = "vibration - transverse"
    VIBRATION_UNKNOWN_OR_ROUGH_DRILLING = "vibration unknown or rough drilling"
    UNEVEN_WEAR_OF_BHA = "uneven wear of BHA"
    UNEVEN_WEAR_OF_DRILLSTRING = "uneven wear of drillstring"
    EXCESSIVE_TORQUE = "excessive torque"
    EXCESSIVE_DRAG = "excessive drag"
    REAMING_GREATER_THAN_2_HOURS = "reaming greater than 2 hours"
    WASHOUTS = "washouts"
    TIGHT_HOLE_OR_OVER_PULL = "tight hole or overPull"
    FAILED_INSPECTIONS_OR_FATIGUE_WEAR = "failed inspections or fatigue wear"
    MECHANICAL = "mechanical"
    DRILLING_GREATER_THAN_1000_FEET_DAY = "drilling greater than 1000 feet/day"
    DRILLING_GREATER_THAN_2000_FEET_DAY = "drilling greater than 2000 feet/day"
    DRILLING_LESS_THAN_20_FEET_DAY = "drilling less than 20 feet/day"
    TRIPS_GREATER_THAN_24_HOURS = "trips greater than 24 hours"
    EXCESSIVE_TIME_FOR_BHA_MAKEUP = "excessive time for BHA makeup"
    WAITING_ON_DECISIONS = "waiting on decisions"
    WAITING_ON_WEATHER = "waiting on weather"
    WAITING_ON_TOOLS = "waiting on tools"
    SLOUGHING_OR_PACKOFFS = "sloughing or packoffs"
    BALLOONING = "ballooning"
    FRACTURE_PROBLEMS = "fracture problems"
    UNSTABLE_ZONES = "unstable zones"
    FORMATION_INTEGRITY_TEST = "formation integrity test"
    LEAK_OFF_TEST = "leak-off test"
    TECTONICS = "tectonics"
    PORE_PRESSURE = "pore pressure"
    BREAKOUTS = "breakouts"
    BED_PARALLEL = "bed parallel"
    WELLBORE_STABILITY = "wellbore stability"
    EXCESSIVE_DOGLEGS = "excessive doglegs"
    SIDETRACK = "sidetrack"
    BHA_CHANGE_FOR_DIRECTIONAL = "BHA change for directional"
    WRONG_TOTAL_FLOW_AREA = "wrong total flow area"
    WELL_COLLISION_ACTUAL = "well collision - actual"
    WELL_COLLISION_TECHNICAL = "well collision - technical"
    GEOSTEERING = "geosteering"
    ABNORMAL_TENDENCY_CHANGES = "abnormal tendency changes"
    RESURVEYING = "resurveying"
    IN_FIELD_REFERENCING_IFR_ACTIONS = "in-field referencing (IFR) actions"
    BIT_OR_BHA_PERFORMANCE = "bit or BHA performance"
    DRILLING_OPTIMIZATION = "drilling optimization"
    BIT_BALLING = "bit balling"
    LOST_CONES_OR_BROKEN_CUTTERS = "lost cones or broken cutters"
    EXCESSIVE_BIT_WEAR_OR_GAUGE = "excessive bit wear or gauge"
    LOW_RATE_OF_BIT_PENETRATION = "low rate of bit penetration"
    HIGH_RATE_OF_BIT_PENETRATION = "high rate of bit penetration"
    DOWNHOLE_TOOL = "downhole tool"
    SURFACE_SYSTEM = "surface system"
    MOTOR_OR_ROTARY_STEERABLE_SYSTEM_FAILURE = "motor or rotary steerable system failure"
    TOPDRIVE_FAILURE = "topdrive failure"
    HOISTING_EQUIPMENT_FAILURE = "hoisting equipment failure"
    CIRCULATING_EQUIPMENT_FAILURE = "circulating equipment failure"
    ELECTRICAL_SYSTEM_FAILURE = "electrical system failure"
    BLOW_OUT_PREVENTER_EVENTS = "blow out preventer events"
    SURFACE_INSTRUMENTATION_PROBLEMS = "surface instrumentation problems"
    RIG_COMMUNICATIONS = "rig communications"
    COMPLETION_EQUIPMENT_FAILURE = "completion equipment failure"
    MISCELLANEOUS_RIG_EQUIPMENT = "miscellaneous rig equipment"
    TOOL_OR_EQUIPMENT_FAILURE = "tool or equipment failure"
    SQUEEZE_JOBS = "squeeze jobs"
    CASING_SURGE_LOSSES = "casing surge losses"
    STUCK_CASING_OR_COMPLETION = "stuck casing or completion"
    SHOE_FAILURES = "shoe failures"
    EARLY_CEMENT_SETUP = "early cement setup"
    CASING_COLLAPSE = "casing collapse"
    MILLING = "milling"
    EXCESSIVE_CASING_WEAR_OR_CUTTINGS = "excessive casing wear or cuttings"
    EXCESSIVE_FORMATION_DAMAGE_OR_SKIN = "excessive formation damage or skin"
    CASING_ROTATION_OR_RECIPROCATION_RQD = "casing rotation or reciprocation rqd"
    BROACHING = "broaching"
    COMPLETION_OR_CASING = "completion or casing"
    STRATIGRAPHY = "stratigraphy"
    FISHING = "fishing"
    JUNK_IN_HOLE = "junk in hole"
    DELAY_DUE_TO_POLITICAL_UNREST = "delay due to political unrest"
    RIG_MOVE = "rig move"
    GAS_HYDRATES = "gas hydrates"
    PENDING_ANALYSIS = "pending analysis"
    RISER_DISCONNECT = "riser disconnect"
    OTHER = "other"
    PERSONNEL = "personnel"
    ENVIRONMENTAL = "environmental"
    AUTOMOTIVE = "automotive"
    ASSET = "asset"
    INFORMATION = "information"
    TIME = "time"
    HSE = "HSE"
