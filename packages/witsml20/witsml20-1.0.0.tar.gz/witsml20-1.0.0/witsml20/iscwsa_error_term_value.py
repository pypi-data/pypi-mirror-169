from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.error_propagation_mode import ErrorPropagationMode
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.measure_or_quantity import MeasureOrQuantity

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class IscwsaErrorTermValue:
    """
    The instantiation of an error term in an error model.The content of this
    element (a number) is the variance scaling factor of the term in the model.

    :ivar term: A pointer to the errorTerm represented by this value.
        This term must exist in the toolErrorTermSet referenced by the
        parent of this node. The same term may only be referenced once
        in the model.
    :ivar prop: The propagation mode for this term in this model.
    :ivar bias: The mean or expected value of the variance.
    :ivar comment: A textual comment about this error term value.
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar value:
    :ivar uid: Unique identifier for this instance of
        IscwsaErrorTermValue.
    """
    term: Optional[str] = field(
        default=None,
        metadata={
            "name": "Term",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    prop: Optional[ErrorPropagationMode] = field(
        default=None,
        metadata={
            "name": "Prop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    bias: Optional[float] = field(
        default=None,
        metadata={
            "name": "Bias",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 2000,
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    value: Optional[MeasureOrQuantity] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
