from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class EnergyUom(Enum):
    """
    :cvar VALUE_1_E6_BTU_IT: million BTU
    :cvar A_J: attojoule
    :cvar BTU_IT: British thermal unit
    :cvar BTU_TH: thermochemical British thermal unit
    :cvar BTU_UK: United Kingdom British thermal unit
    :cvar CAL_IT: calorie [International Table]
    :cvar CAL_TH: calorie
    :cvar CCAL_TH: hundredth of calorie
    :cvar CE_V: centielectronvolt
    :cvar C_J: centijoule
    :cvar DCAL_TH: tenth of calorie
    :cvar DE_V: decielectronvolt
    :cvar D_J: decijoule
    :cvar ECAL_TH: million million million calorie
    :cvar EE_V: exaelectronvolt
    :cvar EJ: exajoule
    :cvar ERG: erg
    :cvar E_V: electronvolt
    :cvar FCAL_TH: femtocalorie
    :cvar FE_V: femtoelectronvolt
    :cvar F_J: femtojoule
    :cvar GCAL_TH: thousand million calorie
    :cvar GE_V: gigaelectronvolt
    :cvar GJ: gigajoule
    :cvar GW_H: gigawatt hour
    :cvar HP_H: horsepower hour
    :cvar HP_METRIC_H: metric-horsepower hour
    :cvar J: joule
    :cvar KCAL_TH: thousand calorie
    :cvar KE_V: kiloelectronvolt
    :cvar K_J: kilojoule
    :cvar K_W_H: kilowatt hour
    :cvar MCAL_TH: thousandth of calorie
    :cvar MCAL_TH_1: million calorie
    :cvar ME_V: millielectronvolt
    :cvar ME_V_1: megaelectronvolt
    :cvar MJ: megajoule
    :cvar M_J_1: millijoule
    :cvar MW_H: megawatt hour
    :cvar NCAL_TH: nanocalorie
    :cvar NE_V: nanoelectronvolt
    :cvar N_J: nanojoule
    :cvar PCAL_TH: picocalorie
    :cvar PE_V: picoelectronvolt
    :cvar P_J: picojoule
    :cvar QUAD: quad
    :cvar TCAL_TH: million million calorie
    :cvar TE_V: teraelectronvolt
    :cvar THERM_EC: European Community therm
    :cvar THERM_UK: United Kingdom therm
    :cvar THERM_US: United States therm
    :cvar TJ: terajoule
    :cvar TW_H: terrawatt hour
    :cvar UCAL_TH: millionth of calorie
    :cvar UE_V: microelectronvolt
    :cvar U_J: microjoule
    """
    VALUE_1_E6_BTU_IT = "1E6 Btu[IT]"
    A_J = "aJ"
    BTU_IT = "Btu[IT]"
    BTU_TH = "Btu[th]"
    BTU_UK = "Btu[UK]"
    CAL_IT = "cal[IT]"
    CAL_TH = "cal[th]"
    CCAL_TH = "ccal[th]"
    CE_V = "ceV"
    C_J = "cJ"
    DCAL_TH = "dcal[th]"
    DE_V = "deV"
    D_J = "dJ"
    ECAL_TH = "Ecal[th]"
    EE_V = "EeV"
    EJ = "EJ"
    ERG = "erg"
    E_V = "eV"
    FCAL_TH = "fcal[th]"
    FE_V = "feV"
    F_J = "fJ"
    GCAL_TH = "Gcal[th]"
    GE_V = "GeV"
    GJ = "GJ"
    GW_H = "GW.h"
    HP_H = "hp.h"
    HP_METRIC_H = "hp[metric].h"
    J = "J"
    KCAL_TH = "kcal[th]"
    KE_V = "keV"
    K_J = "kJ"
    K_W_H = "kW.h"
    MCAL_TH = "mcal[th]"
    MCAL_TH_1 = "Mcal[th]"
    ME_V = "meV"
    ME_V_1 = "MeV"
    MJ = "MJ"
    M_J_1 = "mJ"
    MW_H = "MW.h"
    NCAL_TH = "ncal[th]"
    NE_V = "neV"
    N_J = "nJ"
    PCAL_TH = "pcal[th]"
    PE_V = "peV"
    P_J = "pJ"
    QUAD = "quad"
    TCAL_TH = "Tcal[th]"
    TE_V = "TeV"
    THERM_EC = "therm[EC]"
    THERM_UK = "therm[UK]"
    THERM_US = "therm[US]"
    TJ = "TJ"
    TW_H = "TW.h"
    UCAL_TH = "ucal[th]"
    UE_V = "ueV"
    U_J = "uJ"
