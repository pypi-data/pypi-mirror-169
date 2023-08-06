from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_fluid_component import AbstractFluidComponent
from prodml22.apigravity_measure import ApigravityMeasure
from prodml22.energy_per_mass_measure import EnergyPerMassMeasure
from prodml22.energy_per_volume_measure import EnergyPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class StockTankOil(AbstractFluidComponent):
    """
    Stock tank oil (STO).

    :ivar apigravity: API gravity.
    :ivar molecular_weight: Molecular weight.
    :ivar gross_energy_content_per_unit_mass: The amount of heat
        released during the combustion of a specified amount of STO. It
        is also known as higher heating value (HHV), gross energy, upper
        heating value, gross calorific value (GCV) or higher calorific
        value (HCV). This value takes into account the latent heat of
        vaporization of water in the combustion products, and is useful
        in calculating heating values for fuels where condensation of
        the reaction products is practical.
    :ivar net_energy_content_per_unit_mass: The amount of heat released
        during the combustion of a specified amount of STO. It is also
        known as lower heating value (LHV), net energy, lower heating
        value, net calorific value  (NCV) or lower calorific value
        (LCV). This value ignores the latent heat of vaporization of
        water in the combustion products, and is useful in calculating
        heating values for fuels where condensation of the reaction
        products is not possible and is ignored.
    :ivar gross_energy_content_per_unit_volume: The amount of heat
        released during the combustion of a specified amount of STO. It
        is also known as higher heating value (HHV), gross energy, upper
        heating value,  gross calorific value (GCV) or higher calorific
        value (HCV). This value takes into account the latent heat of
        vaporization of water in the combustion products, and is useful
        in calculating heating values for fuels where condensation of
        the reaction products is practical.
    :ivar net_energy_content_per_unit_volume: The amount of heat
        released during the combustion of a specified amount of STO. It
        is also known as lower heating value  (LHV), net energy, net
        calorific value (NCV) or lower calorific value (LCV). This value
        ignores the latent heat of vaporization of water in the
        combustion products, and is useful in calculating heating values
        for fuels where condensation of the reaction products is not
        possible and is ignored.
    :ivar remark: Remarks and comments about this data item.
    """
    apigravity: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "APIGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "MolecularWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gross_energy_content_per_unit_mass: Optional[EnergyPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "GrossEnergyContentPerUnitMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    net_energy_content_per_unit_mass: Optional[EnergyPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "NetEnergyContentPerUnitMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gross_energy_content_per_unit_volume: Optional[EnergyPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossEnergyContentPerUnitVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    net_energy_content_per_unit_volume: Optional[EnergyPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "NetEnergyContentPerUnitVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
