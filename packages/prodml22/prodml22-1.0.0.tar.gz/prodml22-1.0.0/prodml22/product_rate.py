from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.flow_rate_value import FlowRateValue
from prodml22.mass_per_time_measure import MassPerTimeMeasure
from prodml22.product_fluid_kind import ProductFluidKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductRate:
    """
    The production rate of the product.

    :ivar product_fluid_kind: Information about the product that the
        product quantity represents. See enum ProductFluidKind (in the
        ProdmlCommon package).
    :ivar mass_flow_rate: Mass flow rate.
    :ivar volume_flow_rate: Volume flow rate.
    :ivar remark: Remarks and comments about this data item.
    :ivar product_fluid_reference: A reference (using uid) to a fluid
        component contained in the Fluid Component Catalog.
    """
    product_fluid_kind: Optional[Union[ProductFluidKind, str]] = field(
        default=None,
        metadata={
            "name": "ProductFluidKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    mass_flow_rate: Optional[MassPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "MassFlowRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    volume_flow_rate: Optional[FlowRateValue] = field(
        default=None,
        metadata={
            "name": "VolumeFlowRate",
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
    product_fluid_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProductFluidReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
