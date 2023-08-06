from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class StimFluidSubtype(Enum):
    """
    Specifies the secondary qualifier for fluid type, e.g., acid, base,
    condensate, etc.
    """
    ACID = "acid"
    BASE = "base"
    CARBON_DIOXIDE = "carbon dioxide"
    CARBON_DIOXIDE_AND_NITROGEN = "carbon dioxide and nitrogen"
    CARBON_DIOXIDE_AND_WATER = "carbon dioxide and water"
    CONDENSATE = "condensate"
    CROSS_LINKED_GEL = "cross-linked gel"
    CRUDE_OIL = "crude oil"
    DIESEL = "diesel"
    FOAM = "foam"
    FRACTURING_OIL = "fracturing oil"
    FRESH_WATER = "fresh water"
    GELLED_ACID = "gelled acid"
    GELLED_CONDENSATE = "gelled condensate"
    GELLED_CRUDE = "gelled crude"
    GELLED_DIESEL = "gelled diesel"
    GELLED_OIL = "gelled oil"
    GELLED_SALT_WATER = "gelled salt water"
    HOT_CONDENSATE = "hot condensate"
    HOT_FRESH_WATER = "hot fresh water"
    HOT_OIL = "hot oil"
    HOT_SALT_WATER = "hot salt water"
    HYBRID = "hybrid"
    LINEAR_GEL = "linear gel"
    LIQUEFIED_PETROLEUM_GAS = "liquefied petroleum gas"
    NITROGEN = "nitrogen"
    OIL = "oil"
    OTHER = "other"
    PRODUCED_WATER = "produced water"
    SALT_WATER = "salt water"
    SLICK_WATER = "slick water"
