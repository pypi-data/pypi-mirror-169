from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_pta_pressure_data import AbstractPtaPressureData
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DeconvolvedPressureData(AbstractPtaPressureData):
    """
    :ivar deconvolution: In cases where the abstract Pta pressure data
        has type: deconvolved pressure data, this is a reference, using
        data object reference, to the Deconvolution data-object
        containing details of the deconvolution process.
    """
    deconvolution: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Deconvolution",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
