from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.apigravity_measure import ApigravityMeasure
from prodml22.liquid_composition import LiquidComposition
from prodml22.mass_per_volume_measure_ext import MassPerVolumeMeasureExt
from prodml22.molecular_weight_measure import MolecularWeightMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FlashedLiquid:
    """
    Flashed liquid.

    :ivar liquid_density: This density is measured at the standard
        conditions for this Fluid Analysis.
    :ivar oil_apigravity: The oil molecular weight of the flashed liquid
        in this atmospheric flash test.
    :ivar oil_molecular_weight: The liquid composition of the flashed
        liquid in this atmospheric flash test.
    :ivar liquid_composition: The oil API gravity of the flashed liquid
        in this atmospheric flash test.
    """
    liquid_density: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "LiquidDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_apigravity: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "OilAPIGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "OilMolecularWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    liquid_composition: Optional[LiquidComposition] = field(
        default=None,
        metadata={
            "name": "LiquidComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
