from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.amount_of_substance_per_amount_of_substance_measure_ext import AmountOfSubstancePerAmountOfSubstanceMeasureExt
from prodml22.anion_kind import AnionKind
from prodml22.cation_kind import CationKind
from prodml22.detectable_limit_relative_state_kind import DetectableLimitRelativeStateKind
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_volume_measure_ext import MassPerVolumeMeasureExt
from prodml22.organic_acid_kind import OrganicAcidKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WaterSampleComponent:
    """
    Water sample component.

    :ivar test_method:
    :ivar anion:
    :ivar cation:
    :ivar organic_acid:
    :ivar molar_concentration:
    :ivar volume_concentration:
    :ivar mass_concentration: The mass concentration of the water sample
        component.
    :ivar equivalent_concentration: The equivalent concentration of
        CaCO3 of the water sample component.
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
    :ivar remark:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    test_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    anion: Optional[Union[AnionKind, str]] = field(
        default=None,
        metadata={
            "name": "Anion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".*:.*",
        }
    )
    cation: Optional[Union[CationKind, str]] = field(
        default=None,
        metadata={
            "name": "Cation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".*:.*",
        }
    )
    organic_acid: Optional[Union[OrganicAcidKind, str]] = field(
        default=None,
        metadata={
            "name": "OrganicAcid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".*:.*",
        }
    )
    molar_concentration: Optional[AmountOfSubstancePerAmountOfSubstanceMeasureExt] = field(
        default=None,
        metadata={
            "name": "MolarConcentration",
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
    mass_concentration: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "MassConcentration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    equivalent_concentration: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "EquivalentConcentration",
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
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
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
