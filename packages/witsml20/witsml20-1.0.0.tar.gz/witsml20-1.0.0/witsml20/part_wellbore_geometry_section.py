from __future__ import annotations
from dataclasses import dataclass
from witsml20.wellbore_geometry_section import WellboreGeometrySection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class PartWellboreGeometrySection(WellboreGeometrySection):
    """
    Wrapper for sending individual sections using ETP.
    """
    class Meta:
        name = "part_WellboreGeometrySection"
        namespace = "http://www.energistics.org/energyml/data/witsmlv2"
