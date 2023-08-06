from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_boolean_array import AbstractBooleanArray
from witsml20.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerArrayFromBooleanMaskArray(AbstractIntegerArray):
    """
    One-dimensional array of integer values obtained from the true elements of
    the Boolean mask.

    :ivar total_index_count: Total number of integer elements in the
        array. This number is different from the number of Boolean mask
        values used to represent the array.
    :ivar mask: Boolean mask. A true element indicates that the index is
        included on the list of integer values.
    """
    total_index_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TotalIndexCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    mask: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "Mask",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
