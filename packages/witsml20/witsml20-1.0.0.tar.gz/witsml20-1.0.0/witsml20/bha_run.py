from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.angle_per_length_measure import AnglePerLengthMeasure
from witsml20.bha_status import BhaStatus
from witsml20.data_object_reference import DataObjectReference
from witsml20.drilling_params import DrillingParams

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class BhaRun(AbstractObject):
    """The object used to capture information about one run of the drill string
    into and out of the hole.

    The drill string configuration is described in the Tubular object.
    That is, one drill string configuration may be used for many runs.

    :ivar dtim_start: Date and time that activities for this run
        started.
    :ivar dtim_stop: Date and time that activities for this run stopped.
    :ivar dtim_start_drilling: Start on bottom: date and time.
    :ivar dtim_stop_drilling: Stop off bottom: date and time.
    :ivar plan_dogleg: Planned dogleg severity.
    :ivar act_dogleg: Actual dogleg severity.
    :ivar act_dogleg_mx: Actual dogleg severity: maximum.
    :ivar status_bha: Bottomhole assembly status.
    :ivar num_bit_run: Bit run number.
    :ivar num_string_run: The BHA (drilling string) run number.
    :ivar reason_trip: Reason for a trip.
    :ivar objective_bha: Objective of the bottomhole assembly.
    :ivar drilling_params:
    :ivar wellbore:
    :ivar tubular:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_stop: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStop",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_start_drilling: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStartDrilling",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_stop_drilling: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStopDrilling",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    plan_dogleg: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "PlanDogleg",
            "type": "Element",
        }
    )
    act_dogleg: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "ActDogleg",
            "type": "Element",
        }
    )
    act_dogleg_mx: Optional[AnglePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "ActDoglegMx",
            "type": "Element",
        }
    )
    status_bha: Optional[BhaStatus] = field(
        default=None,
        metadata={
            "name": "StatusBha",
            "type": "Element",
        }
    )
    num_bit_run: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumBitRun",
            "type": "Element",
        }
    )
    num_string_run: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumStringRun",
            "type": "Element",
        }
    )
    reason_trip: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReasonTrip",
            "type": "Element",
            "max_length": 2000,
        }
    )
    objective_bha: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectiveBha",
            "type": "Element",
            "max_length": 2000,
        }
    )
    drilling_params: List[DrillingParams] = field(
        default_factory=list,
        metadata={
            "name": "DrillingParams",
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
    tubular: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Tubular",
            "type": "Element",
        }
    )
