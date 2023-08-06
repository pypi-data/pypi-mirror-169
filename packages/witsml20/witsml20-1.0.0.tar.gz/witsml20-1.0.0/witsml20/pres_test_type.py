from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class PresTestType(Enum):
    """
    Specifies the types of pressure test(s) conducted during a drilling report
    period.

    :cvar LEAK_OFF_TEST: A leakoff test (LOT) is usually conducted
        immediately after drilling below a new casing shoe. The test
        indicates the strength of the wellbore at the casing seat,
        typically considered one of the weakest points in any interval.
        The data gathered during the LOT is used to prevent lost
        circulations while drilling. During the test, the well is shut
        in and fluid is pumped into the wellbore gradually to increase
        the pressure on the formation.
    :cvar FORMATION_INTEGRITY_TEST: To avoid breaking down the
        formation, many operators perform a formation integrity test
        (FIT) at the casing seat to determine if the wellbore will
        tolerate the maximum mud weight anticipated while drilling the
        interval. If the casing seat holds pressure that is equivalent
        to the prescribed mud density, the test is considered successful
        and drilling resumes.
    """
    LEAK_OFF_TEST = "leak off test"
    FORMATION_INTEGRITY_TEST = "formation integrity test"
