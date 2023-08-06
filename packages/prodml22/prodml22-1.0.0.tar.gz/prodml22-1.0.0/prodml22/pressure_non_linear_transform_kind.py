from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class PressureNonLinearTransformKind(Enum):
    """
    Optional enum for gas or multiphase pseudo pressure analyses using pressure
    transforms.
    """
    PRESSURE_UN_TRANSFORMED = "pressure (un-transformed)"
    PRESSURE_SQUARED = "pressure squared"
    GAS_PSEUDO_PRESSURE = "gas pseudo-pressure"
    NORMALISED_GAS_PSEUDO_PRESSURE = "normalised gas pseudo-pressure"
    NORMALISED_MULTI_PHASE_PSEUDO_PRESSURE = "normalised multi-phase pseudo-pressure"
