from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.mass_measure import MassMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class MassIn:
    """
    The mass of fluid in the connecting lines.

    :ivar mass_fluid_slimtube: The mass of fluid in the slim tube for
        this slim tube test volume step mass balance.
    :ivar mass_fluid_connecting_lines: The mass of fluid in the
        connecting lines for this slim tube test volume step mass
        balance.
    :ivar mass_injected_gas_solvent: The mass of injected gas solvent
        for this slim tube test volume step mass balance.
    :ivar total_mass_in: The total mass in for this slim tube test
        volume step mass balance.
    """
    mass_fluid_slimtube: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassFluidSlimtube",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_fluid_connecting_lines: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassFluidConnectingLines",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_injected_gas_solvent: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "MassInjectedGasSolvent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_mass_in: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalMassIn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
