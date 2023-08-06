from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class EtpDataType(Enum):
    """
    Specifies the type of data contained in a channel to facilitate data
    transfer using the Energistics Transfer Protocol (ETP).

    :cvar BOOLEAN: True or false values.
    :cvar BYTES: Integer data value (nominally a one-byte value). The
        value must conform to the format of the xsd:dateTime data type
        (minInclusive=-128 and maxInclusive=127).
    :cvar DOUBLE: Double-precision floating-point value (nominally an
        8-byte value). The value must conform to the format of the
        xsd:double data type.
    :cvar FLOAT: Single-precision floating-point value (nominally a
        4-byte value). The value must conform to the format of the
        xsd:float data type
    :cvar INT: Integer data value (nominally a 4-byte value). The value
        must conform to the format of the xsd:int data type.
    :cvar LONG: Long integer data value (nominally an 8-byte value). The
        value must conform to the format of the xsd:long data type.
    :cvar NULL: No value or the value is null.
    :cvar STRING: Character string data. The value must conform to the
        format of the xsd:string data type. The maximum length of a
        value is determined by individual servers.
    :cvar VECTOR: An array of doubles.
    """
    BOOLEAN = "boolean"
    BYTES = "bytes"
    DOUBLE = "double"
    FLOAT = "float"
    INT = "int"
    LONG = "long"
    NULL = "null"
    STRING = "string"
    VECTOR = "vector"
