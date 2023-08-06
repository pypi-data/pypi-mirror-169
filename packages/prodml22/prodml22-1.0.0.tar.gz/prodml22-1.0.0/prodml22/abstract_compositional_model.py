from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pvt_model import AbstractPvtModel
from prodml22.binary_interaction_coefficient_set import BinaryInteractionCoefficientSet
from prodml22.component_property_set import ComponentPropertySet
from prodml22.mixing_rule import MixingRule

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractCompositionalModel(AbstractPvtModel):
    """
    Abstract class of compositional model.

    :ivar mixing_rule: The mixing rule which was applied in the
        compositional model. Enum. See mixing rule.
    :ivar component_property_set: Component property set.
    :ivar binary_interaction_coefficient_set: Binary interaction
        coefficient set.
    """
    mixing_rule: Optional[MixingRule] = field(
        default=None,
        metadata={
            "name": "MixingRule",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    component_property_set: Optional[ComponentPropertySet] = field(
        default=None,
        metadata={
            "name": "ComponentPropertySet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    binary_interaction_coefficient_set: Optional[BinaryInteractionCoefficientSet] = field(
        default=None,
        metadata={
            "name": "BinaryInteractionCoefficientSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
