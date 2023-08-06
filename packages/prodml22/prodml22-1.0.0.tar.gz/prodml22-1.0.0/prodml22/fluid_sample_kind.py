from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FluidSampleKind(Enum):
    """
    Species the kinds of fluid sample by reference to how it was obtained.

    :cvar BHS_SAMPLES:
    :cvar BLEND_GAS:
    :cvar BLEND_LIQUID:
    :cvar BRINE:
    :cvar CONDENSATE:
    :cvar FILTRATE:
    :cvar GAS:
    :cvar GAS_DRY:
    :cvar MUD_FILTRATE:
    :cvar MUD_SAMPLE:
    :cvar OIL_WATER:
    :cvar OIL_BASE:
    :cvar OIL_BLACK:
    :cvar OIL_DEAD:
    :cvar OIL_HEAVY:
    :cvar OIL_UNKNOWN:
    :cvar OIL_VOLATILE:
    :cvar OTHER:
    :cvar RECOMB_FLUID:
    :cvar RECOMB_GAS:
    :cvar RINSE_POST:
    :cvar RINSE_PRE:
    :cvar SOLID:
    :cvar STO:
    :cvar TOLUENE:
    :cvar WATER:
    :cvar WATER_CONDENSATE:
    :cvar SYNTHETIC: The fluid sample has originated from synthetic
        creation.
    :cvar SEPARATOR_WATER: The fluid sample has originated from
        separator water.
    :cvar SEPARATOR_OIL: The fluid sample has originated from separator
        oil.
    :cvar SEPARATOR_GAS: The fluid sample has originated from separator
        gas.
    :cvar DOWNHOLE_CASED: The fluid sample has originated from downhole
        cased hole sampling.
    :cvar DOWNHOLE_OPEN: The fluid sample has originated from downhole
        openhole sampling.
    :cvar RECOMBINED: The fluid sample has originated from recombined
        samples.
    :cvar WELLHEAD: The fluid sample has originated from wellhead
        sampling.
    :cvar COMMINGLED: The fluid sample has originated from commingled
        flow.
    """
    BHS_SAMPLES = "bhs  samples"
    BLEND_GAS = "blend-gas"
    BLEND_LIQUID = "blend-liquid"
    BRINE = "brine"
    CONDENSATE = "condensate"
    FILTRATE = "filtrate"
    GAS = "gas"
    GAS_DRY = "gas-dry"
    MUD_FILTRATE = "mud filtrate"
    MUD_SAMPLE = "mud sample"
    OIL_WATER = "oil &amp; water"
    OIL_BASE = "oil-base"
    OIL_BLACK = "oil-black"
    OIL_DEAD = "oil-dead"
    OIL_HEAVY = "oil-heavy"
    OIL_UNKNOWN = "oil-unknown"
    OIL_VOLATILE = "oil-volatile"
    OTHER = "other"
    RECOMB_FLUID = "recomb-fluid"
    RECOMB_GAS = "recomb-gas"
    RINSE_POST = "rinse-post"
    RINSE_PRE = "rinse-pre"
    SOLID = "solid"
    STO = "sto"
    TOLUENE = "toluene"
    WATER = "water"
    WATER_CONDENSATE = "water/condensate"
    SYNTHETIC = "synthetic"
    SEPARATOR_WATER = "separator water"
    SEPARATOR_OIL = "separator oil"
    SEPARATOR_GAS = "separator gas"
    DOWNHOLE_CASED = "downhole cased"
    DOWNHOLE_OPEN = "downhole open"
    RECOMBINED = "recombined"
    WELLHEAD = "wellhead"
    COMMINGLED = "commingled"
