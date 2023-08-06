from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RefInjectedGasAdded(AmountOfSubstancePerAmountOfSubstanceMeasure):
    """
    A reference to the particular gas quantity injected, using a uid which
    refers to an Injected Gas, and the quantity as a molar ratio injected.

    :ivar injection_gas_reference: Reference by uid to the Injection Gas
        used for this quantity of injected gas.
    """
    injection_gas_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "injectionGasReference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
