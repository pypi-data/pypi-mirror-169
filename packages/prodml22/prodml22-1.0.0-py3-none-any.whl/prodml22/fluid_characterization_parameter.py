from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.object_alias import ObjectAlias
from prodml22.output_fluid_property import OutputFluidProperty
from prodml22.thermodynamic_phase import ThermodynamicPhase

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidCharacterizationParameter:
    """
    The constant definition used in the table.

    :ivar property: The property that this table constant contains.
        Enum. See output fluid property ext.
    :ivar phase:
    :ivar keyword_alias:
    :ivar name: User-defined name for this attribute.
    :ivar value: The value for this table constant.
    :ivar uom: The UOM for this constant for this fluid characterization
        table.
    :ivar fluid_component_reference: Reference to the fluid component to
        which this value relates.
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
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
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
