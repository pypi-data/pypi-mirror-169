from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.abstract_pvt_model import AbstractPvtModel
from prodml22.fluid_characterization_parameter_set import FluidCharacterizationParameterSet
from prodml22.fluid_characterization_table import FluidCharacterizationTable
from prodml22.reference_separator_stage import ReferenceSeparatorStage
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationModel:
    """
    Fluid characterization model.

    :ivar name: The name of the fluid analysis result.
    :ivar reference_pressure: The reference pressure for this fluid
        characterization.
    :ivar reference_stock_tank_pressure: The reference stock tank
        pressure for this fluid characterization.
    :ivar reference_temperature: The reference temperature for this
        fluid characterization.
    :ivar reference_stock_tank_temperature: The reference stock tank
        temperature for this fluid characterization.
    :ivar remark: Remarks and comments about this data item.
    :ivar model_specification:
    :ivar fluid_characterization_table: Fluid characterization table.
    :ivar fluid_characterization_parameter_set: The constant definition
        used in the table.
    :ivar reference_separator_stage: Reference to the separator stage.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    reference_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "ReferencePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reference_stock_tank_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "ReferenceStockTankPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reference_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ReferenceTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reference_stock_tank_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "ReferenceStockTankTemperature",
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
    model_specification: Optional[AbstractPvtModel] = field(
        default=None,
        metadata={
            "name": "ModelSpecification",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_characterization_table: List[FluidCharacterizationTable] = field(
        default_factory=list,
        metadata={
            "name": "FluidCharacterizationTable",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_characterization_parameter_set: Optional[FluidCharacterizationParameterSet] = field(
        default=None,
        metadata={
            "name": "FluidCharacterizationParameterSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reference_separator_stage: List[ReferenceSeparatorStage] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceSeparatorStage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
