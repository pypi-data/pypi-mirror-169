from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.amount_of_substance_measure import AmountOfSubstanceMeasure
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure
from prodml22.density_value import DensityValue
from prodml22.dimensionless_measure import DimensionlessMeasure
from prodml22.energy_measure import EnergyMeasure
from prodml22.energy_per_volume_measure import EnergyPerVolumeMeasure
from prodml22.flow_rate_value import FlowRateValue
from prodml22.isothermal_compressibility_measure import IsothermalCompressibilityMeasure
from prodml22.mass_measure import MassMeasure
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_time_measure import MassPerTimeMeasure
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.product_volume_port_difference import ProductVolumePortDifference
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure
from prodml22.volume_value import VolumeValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CommonPropertiesProductVolume:
    """
    Properties that are common to multiple structures in the product volume
    schema.

    :ivar gor: Gas oil ratio. The ratio between the total produced gas
        volume and the total produced oil volume including oil and gas
        volumes used on the installation.
    :ivar gor_mtd: Gas oil ratio month to date. The gas oil ratio from
        the beginning of the month to the end of the reporting period.
    :ivar gas_liquid_ratio: The volumetric ratio of gas to liquid for
        all products in the whole flow.
    :ivar water_conc_mass: Water concentration mass basis. The ratio of
        water produced compared to the mass of total liquids produced.
    :ivar water_conc_vol: Water concentration volume basis. The ratio of
        water produced compared to the mass of total liquids produced.
    :ivar atmosphere: The average atmospheric pressure during the
        reporting period.
    :ivar temp: Temperature of the port. Specifying the temperature here
        (as opposed to in Period) implies that the temperature is
        constant for all periods of the flow.
    :ivar pres: Pressure of the port. Specifying the pressure here (as
        opposed to in Period) implies that the pressure is constant for
        all periods of the flow.
    :ivar absolute_min_pres: Absolute minimum pressure before the system
        will give an alarm.
    :ivar mass: The mass of the product.
    :ivar work: The electrical energy represented by the product.
    :ivar efficiency: The actual volume divided by the potential volume.
    :ivar rvp: Reid vapor pressure of the product. The absolute vapor
        pressure of volatile crude oil and volatile petroleum liquids,
        except liquefied petroleum gases, as determined in accordance
        with American Society for Testing and Materials under the
        designation ASTM D323-56.
    :ivar tvp: True vapor pressure of the product. The equilibrium
        partial pressure exerted by a petroleum liquid as determined in
        accordance with standard methods.
    :ivar bsw: Basic sediment and water is measured from a liquid sample
        of the production stream. It includes free water, sediment and
        emulsion and is measured as a volume percentage of the
        production stream.
    :ivar bsw_previous: The basic sediment and water as measured on the
        previous reporting period (e.g., day).
    :ivar density_flow_rate: The mass basis flow rate of the product.
        This is used for things like a sand component.
    :ivar concentration: The concentration of the product as a volume
        percentage of the product stream.
    :ivar molecular_weight: The molecular weight of the product.
    :ivar weight_percent: The weight fraction of the product.
    :ivar mole_percent: The mole fraction of the product.
    :ivar mole_amt: The molar amount.
    :ivar sg: The specific gravity of the product.
    :ivar hc_dewpoint: The temperature at which the heavier hydrocarbons
        come out of solution.
    :ivar water_dewpoint: The temperature at which the first water comes
        out of solution.
    :ivar wobbe_index: Indicator value of the interchangeability of fuel
        gases.
    :ivar gross_calorific_value_std: The amount of heat that would be
        released by the complete combustion in air of a specific
        quantity of product at standard temperature and pressure.
    :ivar rvp_stabilized_crude: Reid vapor pressure of stabilized crude.
    :ivar bsw_stabilized_crude: Basic sediment and water content in
        stabilized crude.
    :ivar density_stabilized_crude: The density of stabilized crude.
    :ivar density_value: A possibly temperature and pressure corrected
        desity value.
    :ivar volume_value: A possibly temperature and pressure corrected
        volume value.
    :ivar port_diff: The internal differences between this port and one
        other port on this unit.
    :ivar flow_rate_value: A possibly temperature and pressure corrected
        flow rate value.
    """
    gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Gor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gor_mtd: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GorMTD",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_liquid_ratio: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasLiquidRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_conc_mass: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "WaterConcMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_conc_vol: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterConcVol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    atmosphere: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Atmosphere",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    temp: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "Temp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Pres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    absolute_min_pres: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "AbsoluteMinPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "Mass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    work: Optional[EnergyMeasure] = field(
        default=None,
        metadata={
            "name": "Work",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    efficiency: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Efficiency",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    rvp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Rvp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    tvp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Tvp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bsw: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Bsw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bsw_previous: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BswPrevious",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    density_flow_rate: Optional[MassPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityFlowRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    concentration: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Concentration",
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
    weight_percent: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "WeightPercent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mole_percent: Optional[AmountOfSubstancePerAmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "MolePercent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mole_amt: Optional[AmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "MoleAmt",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    sg: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Sg",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    hc_dewpoint: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "HcDewpoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_dewpoint: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "WaterDewpoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wobbe_index: Optional[IsothermalCompressibilityMeasure] = field(
        default=None,
        metadata={
            "name": "WobbeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gross_calorific_value_std: Optional[EnergyPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GrossCalorificValueStd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    rvp_stabilized_crude: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "RvpStabilizedCrude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bsw_stabilized_crude: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "BswStabilizedCrude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    density_stabilized_crude: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityStabilizedCrude",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    density_value: List[DensityValue] = field(
        default_factory=list,
        metadata={
            "name": "DensityValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    volume_value: List[VolumeValue] = field(
        default_factory=list,
        metadata={
            "name": "VolumeValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    port_diff: List[ProductVolumePortDifference] = field(
        default_factory=list,
        metadata={
            "name": "PortDiff",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flow_rate_value: List[FlowRateValue] = field(
        default_factory=list,
        metadata={
            "name": "FlowRateValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
