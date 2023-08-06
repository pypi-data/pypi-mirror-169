from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ThermalConductivityUom(Enum):
    """
    :cvar BTU_IT_H_FT_DELTA_F: BTU per hour foot delta Fahrenheit
    :cvar CAL_TH_H_CM_DELTA_C: calorie per hour centimetre delta Celsius
    :cvar CAL_TH_S_CM_DELTA_C: calorie per second centimetre delta
        Celsius
    :cvar KCAL_TH_H_M_DELTA_C: thousand calorie per hour metre delta
        Celsius
    :cvar W_M_DELTA_K: watt per metre delta kelvin
    """
    BTU_IT_H_FT_DELTA_F = "Btu[IT]/(h.ft.deltaF)"
    CAL_TH_H_CM_DELTA_C = "cal[th]/(h.cm.deltaC)"
    CAL_TH_S_CM_DELTA_C = "cal[th]/(s.cm.deltaC)"
    KCAL_TH_H_M_DELTA_C = "kcal[th]/(h.m.deltaC)"
    W_M_DELTA_K = "W/(m.deltaK)"
