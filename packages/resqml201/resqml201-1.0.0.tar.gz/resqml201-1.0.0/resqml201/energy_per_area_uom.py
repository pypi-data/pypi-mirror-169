from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyPerAreaUom(Enum):
    """
    :cvar ERG_CM2: erg per square centimetre
    :cvar J_CM2: joule per square centimetre
    :cvar J_M2: joule per square metre
    :cvar KGF_M_CM2: thousand gram-force metre per square centimetre
    :cvar LBF_FT_IN2: foot pound-force per square inch
    :cvar M_J_CM2: millijoule per square centimetre
    :cvar M_J_M2: millijoule per square metre
    :cvar N_M: newton per metre
    """
    ERG_CM2 = "erg/cm2"
    J_CM2 = "J/cm2"
    J_M2 = "J/m2"
    KGF_M_CM2 = "kgf.m/cm2"
    LBF_FT_IN2 = "lbf.ft/in2"
    M_J_CM2 = "mJ/cm2"
    M_J_M2 = "mJ/m2"
    N_M = "N/m"
