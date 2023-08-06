from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class MessageDigestType(Enum):
    """
    Specifies message digest types.

    :cvar MD5: See IETF RFC 1321 (http://www.ietf.org/rfc/rfc1321.txt)
    :cvar SHA1: See IETF RFC 3174 (http://www.ietf.org/rfc/rfc3174.txt).
    :cvar OTHER:
    """
    MD5 = "MD5"
    SHA1 = "SHA1"
    OTHER = "other"
