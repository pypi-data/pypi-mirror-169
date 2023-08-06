from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure
from prodml22.detectable_limit_relative_state_kind import DetectableLimitRelativeStateKind
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_volume_measure_ext import MassPerVolumeMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractFluidComponent:
    """
    The Abstract base type of FluidComponent.

    :ivar mass_fraction: The fluid mass fraction.
    :ivar volume_concentration:
    :ivar mole_fraction: The fluid mole fraction.
    :ivar concentration_relative_to_detectable_limits: This element can
        be used where a measurement for a concentration is only capable
        of a "yes/no" type accuracy. Values can be ADL (meaning the
        measurement was Above Detectable Limits) or BDL (meaning the
        measurement was Below Detectable Limits). If the condition is
        "ADL" then the concentration as reported in Mass Fraction or
        Mole Fraction is expected to represent the maximum value which
        can be distinguished (so that we know the actual value to be
        equal to or greater than that). If the condition is "BDL" then
        the concentration as reported in Mass Fraction or Mole Fraction
        is expected to represent the minimum value which can be
        distinguished (so that we know the actual value to be equal to
        or less than that).
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    mass_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "MassFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    volume_concentration: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "VolumeConcentration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mole_fraction: Optional[AmountOfSubstancePerAmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "MoleFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    concentration_relative_to_detectable_limits: Optional[DetectableLimitRelativeStateKind] = field(
        default=None,
        metadata={
            "name": "ConcentrationRelativeToDetectableLimits",
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
