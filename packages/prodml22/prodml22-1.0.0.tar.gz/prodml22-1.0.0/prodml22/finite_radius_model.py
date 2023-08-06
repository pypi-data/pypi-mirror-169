from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.near_wellbore_base_model import NearWellboreBaseModel
from prodml22.skin_layer2_relative_to_total_thickness import SkinLayer2RelativeToTotalThickness

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiniteRadiusModel(NearWellboreBaseModel):
    """
    Finite radius model with radial flow into wellbore with skin factor.
    """
    skin_layer2_relative_to_total_thickness: Optional[SkinLayer2RelativeToTotalThickness] = field(
        default=None,
        metadata={
            "name": "SkinLayer2RelativeToTotalThickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
