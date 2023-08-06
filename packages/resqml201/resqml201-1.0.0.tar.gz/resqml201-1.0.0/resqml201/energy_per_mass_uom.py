from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyPerMassUom(Enum):
    """
    :cvar BTU_IT_LBM: BTU per pound-mass
    :cvar CAL_TH_G: calorie per gram
    :cvar CAL_TH_KG: calorie per kilogram
    :cvar CAL_TH_LBM: calorie per pound-mass
    :cvar ERG_G: erg per gram
    :cvar ERG_KG: erg per kilogram
    :cvar HP_H_LBM: horsepower hour per pound-mass
    :cvar J_G: joule per gram
    :cvar J_KG: joule per kilogram
    :cvar KCAL_TH_G: thousand calorie per gram
    :cvar KCAL_TH_KG: thousand calorie per kilogram
    :cvar K_J_KG: kilojoule per kilogram
    :cvar K_W_H_KG: kilowatt hour per kilogram
    :cvar LBF_FT_LBM: foot pound-force per pound-mass
    :cvar MJ_KG: megajoule per kilogram
    :cvar MW_H_KG: megawatt hour per kilogram
    """
    BTU_IT_LBM = "Btu[IT]/lbm"
    CAL_TH_G = "cal[th]/g"
    CAL_TH_KG = "cal[th]/kg"
    CAL_TH_LBM = "cal[th]/lbm"
    ERG_G = "erg/g"
    ERG_KG = "erg/kg"
    HP_H_LBM = "hp.h/lbm"
    J_G = "J/g"
    J_KG = "J/kg"
    KCAL_TH_G = "kcal[th]/g"
    KCAL_TH_KG = "kcal[th]/kg"
    K_J_KG = "kJ/kg"
    K_W_H_KG = "kW.h/kg"
    LBF_FT_LBM = "lbf.ft/lbm"
    MJ_KG = "MJ/kg"
    MW_H_KG = "MW.h/kg"
