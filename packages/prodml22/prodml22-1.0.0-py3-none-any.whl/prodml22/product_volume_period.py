from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_date_time_class import AbstractDateTimeType
from prodml22.common_properties_product_volume import CommonPropertiesProductVolume
from prodml22.dated_comment import DatedComment
from prodml22.product_volume_alert import ProductVolumeAlert
from prodml22.product_volume_balance_set import ProductVolumeBalanceSet
from prodml22.product_volume_component_content import ProductVolumeComponentContent
from prodml22.reporting_duration_kind import ReportingDurationKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumePeriod:
    """
    Product Volume Period Schema.

    :ivar kind: The type of period that is being reported. If not
        specified and a time is not given then the period is defined by
        the reporting period.
    :ivar comment: A time-stamped remark about the amounts.
    :ivar balance_set: Provides the sales context for this period.
    :ivar component_content: The relative amount of a component product
        in the product stream.
    :ivar properties:
    :ivar alert: An indication of some sort of abnormal condition
        relative the values in this period.
    :ivar date_time:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    kind: Optional[ReportingDurationKind] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    comment: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    balance_set: List[ProductVolumeBalanceSet] = field(
        default_factory=list,
        metadata={
            "name": "BalanceSet",
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
    properties: Optional[CommonPropertiesProductVolume] = field(
        default=None,
        metadata={
            "name": "Properties",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    alert: Optional[ProductVolumeAlert] = field(
        default=None,
        metadata={
            "name": "Alert",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    date_time: Optional[AbstractDateTimeType] = field(
        default=None,
        metadata={
            "name": "DateTime",
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
