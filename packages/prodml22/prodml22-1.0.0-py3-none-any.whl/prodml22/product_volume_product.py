from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_ref_product_flow import AbstractRefProductFlow
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure
from prodml22.common_properties_product_volume import CommonPropertiesProductVolume
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.name_struct import NameStruct
from prodml22.product_volume_component_content import ProductVolumeComponentContent
from prodml22.product_volume_period import ProductVolumePeriod
from prodml22.reporting_product import ReportingProduct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeProduct:
    """
    Product Volume Product Schema.

    :ivar kind: The type of product that is being reported.
    :ivar name: The name of product that is being reported. This is
        reserved for generic kinds like chemical.
    :ivar split_factor: This factor describes the fraction of fluid in
        the source flow that is allocated to this product stream. The
        volumes reported here are derived from the source flow based on
        this split factor. This should be an allocation flow.
    :ivar mass_fraction: The weight fraction of the product.
    :ivar mole_fraction: The mole fraction of the product.
    :ivar component_content: The relative amount of a component product
        in the product stream.
    :ivar source_flow:
    :ivar period: Product amounts for a specific period.
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
    name: Optional[NameStruct] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    split_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "SplitFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
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
    component_content: List[ProductVolumeComponentContent] = field(
        default_factory=list,
        metadata={
            "name": "ComponentContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    source_flow: Optional[AbstractRefProductFlow] = field(
        default=None,
        metadata={
            "name": "SourceFlow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    period: List[ProductVolumePeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
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
