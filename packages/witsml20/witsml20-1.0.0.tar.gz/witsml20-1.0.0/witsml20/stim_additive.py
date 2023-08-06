from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.stim_additive_kind import StimAdditiveKind
from witsml20.stim_material import StimMaterial

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class StimAdditive(StimMaterial):
    """
    Provides generic attributes associated with defining an additive used for
    stimulation.

    :ivar additive_kind: Additive type or function from the enumeration
        'StimAdditiveKind'.
    :ivar type: The type of additive that is used, which can represent a
        suppliers description or type of AdditiveKind.  For example, 5%
        HCl could be the type when AdditiveKind=acid.
    :ivar supplier_code: A code used to identify the supplier of the
        additive.
    """
    additive_kind: Optional[StimAdditiveKind] = field(
        default=None,
        metadata={
            "name": "AdditiveKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
    supplier_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
