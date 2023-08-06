from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class HeatFlowRateUom(Enum):
    """
    :cvar VALUE_1_E6_BTU_IT_H: million BTU per hour
    :cvar BTU_IT_H: BTU per hour
    :cvar BTU_IT_MIN: BTU per minute
    :cvar BTU_IT_S: BTU per second
    :cvar CAL_TH_H: calorie per hour
    :cvar EJ_A: exajoule per julian-year
    :cvar ERG_A: erg per julian-year
    :cvar GW: gigawatt
    :cvar J_S: joule per second
    :cvar KCAL_TH_H: thousand calorie per hour
    :cvar K_W: kilowatt
    :cvar LBF_FT_MIN: foot pound-force per minute
    :cvar LBF_FT_S: foot pound-force per second
    :cvar MJ_A: megajoule per julian-year
    :cvar MW: megawatt
    :cvar M_W_1: milliwatt
    :cvar N_W: nanowatt
    :cvar QUAD_A: quad per julian-year
    :cvar TJ_A: terajoule per julian-year
    :cvar TW: terawatt
    :cvar UCAL_TH_S: millionth of calorie per second
    :cvar U_W: microwatt
    :cvar W: watt
    """
    VALUE_1_E6_BTU_IT_H = "1E6 Btu[IT]/h"
    BTU_IT_H = "Btu[IT]/h"
    BTU_IT_MIN = "Btu[IT]/min"
    BTU_IT_S = "Btu[IT]/s"
    CAL_TH_H = "cal[th]/h"
    EJ_A = "EJ/a"
    ERG_A = "erg/a"
    GW = "GW"
    J_S = "J/s"
    KCAL_TH_H = "kcal[th]/h"
    K_W = "kW"
    LBF_FT_MIN = "lbf.ft/min"
    LBF_FT_S = "lbf.ft/s"
    MJ_A = "MJ/a"
    MW = "MW"
    M_W_1 = "mW"
    N_W = "nW"
    QUAD_A = "quad/a"
    TJ_A = "TJ/a"
    TW = "TW"
    UCAL_TH_S = "ucal[th]/s"
    U_W = "uW"
    W = "W"
