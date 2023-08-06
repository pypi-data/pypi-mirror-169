from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_disposition import AbstractDisposition
from prodml22.abstract_product_quantity import AbstractProductQuantity
from prodml22.data_object_reference import DataObjectReference
from prodml22.deferred_production_event import DeferredProductionEvent
from prodml22.injection import Injection
from prodml22.production import Production
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReportingEntityVolumes:
    """Contains all the volumes for a single reporting entity.

    It contains a reference back to the reporting entity using its UUID
    for reference.

    :ivar reporting_entity: Reporting Entity: The top-level entity in
        hierarchy structure.
    :ivar start_date: The starting date of the month.
    :ivar duration: the duration of volume produced at facility
    :ivar opening_inventory:
    :ivar closing_inventory:
    :ivar production: Product volume that is produce from a reporting
        entity.
    :ivar injection: Volume injected per reporting entity.
    :ivar disposition:
    :ivar deferred_production_event: Information about the event or
        incident that caused production to be deferred.
    """
    reporting_entity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReportingEntity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    start_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    duration: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    opening_inventory: List[AbstractProductQuantity] = field(
        default_factory=list,
        metadata={
            "name": "OpeningInventory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    closing_inventory: List[AbstractProductQuantity] = field(
        default_factory=list,
        metadata={
            "name": "ClosingInventory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    production: List[Production] = field(
        default_factory=list,
        metadata={
            "name": "Production",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    injection: List[Injection] = field(
        default_factory=list,
        metadata={
            "name": "Injection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    disposition: List[AbstractDisposition] = field(
        default_factory=list,
        metadata={
            "name": "Disposition",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    deferred_production_event: List[DeferredProductionEvent] = field(
        default_factory=list,
        metadata={
            "name": "DeferredProductionEvent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
