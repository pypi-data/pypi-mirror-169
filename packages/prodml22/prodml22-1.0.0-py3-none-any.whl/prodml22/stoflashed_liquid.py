from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.apigravity_measure import ApigravityMeasure
from prodml22.dimensionless_measure import DimensionlessMeasure
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.sara import Sara
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.viscosity_at_temperature import ViscosityAtTemperature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class StoflashedLiquid:
    """
    Stock tank oil flashed liquid properties and composition.

    :ivar oil_apigravity: Oil API gravity.
    :ivar water_content: The water content of the liquid phase of the
        stock tank analysis.
    :ivar watson_kfactor: The Watson K factor of the liquid phase of the
        stock tank analysis.
    :ivar asphaltene_content: The asphaltene content of the liquid phase
        of the stock tank analysis.
    :ivar paraffin_content: The paraffin content of the liquid phase of
        the stock tank analysis.
    :ivar cloud_point: The cloud point of the liquid phase of the stock
        tank analysis.
    :ivar wax_appearance_temperature: The wax appearance temperature of
        the liquid phase of the stock tank analysis.
    :ivar pour_point: The pour point of the liquid phase of the stock
        tank analysis.
    :ivar astmflash_point: The ASTM flash point of the liquid phase of
        the stock tank analysis.
    :ivar total_acid_number: The total acid number of the liquid phase
        of the stock tank analysis.
    :ivar total_sulfur: The total sulfur content of the liquid phase of
        the stock tank analysis.
    :ivar nitrogen: The nitrogen content of the liquid phase of the
        stock tank analysis.
    :ivar elemental_sulfur: The elemental sulfur content of the liquid
        phase of the stock tank analysis.
    :ivar lead: The lead content of the liquid phase of the stock tank
        analysis.
    :ivar nickel: The nickel content of the liquid phase of the stock
        tank analysis.
    :ivar vanadium: The vanadium content of the liquid phase of the
        stock tank analysis.
    :ivar iron: The iron content of the liquid phase of the stock tank
        analysis.
    :ivar viscosity_at_temperature: The viscosity at test temperature of
        the liquid phase of the stock tank analysis.
    :ivar reid_vapor_pressure: The reid vapor pressure of the liquid
        phase of the stock tank analysis.
    :ivar sara: SARA analysis results. SARA stands for saturates,
        asphaltenes, resins and aromatics.
    """
    class Meta:
        name = "STOFlashedLiquid"

    oil_apigravity: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "OilAPIGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_content: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "WaterContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    watson_kfactor: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "WatsonKFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    asphaltene_content: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "AsphalteneContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    paraffin_content: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "ParaffinContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cloud_point: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "CloudPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wax_appearance_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "WaxAppearanceTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pour_point: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "PourPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    astmflash_point: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ASTMFlashPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_acid_number: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "TotalAcidNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_sulfur: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalSulfur",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    nitrogen: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Nitrogen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    elemental_sulfur: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "ElementalSulfur",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    lead: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Lead",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    nickel: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Nickel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    vanadium: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Vanadium",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    iron: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Iron",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    viscosity_at_temperature: List[ViscosityAtTemperature] = field(
        default_factory=list,
        metadata={
            "name": "ViscosityAtTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reid_vapor_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "ReidVaporPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    sara: List[Sara] = field(
        default_factory=list,
        metadata={
            "name": "Sara",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
