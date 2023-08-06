from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from witsml20.iscwsa_name_and_description import IscwsaNameAndDescription
from witsml20.iscwsa_nomenclature_constant import IscwsaNomenclatureConstant

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaNomenclature:
    """
    A nomenclature for the description of error terms.
    """
    parameter: List[IscwsaNameAndDescription] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    function: List[IscwsaNameAndDescription] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    constant: List[IscwsaNomenclatureConstant] = field(
        default_factory=list,
        metadata={
            "name": "Constant",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
