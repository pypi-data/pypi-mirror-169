from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.area_measure import AreaMeasure
from witsml20.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StnTrajMatrixCov:
    """
    Captures validation information for a covariance matrix.

    :ivar variance_nn: Covariance north north.
    :ivar variance_ne: Crossvariance north east.
    :ivar variance_nvert: Crossvariance north vertical.
    :ivar variance_ee: Covariance east east.
    :ivar variance_evert: Crossvariance east vertical.
    :ivar variance_vert_vert: Covariance vertical vertical.
    :ivar bias_n: Bias north.
    :ivar bias_e: Bias east.
    :ivar bias_vert: Bias vertical. The coordinate system is set up in a
        right-handed configuration, which makes the vertical direction
        increasing (i.e., positive) downwards.
    """
    variance_nn: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceNN",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    variance_ne: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceNE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    variance_nvert: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceNVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    variance_ee: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceEE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    variance_evert: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceEVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    variance_vert_vert: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "VarianceVertVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bias_n: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BiasN",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bias_e: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BiasE",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    bias_vert: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "BiasVert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
