from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Citation:
    """
    An ISO 19115 EIP-derived set of metadata attached to all specializations of
    AbstractObject to ensure the traceability of each individual independent
    (top level) element.

    :ivar title: One line description/name of the object. This is the
        equivalent in ISO 19115 of CI_Citation.title Legacy DCGroup -
        title
    :ivar originator: Name (or other human-readable identifier) of the
        person who initially originated the object or document in the
        source application. If that information is not available, then
        this is the user who created the format file. The originator
        remains the same as the object is subsequently edited. This is
        the equivalent in ISO 19115 to the CI_Individual.name or the
        CI_Organization.name of the citedResponsibleParty whose role is
        "originator". Legacy DCGroup - author
    :ivar creation: Date and time the document was created in the source
        application or, if that information is not available, when it
        was saved to the file. This is the equivalent of the ISO 19115
        CI_Date where the CI_DateTypeCode = "creation" Format: YYYY-MM-
        DDThh:mm:ssZ[+/-]hh:mm Legacy DCGroup - created
    :ivar format: Software or service that was used to originate the
        object and the file format created. Must be human and machine
        readable and unambiguously identify the software by including
        the company name, software name and software version. This is
        the equivalent in ISO 19115 to the distributionFormat.MD_Format.
        The ISO format for this is
        [vendor:applicationName]/fileExtension where the application
        name includes the version number of the application. SIG
        Implementation Notes - Legacy DCGroup from v1.1 - publisher -
        fileExtension is not relevant and will be ignored if present. -
        vendor and applicationName are mandatory.
    :ivar editor: Name (or other human-readable identifier) of the last
        person who updated the object. This is the equivalent in ISO
        19115 to the CI_Individual.name or the CI_Organization.name of
        the citedResponsibleParty whose role is "editor". Legacy DCGroup
        - contributor
    :ivar last_update: Date and time the document was last modified in
        the source application or, if that information is not available,
        when it was last saved to the RESQML format file. This is the
        equivalent of the ISO 19115 CI_Date where the CI_DateTypeCode =
        "lastUpdate" Format: YYYY-MM-DDThh:mm:ssZ[+/-]hh:mm Legacy
        DCGroup - modified
    :ivar version_string:
    :ivar description: User descriptive comments about the object.
        Intended for end-user use (human readable); not necessarily
        meant to be used by software. This is the equivalent of the ISO
        19115 abstract.CharacterString Legacy DCGroup - description
    :ivar descriptive_keywords: Key words to describe the activity, for
        example, history match or volumetric calculations, relevant to
        this object. Intended to be used in a search function by
        software. This is the equivalent in ISO 19115 of
        descriptiveKeywords.MD_Keywords Legacy DCGroup - subject
    """
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    originator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Originator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    creation: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Creation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    editor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Editor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    last_update: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastUpdate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    version_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    descriptive_keywords: Optional[str] = field(
        default=None,
        metadata={
            "name": "DescriptiveKeywords",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
