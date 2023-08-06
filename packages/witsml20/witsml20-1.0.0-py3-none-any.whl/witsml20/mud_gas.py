from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.gas_in_mud import GasInMud
from witsml20.gas_peak import GasPeak

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class MudGas:
    """
    Information on gas in the mud and gas peak.
    """
    gas_in_mud: Optional[GasInMud] = field(
        default=None,
        metadata={
            "name": "GasInMud",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    gas_peak: List[GasPeak] = field(
        default_factory=list,
        metadata={
            "name": "GasPeak",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
