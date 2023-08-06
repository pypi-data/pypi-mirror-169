from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.depth_reg_log_rect import DepthRegLogRect
from witsml20.depth_reg_log_section import DepthRegLogSection
from witsml20.depth_reg_rectangle import DepthRegRectangle
from witsml20.digital_storage_measure import DigitalStorageMeasure
from witsml20.file_name_type import FileNameType
from witsml20.message_digest_type import MessageDigestType
from witsml20.mime_type import MimeType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class DepthRegImage(AbstractObject):
    """
    Information about the composition, layout, and depth registration of a
    digital image of a well log, typically a scanned image of a paper well log
    document.

    :ivar file_name_type: Mimetype of image file content.
    :ivar mimetype: Mimetype of image file content.
    :ivar file_name: Reference to the file containing the image content.
    :ivar file_size: Size of image file, in bytes.
    :ivar checksum: Image file checksum.
    :ivar image_pixel_width: Image file width, in pixels.
    :ivar image_pixel_height: Image file height, in pixels.
    :ivar version: File version.
    :ivar image_boundary: The bounding rectangle of the image
    :ivar header_section: Log header information extracted from the well
        log image header section. Also contains X, Y coordinates and
        positional data with respect to the header section location
        within the log image file.
    :ivar log_section: Provides log name, log type, curve scale and
        other information about each log section of the image file. Most
        importantly, this section contains the depth registration
        elements (CalibrationPoint) necessary for depth calibrating well
        log sections.
    :ivar alternate_section: Provides a positional reference for
        sections of the image file not included in other elements of
        this object.
    :ivar wellbore:
    :ivar uid: Unique identifier for the registration image.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    file_name_type: Optional[FileNameType] = field(
        default=None,
        metadata={
            "name": "FileNameType",
            "type": "Element",
        }
    )
    mimetype: Optional[MimeType] = field(
        default=None,
        metadata={
            "name": "Mimetype",
            "type": "Element",
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "required": True,
            "max_length": 64,
        }
    )
    file_size: Optional[DigitalStorageMeasure] = field(
        default=None,
        metadata={
            "name": "FileSize",
            "type": "Element",
        }
    )
    checksum: Optional[MessageDigestType] = field(
        default=None,
        metadata={
            "name": "Checksum",
            "type": "Element",
        }
    )
    image_pixel_width: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImagePixelWidth",
            "type": "Element",
            "min_inclusive": 0,
        }
    )
    image_pixel_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "ImagePixelHeight",
            "type": "Element",
            "min_inclusive": 0,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "max_length": 64,
        }
    )
    image_boundary: Optional[DepthRegRectangle] = field(
        default=None,
        metadata={
            "name": "ImageBoundary",
            "type": "Element",
            "required": True,
        }
    )
    header_section: Optional[DepthRegLogRect] = field(
        default=None,
        metadata={
            "name": "HeaderSection",
            "type": "Element",
        }
    )
    log_section: List[DepthRegLogSection] = field(
        default_factory=list,
        metadata={
            "name": "LogSection",
            "type": "Element",
        }
    )
    alternate_section: List[DepthRegLogRect] = field(
        default_factory=list,
        metadata={
            "name": "AlternateSection",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
