from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.anchor_state import AnchorState
from witsml20.force_measure import ForceMeasure
from witsml20.length_measure import LengthMeasure
from witsml20.plane_angle_measure import PlaneAngleMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class RigResponse:
    """
    Operations Rig Response Component Schema.

    :ivar rig_heading: Direction, relative to true north, to which the
        rig is facing.
    :ivar rig_heave: Maximum amplitude of the vertical motion of the
        rig.
    :ivar rig_pitch_angle: Measure of the fore-aft rotational movement
        of the rig due to the combined effects of wind and waves;
        measured as the angle from horizontal.
    :ivar rig_roll_angle: Measure of the side-to-side rotational
        movement of the rig due to the combined effects of wind and
        waves; measured as the angle from vertical.
    :ivar riser_angle: Angle of the marine riser with the vertical.
    :ivar riser_direction: Direction of the marine riser.
    :ivar riser_tension: Tension of the marine riser.
    :ivar variable_deck_load: Current temporary load on the rig deck.
    :ivar total_deck_load: Total deck load.
    :ivar guide_base_angle: Direction of the guide base.
    :ivar ball_joint_angle: Angle between the riser and the blowout
        preventer (BOP) at the flex joint.
    :ivar ball_joint_direction: Direction of the ball joint.
    :ivar offset_rig: Horizontal displacement of the rig relative to the
        wellhead.
    :ivar load_leg1: Load carried by one leg of a jackup rig.
    :ivar load_leg2: Load carried by the second leg of a jackup rig.
    :ivar load_leg3: Load carried by the third leg of a jackup rig.
    :ivar load_leg4: Load carried by the fourth leg of a jackup rig.
    :ivar penetration_leg1: Penetration of the first leg into the
        seabed.
    :ivar penetration_leg2: Penetration of the second leg into the
        seabed.
    :ivar penetration_leg3: Penetration of the third leg into the
        seabed.
    :ivar penetration_leg4: Penetration of the fourth leg into the
        seabed.
    :ivar disp_rig: Vessel displacement (in water).
    :ivar mean_draft: Mean draft at mid-section of the vessel.
    :ivar anchor_state:
    """
    rig_heading: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "RigHeading",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rig_heave: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "RigHeave",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rig_pitch_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "RigPitchAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    rig_roll_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "RigRollAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    riser_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "RiserAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    riser_direction: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "RiserDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    riser_tension: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "RiserTension",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    variable_deck_load: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "VariableDeckLoad",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    total_deck_load: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "TotalDeckLoad",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    guide_base_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "GuideBaseAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ball_joint_angle: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "BallJointAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    ball_joint_direction: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "BallJointDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    offset_rig: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OffsetRig",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    load_leg1: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "LoadLeg1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    load_leg2: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "LoadLeg2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    load_leg3: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "LoadLeg3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    load_leg4: Optional[ForceMeasure] = field(
        default=None,
        metadata={
            "name": "LoadLeg4",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    penetration_leg1: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PenetrationLeg1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    penetration_leg2: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PenetrationLeg2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    penetration_leg3: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PenetrationLeg3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    penetration_leg4: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "PenetrationLeg4",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    disp_rig: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "DispRig",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    mean_draft: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MeanDraft",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    anchor_state: List[AnchorState] = field(
        default_factory=list,
        metadata={
            "name": "AnchorState",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
