from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PowerPerAreaUom(Enum):
    """
    :cvar BTU_IT_H_FT2: (BTU per hour) per square foot
    :cvar BTU_IT_S_FT2: BTU per second square foot
    :cvar CAL_TH_H_CM2: calorie per hour square centimetre
    :cvar HP_IN2: horsepower per square inch
    :cvar HP_HYD_IN2: hydraulic-horsepower per square inch
    :cvar K_W_CM2: kilowatt per square centimetre
    :cvar K_W_M2: kilowatt per square metre
    :cvar M_W_M2: milliwatt per square metre
    :cvar UCAL_TH_S_CM2: millionth of calorie per second square
        centimetre
    :cvar W_CM2: watt per square centimetre
    :cvar W_M2: watt per square metre
    :cvar W_MM2: watt per square millimetre
    """
    BTU_IT_H_FT2 = "Btu[IT]/(h.ft2)"
    BTU_IT_S_FT2 = "Btu[IT]/(s.ft2)"
    CAL_TH_H_CM2 = "cal[th]/(h.cm2)"
    HP_IN2 = "hp/in2"
    HP_HYD_IN2 = "hp[hyd]/in2"
    K_W_CM2 = "kW/cm2"
    K_W_M2 = "kW/m2"
    M_W_M2 = "mW/m2"
    UCAL_TH_S_CM2 = "ucal[th]/(s.cm2)"
    W_CM2 = "W/cm2"
    W_M2 = "W/m2"
    W_MM2 = "W/mm2"
