from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.dimensionless_measure import DimensionlessMeasure
from witsml20.force_per_volume_measure import ForcePerVolumeMeasure
from witsml20.measured_depth_coord import MeasuredDepthCoord
from witsml20.pressure_measure import PressureMeasure
from witsml20.stim_flow_path_type import StimFlowPathType
from witsml20.stim_tubular import StimTubular

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimFlowPath:
    """
    The fluid flow path for used when pumping a stage in a stimulation job.

    :ivar avg_pmax_pac_pres: PMax prediction allows the tool assembly to
        be designed with expected pressures. It determines maximum
        allowable surface pressure and is typically calculated as a
        single number by which the pressure relief valves are set. This
        variable is the average of all the pmax pressures calculated for
        this flow path.
    :ivar friction_factor_open_hole: The friction factor used to compute
        openhole pressure loss.
    :ivar avg_pmax_weaklink_pres: Average allowable pressure for the
        zone of interest with respect to the bottomhole assembly during
        the stimulation services.
    :ivar break_down_pres: The pressure at which the formation broke.
    :ivar bridge_plug_md: The measured depth of a bridge plug.
    :ivar fracture_gradient: The formation fracture gradient for this
        treatment interval.
    :ivar kind: The type of flow path.
    :ivar max_pmax_pac_pres: PMax prediction allows the tool assembly to
        be designed with expected pressures. It determines maximum
        allowable surface pressure and is typically calculated as a
        single number by which the pressure relief valves are set. This
        variable is the maximum of all the pmax pressures calculated for
        this flow path.
    :ivar max_pmax_weaklink_pres: Maximum allowable pressure for the
        zone of interest with respect to the bottomhole assembly during
        the stimulation services.
    :ivar packer_md: The measured depth of a packer.
    :ivar friction_factor_pipe: The friction factor for the pipe,
        tubing, and/or casing.
    :ivar tubing_bottom_md: The maximum measured depth of the tubing
        used for treatment of a stage.
    :ivar tubular:
    """
    avg_pmax_pac_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPmaxPacPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    friction_factor_open_hole: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "FrictionFactorOpenHole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    avg_pmax_weaklink_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AvgPmaxWeaklinkPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    break_down_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "BreakDownPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bridge_plug_md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "BridgePlugMD",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    fracture_gradient: Optional[ForcePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FractureGradient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    kind: Optional[StimFlowPathType] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_pmax_pac_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPmaxPacPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    max_pmax_weaklink_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "MaxPmaxWeaklinkPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    packer_md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "PackerMD",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    friction_factor_pipe: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "FrictionFactorPipe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubing_bottom_md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "TubingBottomMD",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    tubular: List[StimTubular] = field(
        default_factory=list,
        metadata={
            "name": "Tubular",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
