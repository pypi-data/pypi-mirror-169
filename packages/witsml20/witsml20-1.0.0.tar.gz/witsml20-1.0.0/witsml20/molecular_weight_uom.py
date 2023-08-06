from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class MolecularWeightUom(Enum):
    """
    :cvar G_MOL: gram per mole
    :cvar KG_MOL: kilogram per mole
    :cvar LBM_LBMOL: pound-mass per pound-mole
    """
    G_MOL = "g/mol"
    KG_MOL = "kg/mol"
    LBM_LBMOL = "lbm/lbmol"
