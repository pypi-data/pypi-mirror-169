from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.production_operation_alarm import ProductionOperationAlarm
from prodml22.production_operation_cargo_ship_operation import ProductionOperationCargoShipOperation
from prodml22.production_operation_lost_production import ProductionOperationLostProduction
from prodml22.production_operation_marine_operation import ProductionOperationMarineOperation
from prodml22.production_operation_operational_comment import ProductionOperationOperationalComment
from prodml22.production_operation_shutdown import ProductionOperationShutdown
from prodml22.production_operation_water_cleaning_quality import ProductionOperationWaterCleaningQuality

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationActivity:
    """
    Production Activity Schema.

    :ivar water_cleaning_quality: Information about the contaminants in
        water, and the general water quality.
    :ivar marine_operation: Information about a marine operation.
    :ivar cargo_ship_operation: Information about a cargo operation.
    :ivar shutdown: Infomation about a shutdown event.
    :ivar operational_comment: A comment about a kind of operation. The
        time of the operation can be specified.
    :ivar alarm: Infomation about an alarm.
    :ivar lost_production: Infomation about a lost production.
    :ivar lost_injection: Infomation about a lost injection.
    """
    water_cleaning_quality: List[ProductionOperationWaterCleaningQuality] = field(
        default_factory=list,
        metadata={
            "name": "WaterCleaningQuality",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    marine_operation: List[ProductionOperationMarineOperation] = field(
        default_factory=list,
        metadata={
            "name": "MarineOperation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cargo_ship_operation: List[ProductionOperationCargoShipOperation] = field(
        default_factory=list,
        metadata={
            "name": "CargoShipOperation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    shutdown: List[ProductionOperationShutdown] = field(
        default_factory=list,
        metadata={
            "name": "Shutdown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    operational_comment: List[ProductionOperationOperationalComment] = field(
        default_factory=list,
        metadata={
            "name": "OperationalComment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    alarm: List[ProductionOperationAlarm] = field(
        default_factory=list,
        metadata={
            "name": "Alarm",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    lost_production: Optional[ProductionOperationLostProduction] = field(
        default=None,
        metadata={
            "name": "LostProduction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    lost_injection: Optional[ProductionOperationLostProduction] = field(
        default=None,
        metadata={
            "name": "LostInjection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
