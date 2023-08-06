from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.energy_per_mass_measure_ext import EnergyPerMassMeasureExt
from prodml22.energy_per_volume_measure_ext import EnergyPerVolumeMeasureExt
from prodml22.mass_per_volume_measure_ext import MassPerVolumeMeasureExt
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.vapor_composition import VaporComposition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FlashedGas:
    """
    Flashed gas.

    :ivar gas_density: This density is measured at the standard
        conditions for this Fluid Analysis.
    :ivar gas_gravity: The gas gravity of the flashed gas in this
        atmospheric flash test.
    :ivar gas_zfactor: The gas Z factor value at this test step.
    :ivar gas_molecular_weight: The molecular weight of the gas phase at
        this test step.
    :ivar gross_energy_content_per_unit_mass: The amount of heat
        released during the combustion of a specified amount of gas. It
        is also known as higher heating value (HHV), gross energy, upper
        heating value, gross calorific value (GCV) or higher calorific
        Value (HCV). This value takes into account the latent heat of
        vaporization of water in the combustion products, and is useful
        in calculating heating values for fuels where condensation of
        the reaction products is practical.
    :ivar net_energy_content_per_unit_mass: The amount of heat released
        during the combustion of a specified amount of gas. It is also
        known as lower heating value (LHV), net energy, net calorific
        value (NCV) or lower calorific value (LCV). This value ignores
        the latent heat of vaporization of water in the combustion
        products, and is useful in calculating heating values for fuels
        where condensation of the reaction products is not possible and
        is ignored.
    :ivar gross_energy_content_per_unit_volume: The amount of heat
        released during the combustion of a specified amount of gas. It
        is also known as higher heating value (HHV), gross energy, upper
        heating value, gross calorific value (GCV) or higher calorific
        value (HCV). This value takes into account the latent heat of
        vaporization of water in the combustion products, and is useful
        in calculating heating values for fuels where condensation of
        the reaction products is practical.
    :ivar net_energy_content_per_unit_volume: The amount of heat
        released during the combustion of a specified amount of gas. It
        is also known as lower heating value (LHV), net energy, net
        calorific value (NCV) or lower calorific value (LCV). This value
        ignores the latent heat of vaporization of water in the
        combustion products, and is useful in calculating heating values
        for fuels where condensation of the reaction products is not
        possible and is ignored.
    :ivar vapor_composition: The vapor composition of the flashed gas in
        this atmospheric flash test.
    """
    gas_density: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "GasDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "GasGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_zfactor: Optional[float] = field(
        default=None,
        metadata={
            "name": "GasZFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "GasMolecularWeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gross_energy_content_per_unit_mass: Optional[EnergyPerMassMeasureExt] = field(
        default=None,
        metadata={
            "name": "GrossEnergyContentPerUnitMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    net_energy_content_per_unit_mass: Optional[EnergyPerMassMeasureExt] = field(
        default=None,
        metadata={
            "name": "NetEnergyContentPerUnitMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gross_energy_content_per_unit_volume: Optional[EnergyPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "GrossEnergyContentPerUnitVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    net_energy_content_per_unit_volume: Optional[EnergyPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "NetEnergyContentPerUnitVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vapor_composition: Optional[VaporComposition] = field(
        default=None,
        metadata={
            "name": "VaporComposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
