from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.boundary_base_model import BoundaryBaseModel
from prodml22.drainage_area_measured import DrainageAreaMeasured
from prodml22.pore_volume_measured import PoreVolumeMeasured
from prodml22.single_boundary_sub_model import SingleBoundarySubModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class NumericalBoundaryModel(BoundaryBaseModel):
    """
    Numerical boundary model in which any arbitrary outer shape of the
    reservoir boundary can be imposed by use of any number of straight line
    segments which together define the boundary.
    """
    drainage_area_measured: Optional[DrainageAreaMeasured] = field(
        default=None,
        metadata={
            "name": "DrainageAreaMeasured",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    pore_volume_measured: Optional[PoreVolumeMeasured] = field(
        default=None,
        metadata={
            "name": "PoreVolumeMeasured",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    single_boundary_sub_model: List[SingleBoundarySubModel] = field(
        default_factory=list,
        metadata={
            "name": "SingleBoundarySubModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
