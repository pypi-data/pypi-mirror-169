from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_fluid_component import AbstractFluidComponent
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.plus_component_kind import PlusComponentKind
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PlusFluidComponent(AbstractFluidComponent):
    """
    Plus fluid component.

    :ivar kind: The kind from plus fluid component. See
        PlusComponentEnum.
    :ivar specific_gravity: The fluid specific gravity.
    :ivar starting_carbon_number: The start/min carbon number.
    :ivar starting_boiling_point: The starting boiling temperature
        measure.
    :ivar avg_density: The average density of the fluid.
    :ivar avg_molecular_weight: The average molecular weight of the
        fluid.
    :ivar remark: Remarks and comments about this data item.
    """
    kind: Optional[Union[PlusComponentKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    specific_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "SpecificGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    starting_carbon_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartingCarbonNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
    starting_boiling_point: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "StartingBoilingPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    avg_density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "AvgDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    avg_molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "AvgMolecularWeight",
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
