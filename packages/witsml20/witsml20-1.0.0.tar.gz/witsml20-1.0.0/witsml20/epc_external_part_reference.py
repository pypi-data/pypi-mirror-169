from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class EpcExternalPartReference(AbstractObject):
    """It defines a proxy for external part of the EPC package.

    It must be used at least for external HDF parts. Each
    EpcExternalPartReference represents a single operating system file

    :ivar filename:
    :ivar mime_type: IAMF registered, if one exists, or a free text
        field. Needs documentation on seismic especially. MIME type for
        HDF proxy is : application/x-hdf5 (by convention).
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    filename: Optional[str] = field(
        default=None,
        metadata={
            "name": "Filename",
            "type": "Element",
            "max_length": 2000,
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "max_length": 2000,
        }
    )
