from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.delta_time_storage_changes import DeltaTimeStorageChanges
from prodml22.ratio_initial_to_final_wellbore_storage import RatioInitialToFinalWellboreStorage
from prodml22.wellbore_base_model import WellboreBaseModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ChangingStorageFairModel(WellboreBaseModel):
    """
    Changing wellbore storage model using the Fair model.
    """
    ratio_initial_to_final_wellbore_storage: Optional[RatioInitialToFinalWellboreStorage] = field(
        default=None,
        metadata={
            "name": "RatioInitialToFinalWellboreStorage",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    delta_time_storage_changes: Optional[DeltaTimeStorageChanges] = field(
        default=None,
        metadata={
            "name": "DeltaTimeStorageChanges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
