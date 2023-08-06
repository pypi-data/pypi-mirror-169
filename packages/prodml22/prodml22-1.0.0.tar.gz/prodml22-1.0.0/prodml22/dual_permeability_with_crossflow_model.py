from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.interporosity_flow_parameter import InterporosityFlowParameter
from prodml22.layer2_thickness import Layer2Thickness
from prodml22.ratio_layer1_to_total_permeability_thickness_product import RatioLayer1ToTotalPermeabilityThicknessProduct
from prodml22.reservoir_base_model import ReservoirBaseModel
from prodml22.storativity_ratio import StorativityRatio

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DualPermeabilityWithCrossflowModel(ReservoirBaseModel):
    """
    Dual Permeability reservoir model, with Cross-Flow between the two layers.
    """
    interporosity_flow_parameter: Optional[InterporosityFlowParameter] = field(
        default=None,
        metadata={
            "name": "InterporosityFlowParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    storativity_ratio: Optional[StorativityRatio] = field(
        default=None,
        metadata={
            "name": "StorativityRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    ratio_layer1_to_total_permeability_thickness_product: Optional[RatioLayer1ToTotalPermeabilityThicknessProduct] = field(
        default=None,
        metadata={
            "name": "RatioLayer1ToTotalPermeabilityThicknessProduct",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    layer2_thickness: Optional[Layer2Thickness] = field(
        default=None,
        metadata={
            "name": "Layer2Thickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
