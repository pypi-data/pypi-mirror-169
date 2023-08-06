from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure
from prodml22.detectable_limit_relative_state_kind import DetectableLimitRelativeStateKind
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_volume_measure_ext import MassPerVolumeMeasureExt
from prodml22.volume_per_volume_measure_ext import VolumePerVolumeMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidComponentFraction:
    """Fractions of a flluid component.

    It's expected but not required that only one of the fractions will
    be populated.

    :ivar mass_fraction: The mass fraction for the fluid component.
    :ivar mole_fraction: The mole fraction for the fluid component.
    :ivar volume_fraction:
    :ivar volume_concentration:
    :ivar kvalue: K value.
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
    :ivar fluid_component_reference: Fluid component reference.
    """
    mass_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "MassFraction",
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
    volume_fraction: Optional[VolumePerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "VolumeFraction",
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
    kvalue: Optional[AmountOfSubstancePerAmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "KValue",
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
    fluid_component_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fluidComponentReference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
