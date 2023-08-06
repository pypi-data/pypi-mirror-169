from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.channel_status import ChannelStatus
from witsml20.data_object_reference import DataObjectReference
from witsml20.md_interval import MdInterval
from witsml20.show_evaluation_interval import ShowEvaluationInterval

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class ShowEvaluation(AbstractObject):
    """A container object for zero or more ShowEvaluationInterval objects.

    The container references a specific wellbore, a depth interval, a
    growing object status, and a collection of show evaluation
    intervals. In a similar way to the InterpretedGeology, these are
    manually entered by the wellsite geologist or mud logger as an
    interpretation of the hydrocarbon show along the wellbore, based on
    the raw readings from one or more show analyses of individual show
    tests on cuttings samples.

    :ivar md_interval: [maintained by the server] The interval that
        contains the minimum and maximum measured depths for all show
        intervals in this show evaluation.
    :ivar growing_status: Describes the growing status of the show
        evaluation intervals. Valid values: active, inactive or closed.
    :ivar evaluated_interval_show:
    :ivar wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
        }
    )
    growing_status: Optional[ChannelStatus] = field(
        default=None,
        metadata={
            "name": "GrowingStatus",
            "type": "Element",
            "required": True,
        }
    )
    evaluated_interval_show: List[ShowEvaluationInterval] = field(
        default_factory=list,
        metadata={
            "name": "EvaluatedIntervalShow",
            "type": "Element",
        }
    )
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "required": True,
        }
    )
