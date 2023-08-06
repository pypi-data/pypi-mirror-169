from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReportingProduct(Enum):
    """
    Specifies the kinds of product in a fluid system.

    :cvar AQUEOUS: aqueous
    :cvar C10: c10
    :cvar C10_1: c10-
    :cvar C10_2: c10+
    :cvar C2: c2-
    :cvar C2_1: c2+
    :cvar C3: c3-
    :cvar C3_1: c3+
    :cvar C4: c4-
    :cvar C4_1: c4+
    :cvar C5: c5-
    :cvar C5_1: c5+
    :cvar C6: c6-
    :cvar C6_1: c6+
    :cvar C7: c7
    :cvar C7_1: c7-
    :cvar C7_2: c7+
    :cvar C8: c8
    :cvar C8_1: c8-
    :cvar C8_2: c8+
    :cvar C9: c9
    :cvar C9_1: c9-
    :cvar C9_2: c9+
    :cvar CARBON_DIOXIDE_GAS: carbon dioxide gas
    :cvar CARBON_MONOXIDE_GAS: carbon monoxide gas
    :cvar CHEMICAL: chemical
    :cvar CONDENSATE: condensate
    :cvar CONDENSATE_GROSS: condensate - gross
    :cvar CONDENSATE_NET: condensate - net
    :cvar CRUDE_STABILIZED: crude - stabilized
    :cvar CUTTINGS: cuttings
    :cvar DIESEL: diesel
    :cvar DIETHYLENE_GLYCOL: diethylene glycol
    :cvar DIOXYGEN: dioxygen
    :cvar ELECTRIC_POWER: electric power
    :cvar ETHANE: ethane
    :cvar ETHANE_COMPONENT: ethane - component
    :cvar GAS: gas
    :cvar GAS_COMPONENT_IN_OIL: gas - component in oil
    :cvar GAS_DRY: gas - dry
    :cvar GAS_RICH: gas - rich
    :cvar GAS_WET: gas - wet
    :cvar HELIUM_GAS: helium gas
    :cvar HEPTANE: heptane
    :cvar HYDRAULIC_CONTROL_FLUID: hydraulic control fluid
    :cvar HYDROGEN_GAS: hydrogen gas
    :cvar HYDROGEN_SULFIDE: hydrogen sulfide
    :cvar I_BUTANE_COMPONENT: i-butane - component
    :cvar ISOBUTANE: isobutane
    :cvar ISOPENTANE: isopentane
    :cvar LIQUEFIED_NATURAL_GAS: liquefied natural gas
    :cvar LIQUEFIED_PETROLEUM_GAS: liquefied petroleum gas
    :cvar LIQUID: liquid
    :cvar METHANE: methane
    :cvar METHANE_COMPONENT: methane - component
    :cvar METHANOL: methanol
    :cvar MIXED_BUTANE: mixed butane
    :cvar MONOETHYLENE_GLYCOL: monoethylene glycol
    :cvar NAPHTHA: naphta
    :cvar NATURAL_GAS_LIQUID: natural gas liquid
    :cvar N_BUTANE_COMPONENT: n-butane - component
    :cvar NEOPENTANE: neopentane
    :cvar NGL_COMPONENT_IN_GAS: NGL - component in gas
    :cvar NITROGEN_GAS: nitrogen gas
    :cvar NITROGEN_OXIDE_GAS: nitrogen oxide gas
    :cvar NORMAL_BUTANE: normal butane
    :cvar NORMAL_PENTANE: normal pentane
    :cvar OIL: oil
    :cvar OIL_COMPONENT_IN_WATER: oil - component in water
    :cvar OIL_GROSS: oil - gross
    :cvar OIL_NET: oil - net
    :cvar OIL_AND_GAS: oil and gas
    :cvar OLEIC: oleic
    :cvar PENTANE_COMPONENT: pentane - component
    :cvar PETROLEUM_GAS_LIQUID: petroleum gas liquid
    :cvar PROPANE: propane
    :cvar PROPANE_COMPONENT: propane - component
    :cvar SALT: salt
    :cvar SAND_COMPONENT: sand - component
    :cvar TRIETHYLENE_GLYCOL: triethylene glycol
    :cvar UNKNOWN: unknown
    :cvar VAPOR: vapor
    :cvar WATER: water
    :cvar WATER_DISCHARGE: water - discharge
    :cvar WATER_PROCESSED: water - processed
    """
    AQUEOUS = "aqueous"
    C10 = "c10"
    C10_1 = "c10-"
    C10_2 = "c10+"
    C2 = "c2-"
    C2_1 = "c2+"
    C3 = "c3-"
    C3_1 = "c3+"
    C4 = "c4-"
    C4_1 = "c4+"
    C5 = "c5-"
    C5_1 = "c5+"
    C6 = "c6-"
    C6_1 = "c6+"
    C7 = "c7"
    C7_1 = "c7-"
    C7_2 = "c7+"
    C8 = "c8"
    C8_1 = "c8-"
    C8_2 = "c8+"
    C9 = "c9"
    C9_1 = "c9-"
    C9_2 = "c9+"
    CARBON_DIOXIDE_GAS = "carbon dioxide gas"
    CARBON_MONOXIDE_GAS = "carbon monoxide gas"
    CHEMICAL = "chemical"
    CONDENSATE = "condensate"
    CONDENSATE_GROSS = "condensate - gross"
    CONDENSATE_NET = "condensate - net"
    CRUDE_STABILIZED = "crude - stabilized"
    CUTTINGS = "cuttings"
    DIESEL = "diesel"
    DIETHYLENE_GLYCOL = "diethylene glycol"
    DIOXYGEN = "dioxygen"
    ELECTRIC_POWER = "electric power"
    ETHANE = "ethane"
    ETHANE_COMPONENT = "ethane - component"
    GAS = "gas"
    GAS_COMPONENT_IN_OIL = "gas - component in oil"
    GAS_DRY = "gas - dry"
    GAS_RICH = "gas - rich"
    GAS_WET = "gas - wet"
    HELIUM_GAS = "helium gas"
    HEPTANE = "heptane"
    HYDRAULIC_CONTROL_FLUID = "hydraulic control fluid"
    HYDROGEN_GAS = "hydrogen gas"
    HYDROGEN_SULFIDE = "hydrogen sulfide"
    I_BUTANE_COMPONENT = "i-butane - component"
    ISOBUTANE = "isobutane"
    ISOPENTANE = "isopentane"
    LIQUEFIED_NATURAL_GAS = "liquefied natural gas"
    LIQUEFIED_PETROLEUM_GAS = "liquefied petroleum gas"
    LIQUID = "liquid"
    METHANE = "methane"
    METHANE_COMPONENT = "methane - component"
    METHANOL = "methanol"
    MIXED_BUTANE = "mixed butane"
    MONOETHYLENE_GLYCOL = "monoethylene glycol"
    NAPHTHA = "naphtha"
    NATURAL_GAS_LIQUID = "natural gas liquid"
    N_BUTANE_COMPONENT = "n-butane - component"
    NEOPENTANE = "neopentane"
    NGL_COMPONENT_IN_GAS = "NGL - component in gas"
    NITROGEN_GAS = "nitrogen gas"
    NITROGEN_OXIDE_GAS = "nitrogen oxide gas"
    NORMAL_BUTANE = "normal butane"
    NORMAL_PENTANE = "normal pentane"
    OIL = "oil"
    OIL_COMPONENT_IN_WATER = "oil - component in water"
    OIL_GROSS = "oil - gross"
    OIL_NET = "oil - net"
    OIL_AND_GAS = "oil and gas"
    OLEIC = "oleic"
    PENTANE_COMPONENT = "pentane - component"
    PETROLEUM_GAS_LIQUID = "petroleum gas liquid"
    PROPANE = "propane"
    PROPANE_COMPONENT = "propane - component"
    SALT = "salt"
    SAND_COMPONENT = "sand - component"
    TRIETHYLENE_GLYCOL = "triethylene glycol"
    UNKNOWN = "unknown"
    VAPOR = "vapor"
    WATER = "water"
    WATER_DISCHARGE = "water - discharge"
    WATER_PROCESSED = "water - processed"
