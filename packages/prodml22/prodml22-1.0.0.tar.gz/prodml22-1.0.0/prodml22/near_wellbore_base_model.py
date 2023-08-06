from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_model_section import AbstractModelSection
from prodml22.delta_pressure_total_skin import DeltaPressureTotalSkin
from prodml22.rate_dependent_skin_factor import RateDependentSkinFactor
from prodml22.ratio_dp_skin_to_total_drawdown import RatioDpSkinToTotalDrawdown
from prodml22.skin_relative_to_total_thickness import SkinRelativeToTotalThickness

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class NearWellboreBaseModel(AbstractModelSection):
    """
    Abstract near-wellbore response model from which the other near wellbore
    response model types are derived.
    """
    skin_relative_to_total_thickness: Optional[SkinRelativeToTotalThickness] = field(
        default=None,
        metadata={
            "name": "SkinRelativeToTotalThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    rate_dependent_skin_factor: Optional[RateDependentSkinFactor] = field(
        default=None,
        metadata={
            "name": "RateDependentSkinFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    delta_pressure_total_skin: Optional[DeltaPressureTotalSkin] = field(
        default=None,
        metadata={
            "name": "DeltaPressureTotalSkin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    ratio_dp_skin_to_total_drawdown: Optional[RatioDpSkinToTotalDrawdown] = field(
        default=None,
        metadata={
            "name": "RatioDpSkinToTotalDrawdown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
