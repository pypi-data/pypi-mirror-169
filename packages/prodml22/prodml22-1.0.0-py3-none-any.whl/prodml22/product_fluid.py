from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_product_quantity import AbstractProductQuantity
from prodml22.energy_measure import EnergyMeasure
from prodml22.overall_composition import OverallComposition
from prodml22.product_fluid_kind import ProductFluidKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductFluid(AbstractProductQuantity):
    """Contains the physical properties of the product fluid.

    Every volume has a product fluid reference.

    :ivar product_fluid_kind: A simple enumeration to provide
        information about the product that the production quantity
        represents.
    :ivar gross_energy_content: The amount of heat released during the
        combustion of the reported amount of this product. This value
        takes into account the latent heat of vaporization of water in
        the combustion products, and is useful in calculating heating
        values for fuels where condensation of the reaction products is
        practical.
    :ivar net_energy_content: The amount of heat released during the
        combustion of the reported amount of this product. This value
        ignores the latent heat of vaporization of water in the
        combustion products, and is useful in calculating heating values
        for fuels where condensation of the reaction products is not
        possible and is ignored.
    :ivar overall_composition: Overall composition.
    :ivar product_fluid_reference: String UID that points to the
        productFluid in the fluidComponentSet.
    """
    product_fluid_kind: Optional[Union[ProductFluidKind, str]] = field(
        default=None,
        metadata={
            "name": "ProductFluidKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    gross_energy_content: Optional[EnergyMeasure] = field(
        default=None,
        metadata={
            "name": "GrossEnergyContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    net_energy_content: Optional[EnergyMeasure] = field(
        default=None,
        metadata={
            "name": "NetEnergyContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    overall_composition: Optional[OverallComposition] = field(
        default=None,
        metadata={
            "name": "OverallComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    product_fluid_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "productFluidReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
