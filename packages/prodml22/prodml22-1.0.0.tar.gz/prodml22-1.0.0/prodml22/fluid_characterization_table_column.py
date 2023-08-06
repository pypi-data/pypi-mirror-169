from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.legacy_unit_of_measure import LegacyUnitOfMeasure
from prodml22.object_alias import ObjectAlias
from prodml22.output_fluid_property import OutputFluidProperty
from prodml22.thermodynamic_phase import ThermodynamicPhase
from prodml22.unit_of_measure import UnitOfMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationTableColumn:
    """
    Column of a table.

    :ivar property: The property that this column contains. Enum. See
        output fluid property ext.
    :ivar phase:
    :ivar keyword_alias:
    :ivar fluid_component_reference: The  reference to a fluid component
        for this column in this fluid characterization table.
    :ivar name: The name for this column in this fluid characterization
        table.
    :ivar sequence: Index number for this column for consumption by an
        external system.
    :ivar uom: The UOM for this column in this fluid characterization
        table.
    """
    property: Optional[Union[OutputFluidProperty, str]] = field(
        default=None,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    phase: Optional[ThermodynamicPhase] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    keyword_alias: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "KeywordAlias",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_component_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidComponentReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
    sequence: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
        }
    )
    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
