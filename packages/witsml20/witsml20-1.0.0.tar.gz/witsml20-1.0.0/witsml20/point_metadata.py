from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.etp_data_type import EtpDataType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PointMetadata:
    """Used to declare that data points in a specific WITSML log channel may
    contain value attributes (e.g., quality identifiers).

    This declaration is independent from the possibility that ETP may
    have sent ValueAttributes in real time. If an instance of
    PointMetadata is present for a Channel, then the value for that
    point is represented as an array in the bulk data string.

    :ivar name: The name of the point metadata.
    :ivar etp_data_type: The underlying ETP data type of the point
        metadata.
    :ivar description: Free format description of the point metadata.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    etp_data_type: Optional[EtpDataType] = field(
        default=None,
        metadata={
            "name": "EtpDataType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "max_length": 2000,
        }
    )
