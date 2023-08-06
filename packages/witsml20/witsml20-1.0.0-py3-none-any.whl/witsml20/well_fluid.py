from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellFluid(Enum):
    """
    Specifies values for the type of fluid being produced from or injected into
    a well facility.

    :cvar AIR: This is generally an injected fluid.
    :cvar CONDENSATE: Liquid hydrocarbons produced with natural gas that
        are separated from the gas by cooling and various other means.
        Condensate generally has an API gravity of 50 degrees to 120
        degrees and is water white, straw, or bluish in color. It is the
        liquid recovery from a well classified as a gas well. It is
        generally dissolved in the gaseous state under reservoir
        conditions but separates as a liquid either in passing up the
        hole or at the surface. These hydrocarbons, from associated and
        non-associated gas well gas, normally are recovered from lease
        separators or field facilities by mechanical separation.
    :cvar DRY: The well facility is classified as a dry well. It has not
        been, nor will it be used to produce or inject any fluids.
    :cvar GAS: The well is classified as a gas well, producing or
        injecting a hydrocarbon gas. The gas is generally methane but
        may have a mixture of other gases also.
    :cvar GAS_WATER: The well facility is classified as producing both
        gas and water. USe this classification when the produced stream
        flow is a mixture of gas and water. When a facility produces gas
        and water in separate streams, classify it twice, as gas and as
        water.
    :cvar NON_HC_GAS: The well produces or injects non-hydrocarbon
        gases. Typical other gases would be helium and carbon dioxide.
    :cvar NON_HC_GAS_CO2: Carbon dioxide gas.
    :cvar OIL: The liquid hydrocarbon generally referred to as crude
        oil.
    :cvar OIL_GAS: The well facility is classified as producing both gas
        and oil. Use this classification when the produced stream flow
        is a mixture of oil and gas. When a facility produces oil and
        gas in separate streams, classify it twice, as oil and as gas.
    :cvar OIL_WATER: The well facility is classified as producing both
        oil and water. Use this classification when the produced stream
        flow is a mixture of oil and water. When a facility produces oil
        and water in separate streams, classify it twice, as oil and as
        water.
    :cvar STEAM: The gaseous state of water. This is generally an
        injected fluid, but it is possible that some hydrothermal wells
        produce steam.
    :cvar WATER: The well is classified as a water well without
        distinguishing between brine or fresh water.
    :cvar WATER_BRINE: The well facility is classified as producing or
        injecting salt water.
    :cvar WATER_FRESH_WATER: The well facility is classified as
        producing fresh water that is capable of use for drinking or
        crop irrigation.
    """
    AIR = "air"
    CONDENSATE = "condensate"
    DRY = "dry"
    GAS = "gas"
    GAS_WATER = "gas-water"
    NON_HC_GAS = "non HC gas"
    NON_HC_GAS_CO2 = "non HC gas -- CO2"
    OIL = "oil"
    OIL_GAS = "oil-gas"
    OIL_WATER = "oil-water"
    STEAM = "steam"
    WATER = "water"
    WATER_BRINE = "water -- brine"
    WATER_FRESH_WATER = "water -- fresh water"
