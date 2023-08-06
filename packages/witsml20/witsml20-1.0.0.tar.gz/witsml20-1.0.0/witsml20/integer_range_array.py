from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerRangeArray(AbstractIntegerArray):
    """Defines an array as a range of integers.

    The range is defined by an initial value and a count defining the
    size of the range.

    :ivar count: Size of the array.
    :ivar value: Start value for the range. End value is start+count-1.
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
