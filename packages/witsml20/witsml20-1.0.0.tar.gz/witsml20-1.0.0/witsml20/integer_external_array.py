from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_integer_array import AbstractIntegerArray
from witsml20.external_dataset import ExternalDataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class IntegerExternalArray(AbstractIntegerArray):
    """Array of integer values provided explicitly by an HDF5 dataset.

    The null value must be  explicitly provided in the NullValue
    attribute of this class.

    :ivar null_value:
    :ivar values: Reference to an HDF5 array of integers or doubles.
    """
    null_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "NullValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: Optional[ExternalDataset] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
