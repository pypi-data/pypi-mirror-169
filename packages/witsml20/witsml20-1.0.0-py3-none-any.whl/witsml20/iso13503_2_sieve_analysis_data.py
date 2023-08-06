from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml20.mass_per_mass_measure import MassPerMassMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class Iso135032SieveAnalysisData:
    """Proppant properties on percent retained and sieve number.

    Data from this ISO anaylsis.

    :ivar percent_retained: The percentage of mass retained in the
        sieve.
    :ivar sieve_number: ASTM US Standard mesh opening size used in the
        sieve analysis test.  To indicate "Pan",  use "0".
    :ivar uid: Unique identifier for this instance of
        ISO13503_2SieveAnalysisData.
    """
    class Meta:
        name = "ISO13503_2SieveAnalysisData"

    percent_retained: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "PercentRetained",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
        }
    )
    sieve_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "SieveNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/witsmlv2",
            "required": True,
            "min_inclusive": 0,
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
