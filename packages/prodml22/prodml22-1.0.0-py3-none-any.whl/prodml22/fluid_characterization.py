from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.abstract_temperature_pressure import AbstractTemperaturePressure
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_characterization_model import FluidCharacterizationModel
from prodml22.fluid_characterization_source import FluidCharacterizationSource
from prodml22.fluid_characterization_table_format import FluidCharacterizationTableFormat
from prodml22.fluid_component_catalog import FluidComponentCatalog

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterization(AbstractObject):
    """
    Fluid characterization.

    :ivar application_target: The software which is the consumer of the
        fluid characterization.
    :ivar kind: The kind of fluid characterization.
    :ivar intended_usage: The intended usage of the fluid
        characterization.
    :ivar rock_fluid_unit_interpretation: Reference to a
        RockFluidUnitInterpretation (a RESQML class).
    :ivar standard_conditions: The standard temperature and pressure
        used for the representation of this fluid characterization.
    :ivar source: Reference to the fluid analysis tests which were the
        source data for this fluid characterization.
    :ivar fluid_component_catalog: The fluid component catalog for this
        fluid characterization.
    :ivar model: The model used to generate the fluid characterization.
    :ivar table_format: The collection of fluid characterization table
        formats.
    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_system:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    application_target: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ApplicationTarget",
            "type": "Element",
            "max_length": 2000,
        }
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "max_length": 64,
        }
    )
    intended_usage: Optional[str] = field(
        default=None,
        metadata={
            "name": "IntendedUsage",
            "type": "Element",
            "max_length": 64,
        }
    )
    rock_fluid_unit_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RockFluidUnitInterpretation",
            "type": "Element",
        }
    )
    standard_conditions: Optional[AbstractTemperaturePressure] = field(
        default=None,
        metadata={
            "name": "StandardConditions",
            "type": "Element",
        }
    )
    source: List[FluidCharacterizationSource] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
        }
    )
    fluid_component_catalog: Optional[FluidComponentCatalog] = field(
        default=None,
        metadata={
            "name": "FluidComponentCatalog",
            "type": "Element",
        }
    )
    model: List[FluidCharacterizationModel] = field(
        default_factory=list,
        metadata={
            "name": "Model",
            "type": "Element",
        }
    )
    table_format: List[FluidCharacterizationTableFormat] = field(
        default_factory=list,
        metadata={
            "name": "TableFormat",
            "type": "Element",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_length": 2000,
        }
    )
    fluid_system: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSystem",
            "type": "Element",
        }
    )
