from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


@dataclass
class AbstractLogDataContext:
    """Defines a constraint against the data points in the log's channel.

    Each time the log is realized, only the data points satisfying this
    constraint are included.
    """
