from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class PowerUom(Enum):
    """
    :cvar C_W: centiwatt
    :cvar D_W: deciwatt
    :cvar EW: exawatt
    :cvar F_W: femtowatt
    :cvar GW: gigawatt
    :cvar HP: horsepower
    :cvar HP_ELEC: electric-horsepower
    :cvar HP_HYD: hydraulic-horsepower
    :cvar HP_METRIC: metric-horsepower
    :cvar K_W: kilowatt
    :cvar MW: megawatt
    :cvar M_W_1: milliwatt
    :cvar N_W: nanowatt
    :cvar P_W: picowatt
    :cvar TON_REFRIG: ton-refrigeration
    :cvar TW: terawatt
    :cvar U_W: microwatt
    :cvar W: watt
    """
    C_W = "cW"
    D_W = "dW"
    EW = "EW"
    F_W = "fW"
    GW = "GW"
    HP = "hp"
    HP_ELEC = "hp[elec]"
    HP_HYD = "hp[hyd]"
    HP_METRIC = "hp[metric]"
    K_W = "kW"
    MW = "MW"
    M_W_1 = "mW"
    N_W = "nW"
    P_W = "pW"
    TON_REFRIG = "tonRefrig"
    TW = "TW"
    U_W = "uW"
    W = "W"
