from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_fluid_component import AbstractFluidComponent
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.pure_component_kind import PureComponentKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PureFluidComponent(AbstractFluidComponent):
    """
    Pure fluid component.

    :ivar kind: The type of component.
    :ivar molecular_weight: The molecular weight of the pure component.
    :ivar hydrocarbon_flag: Yes/no  flag indicates if hydrocarbon or
        not.
    :ivar remark: Remarks and comments about this data item.
    """
    kind: Optional[Union[PureComponentKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
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
    hydrocarbon_flag: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HydrocarbonFlag",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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
