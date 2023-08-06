from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from witsml20.abstract_object import AbstractObject
from witsml20.data_object_reference import DataObjectReference
from witsml20.extension_name_value import ExtensionNameValue
from witsml20.measured_depth_coord import MeasuredDepthCoord

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Attachment(AbstractObject):
    """A dedicated object used to attach digital supplemental data (for
    example, a graphic or PDF file) to another data object.

    The attachment is captured as a base 64 binary type.

    :ivar category: Used to tell what the object is when you have
        multiple attachments of the same file type. E.g., if you have
        attached a picture of cuttings on a specific depth, you can tag
        it with Category="CuttingsPicture".
    :ivar md: The along-hole measured depth represented by the
        attachment.
    :ivar param: Any extra numeric data. For this usage, the name
        attribute MUST be specified because it represents the meaning of
        the data. While the index attribute is mandatory, it is only
        significant if the same name repeats.
    :ivar md_bit: The along-hole measured depth of the bit.
    :ivar file_name: A file name associated with the attachment. Note
        this is NOT a file path and should contain a name only.
    :ivar file_type: The file type. This field SHOULD be a registered
        mime type as cataloged at http://www.iana.org/assignments/media-
        types/media-types.xhtml.
    :ivar content: The actual attachment content.
    :ivar object_reference: A reference to an object that is defined
        within the context of the specified wellbore.
    :ivar sub_object_reference: A reference to a sub-object that is
        defined within the context of the object referenced by
        objectReference. This should only refer to recurring components
        of a growing object. The content is the UID of the sub-object.
    :ivar wellbore:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"

    category: Optional[str] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "max_length": 64,
        }
    )
    md: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "Md",
            "type": "Element",
        }
    )
    param: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "Param",
            "type": "Element",
        }
    )
    md_bit: Optional[MeasuredDepthCoord] = field(
        default=None,
        metadata={
            "name": "MdBit",
            "type": "Element",
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Element",
            "max_length": 64,
        }
    )
    file_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileType",
            "type": "Element",
            "max_length": 64,
        }
    )
    content: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "Content",
            "type": "Element",
            "required": True,
            "format": "base64",
        }
    )
    object_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ObjectReference",
            "type": "Element",
        }
    )
    sub_object_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubObjectReference",
            "type": "Element",
            "max_length": 64,
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
