from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ServiceFluidKind(Enum):
    """
    Specifies the kinds of product in a fluid system.

    :cvar ALKALINE_SOLUTIONS: alkaline solutions
    :cvar BIOCIDE: biocide
    :cvar CARBON_DIOXIDE: carbon dioxide
    :cvar CARBON_MONOXIDE: carbon monoxide
    :cvar CORROSION_INHIBITOR: corrosion inhibitor
    :cvar DEMULSIFIER: demulsifier
    :cvar DIESEL: diesel
    :cvar DIETHYLENE_GLYCOL: diethylene glycol
    :cvar DISPERSANT: dispersant
    :cvar DRAG_REDUCING_AGENT: drag reducing agent
    :cvar EMULSIFIER: emulsifier
    :cvar FLOCCULANT: flocculant
    :cvar HYDRAULIC_CONTROL_FLUID: hydraulic control fluid
    :cvar ISOPROPANOL: isopropanol
    :cvar LUBRICANT: lubricant
    :cvar METHANOL: methanol
    :cvar MONOETHYLENE_GLYCOL: monoethylene glycol
    :cvar OIL: oil
    :cvar OTHER_CHEMICAL: other chemical
    :cvar OTHER_HYDRATE_INHIBITOR: other hydrate inhibitor
    :cvar POLYMER: polymer
    :cvar SCALE_INHIBITOR: scale inhibitor
    :cvar SOLVENT: solvent
    :cvar STABILIZING_AGENT: stabilizing agent
    :cvar SURFACTANT: surfactant
    :cvar THINNER: thinner
    :cvar TRIETHYLENE_GLYCOL: triethylene glycol
    """
    ALKALINE_SOLUTIONS = "alkaline solutions"
    BIOCIDE = "biocide"
    CARBON_DIOXIDE = "carbon dioxide"
    CARBON_MONOXIDE = "carbon monoxide"
    CORROSION_INHIBITOR = "corrosion inhibitor"
    DEMULSIFIER = "demulsifier"
    DIESEL = "diesel"
    DIETHYLENE_GLYCOL = "diethylene glycol"
    DISPERSANT = "dispersant"
    DRAG_REDUCING_AGENT = "drag reducing agent"
    EMULSIFIER = "emulsifier"
    FLOCCULANT = "flocculant"
    HYDRAULIC_CONTROL_FLUID = "hydraulic control fluid"
    ISOPROPANOL = "isopropanol"
    LUBRICANT = "lubricant"
    METHANOL = "methanol"
    MONOETHYLENE_GLYCOL = "monoethylene glycol"
    OIL = "oil"
    OTHER_CHEMICAL = "other chemical"
    OTHER_HYDRATE_INHIBITOR = "other hydrate inhibitor"
    POLYMER = "polymer"
    SCALE_INHIBITOR = "scale inhibitor"
    SOLVENT = "solvent"
    STABILIZING_AGENT = "stabilizing agent"
    SURFACTANT = "surfactant"
    THINNER = "thinner"
    TRIETHYLENE_GLYCOL = "triethylene glycol"
