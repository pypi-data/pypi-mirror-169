from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pta_flow_data import AbstractPtaFlowData
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PreProcessedFlowData(AbstractPtaFlowData):
    """
    :ivar pre_process: In cases where the abstract Pta pressure data has
        type: deconvolved pressure data, this is a reference, using data
        object reference, to the PtaDataPreProcess data-object
        containing details of the pre-processing applied.
    """
    pre_process: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PreProcess",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
