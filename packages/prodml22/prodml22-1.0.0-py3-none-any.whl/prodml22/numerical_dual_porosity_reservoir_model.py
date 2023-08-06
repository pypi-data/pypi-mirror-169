from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.distributed_parameters_sub_model import DistributedParametersSubModel
from prodml22.internal_fault_sub_model import InternalFaultSubModel
from prodml22.interporosity_flow_parameter import InterporosityFlowParameter
from prodml22.reservoir_base_model import ReservoirBaseModel
from prodml22.reservoir_zone_sub_model import ReservoirZoneSubModel
from prodml22.storativity_ratio import StorativityRatio

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class NumericalDualPorosityReservoirModel(ReservoirBaseModel):
    """Numerical model with dual porosity reservoir.

    This model may have constant value or reference a grid of
    geometrically distributed values for the following parameters:
    permeability (k), thickness (h), porosity (phi), depth (Z), vertical
    anisotropy (KvToKr) and horizontal anisotropy (KyTokx).  Internal
    faults can be positioned in this reservoir.
    """
    interporosity_flow_parameter: Optional[InterporosityFlowParameter] = field(
        default=None,
        metadata={
            "name": "InterporosityFlowParameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    storativity_ratio: Optional[StorativityRatio] = field(
        default=None,
        metadata={
            "name": "StorativityRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    internal_fault_sub_model: List[InternalFaultSubModel] = field(
        default_factory=list,
        metadata={
            "name": "InternalFaultSubModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    distributed_parameters_sub_model: Optional[DistributedParametersSubModel] = field(
        default=None,
        metadata={
            "name": "DistributedParametersSubModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    reservoir_zone_sub_model: List[ReservoirZoneSubModel] = field(
        default_factory=list,
        metadata={
            "name": "ReservoirZoneSubModel",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
