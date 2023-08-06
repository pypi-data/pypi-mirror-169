from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudLosses:
    """
    Operations Mud Losses Schema.Captures volumes of mud lost for specific
    activities or onsite locations and total volumes for surface and down hole.

    :ivar vol_lost_shaker_surf: Volume of mud lost at shakers (at
        surface).
    :ivar vol_lost_mud_cleaner_surf: Volume of mud lost in mud cleaning
        equipment (at surface).
    :ivar vol_lost_pits_surf: Volume of mud lost in pit room (at
        surface).
    :ivar vol_lost_tripping_surf: Volume of mud lost while tripping (at
        surface).
    :ivar vol_lost_other_surf: Surface volume lost other location.
    :ivar vol_tot_mud_lost_surf: Total volume of mud lost at surface.
    :ivar vol_lost_circ_hole: Mud volume lost downhole while
        circulating.
    :ivar vol_lost_csg_hole: Mud volume lost downhole while running
        casing.
    :ivar vol_lost_cmt_hole: Mud volume lost downhole while cementing.
    :ivar vol_lost_bhd_csg_hole: Mud volume lost downhole behind casing.
    :ivar vol_lost_abandon_hole: Mud volume lost downhole during
        abandonment.
    :ivar vol_lost_other_hole: Mud volume lost downhole from other
        location.
    :ivar vol_tot_mud_lost_hole: Total volume of mud lost downhole.
    """
    vol_lost_shaker_surf: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostShakerSurf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_mud_cleaner_surf: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostMudCleanerSurf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_pits_surf: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostPitsSurf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_tripping_surf: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostTrippingSurf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_other_surf: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostOtherSurf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_tot_mud_lost_surf: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolTotMudLostSurf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_circ_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostCircHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_csg_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostCsgHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_cmt_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostCmtHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_bhd_csg_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostBhdCsgHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_abandon_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostAbandonHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_lost_other_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolLostOtherHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    vol_tot_mud_lost_hole: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolTotMudLostHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
