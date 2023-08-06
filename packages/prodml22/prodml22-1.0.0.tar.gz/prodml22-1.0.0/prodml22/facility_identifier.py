from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.geographic_context import GeographicContext
from prodml22.name_struct import NameStruct
from prodml22.product_volume_business_unit import ProductVolumeBusinessUnit

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FacilityIdentifier:
    """
    Contains details about the facility being surveyed, such as name,
    geographical data, etc.

    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    :ivar content:
    """
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Name",
                    "type": NameStruct,
                    "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
                },
                {
                    "name": "Installation",
                    "type": FacilityIdentifierStruct,
                    "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
                },
                {
                    "name": "Kind",
                    "type": str,
                    "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
                    "max_length": 64,
                },
                {
                    "name": "ContextFacility",
                    "type": FacilityIdentifierStruct,
                    "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
                },
                {
                    "name": "BusinessUnit",
                    "type": ProductVolumeBusinessUnit,
                    "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
                },
                {
                    "name": "Operator",
                    "type": DataObjectReference,
                    "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
                },
                {
                    "name": "GeographicContext",
                    "type": GeographicContext,
                    "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
                },
            ),
        }
    )
