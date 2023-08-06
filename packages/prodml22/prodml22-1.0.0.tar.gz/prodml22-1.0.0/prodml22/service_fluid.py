from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_product_quantity import AbstractProductQuantity
from prodml22.service_fluid_kind import ServiceFluidKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ServiceFluid(AbstractProductQuantity):
    """
    Service fluid (e.g., biocides, lubricants, etc.) being reported on.

    :ivar service_fluid_kind: Indicates the kind of service fluid. See
        enum ServiceFluidKind (in ProdmlCommon).
    :ivar service_fluid_reference: String ID that points to a service
        fluid in the FluidComponentSet.
    """
    service_fluid_kind: Optional[Union[ServiceFluidKind, str]] = field(
        default=None,
        metadata={
            "name": "ServiceFluidKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    service_fluid_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "serviceFluidReference",
            "type": "Attribute",
            "max_length": 64,
        }
    )
