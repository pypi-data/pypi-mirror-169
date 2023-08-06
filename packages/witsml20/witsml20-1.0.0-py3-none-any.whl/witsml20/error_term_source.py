from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ErrorTermSource(Enum):
    """
    Specifies the codes for the various classes of error sources.

    :cvar SENSOR: Errors arising from sensors in the survey tool.
    :cvar AZIMUTH_REFERENCE: Errors arising from the adoption of a
        particular reference azimuth.
    :cvar MAGNETIC: Errors arising from external magnetic field
        influences.
    :cvar ALIGNMENT: Errors arising from the misalignment of the tool
        relative to the borehole.
    :cvar MISALIGNMENT: Specifies the codes for the various classes of
        error source.
    :cvar DEPTH: Errors arising from the measurement of depth.
    :cvar REFERENCE: Errors arising from the measurement of depth.
    """
    SENSOR = "sensor"
    AZIMUTH_REFERENCE = "azimuth reference"
    MAGNETIC = "magnetic"
    ALIGNMENT = "alignment"
    MISALIGNMENT = "misalignment"
    DEPTH = "depth"
    REFERENCE = "reference"
