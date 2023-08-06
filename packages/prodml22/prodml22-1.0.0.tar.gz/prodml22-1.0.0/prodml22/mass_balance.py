from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.mass_in import MassIn
from prodml22.mass_out import MassOut
from prodml22.mass_per_mass_measure import MassPerMassMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class MassBalance:
    """
    The balance sheet of mass.

    :ivar mass_balance_fraction: The mass balance fraction for this slim
        tube test volume step.
    :ivar remark: Remarks and comments about this data item.
    :ivar mass_in:
    :ivar mass_out:
    """
    mass_balance_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "MassBalanceFraction",
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
    mass_in: Optional[MassIn] = field(
        default=None,
        metadata={
            "name": "MassIn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_out: Optional[MassOut] = field(
        default=None,
        metadata={
            "name": "MassOut",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
