from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_string_array import AbstractStringArray
from witsml20.external_dataset import ExternalDataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringExternalArray(AbstractStringArray):
    """Used to store explicit string values, i.e., values that are not double,
    boolean or integers.

    The datatype of the values will be identified by means of the HDF5
    API.

    :ivar values: Reference to HDF5 array of integer or double
    """
    values: Optional[ExternalDataset] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
