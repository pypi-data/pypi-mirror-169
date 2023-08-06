from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Personnel:
    """Operations Personnel Component Schema.

    List each company on the rig at the time of the report and key
    information about each company, for example, name, type of service,
    and number of personnel.

    :ivar company: Name of the company.
    :ivar type_service: Service provided by the company.
    :ivar num_people: Number of people on board for that company.
    :ivar total_time: Total time worked by the company (commonly in
        hours).
    :ivar extension_name_value: Extensions to the schema based on a
        name-value construct.
    :ivar uid: Unique identifier for this instance of Personnel.
    """
    company: Optional[str] = field(
        default=None,
        metadata={
            "name": "Company",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    type_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "TypeService",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "max_length": 64,
        }
    )
    num_people: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumPeople",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
        }
    )
    total_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "TotalTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
