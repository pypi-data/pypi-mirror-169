from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.fluid_analysis_step_condition import FluidAnalysisStepCondition
from prodml22.liquid_composition import LiquidComposition
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.overall_composition import OverallComposition
from prodml22.phase_present import PhasePresent
from prodml22.pressure_measure import PressureMeasure
from prodml22.stoflashed_liquid import StoflashedLiquid
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.vapor_composition import VaporComposition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Stoanalysis:
    """
    Stock tank oil analysis.

    :ivar date: The date when this test was performed.
    :ivar flash_from_pressure: The pressure from which the sample was
        flashed for the stock tank oil analysis.
    :ivar flash_from_temperature: The temperature from which the sample
        was flashed for the stock tank oil analysis.
    :ivar molecular_weight: The molecular weight for the stock tank oil
        analysis.
    :ivar fluid_condition: The fluid condition at this test step. Enum,
        see fluid analysis step condition.
    :ivar phases_present: The phases present for the stock tank oil
        analysis.
    :ivar liquid_composition: The liquid composition for the stock tank
        oil analysis.
    :ivar vapor_composition: The vapor composition for the stock tank
        oil analysis.
    :ivar overall_composition: The overall composition for the stock
        tank oil analysis.
    :ivar remark: Remarks and comments about this data item.
    :ivar stoflashed_liquid: Stock tank oil flashed liquid properties
        and composition.
    """
    class Meta:
        name = "STOAnalysis"

    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    flash_from_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FlashFromPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flash_from_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "FlashFromTemperature",
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
    fluid_condition: Optional[FluidAnalysisStepCondition] = field(
        default=None,
        metadata={
            "name": "FluidCondition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    phases_present: Optional[PhasePresent] = field(
        default=None,
        metadata={
            "name": "PhasesPresent",
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
    vapor_composition: Optional[VaporComposition] = field(
        default=None,
        metadata={
            "name": "VaporComposition",
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
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    stoflashed_liquid: Optional[StoflashedLiquid] = field(
        default=None,
        metadata={
            "name": "STOFlashedLiquid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
