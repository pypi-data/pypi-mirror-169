from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.product_volume_balance_event import ProductVolumeBalanceEvent
from prodml22.product_volume_component_content import ProductVolumeComponentContent
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure
from prodml22.volume_value import VolumeValue

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeBalanceDetail:
    """
    Product Volume Balance Detail Schema.

    :ivar owner: A pointer to the business unit which owns the product.
    :ivar source_unit: Points to the business unit from which the
        product originated.
    :ivar share: The owner's share of the product.
    :ivar account_number: An account identifier for the balance.
    :ivar sample_analysis_result: A pointer to a fluid sample analysis
        result object that is relevant to the balance. This sample may
        have been acquired previous to or after this period and is used
        for determining the allocated characteristics.
    :ivar volume_value: A possibly temperature and pressure corrected
        volume value.
    :ivar component_content:
    :ivar event:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    source_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceUnit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    share: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Share",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    account_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "AccountNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    sample_analysis_result: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SampleAnalysisResult",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    volume_value: List[VolumeValue] = field(
        default_factory=list,
        metadata={
            "name": "VolumeValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    component_content: List[ProductVolumeComponentContent] = field(
        default_factory=list,
        metadata={
            "name": "ComponentContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    event: List[ProductVolumeBalanceEvent] = field(
        default_factory=list,
        metadata={
            "name": "Event",
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
