from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.common_properties_product_volume import CommonPropertiesProductVolume
from prodml22.reporting_product import ReportingProduct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeComponentContent:
    """
    Product Volume Component Content Schema.

    :ivar kind: The type of product whose relative content is being
        described. This should be a specific component (e.g., water)
        rather than a phase (e.g., aqueous).
    :ivar reference_kind: The type of product to which the product is
        being compared. If not given then the product is being compared
        against the overall flow stream.
    :ivar properties:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    kind: Optional[ReportingProduct] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    reference_kind: Optional[ReportingProduct] = field(
        default=None,
        metadata={
            "name": "ReferenceKind",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
