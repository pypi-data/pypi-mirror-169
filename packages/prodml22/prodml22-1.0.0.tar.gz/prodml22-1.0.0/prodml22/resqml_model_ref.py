from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ResqmlModelRef:
    """
    A reference to a RESQML Model element containing the data relating to the
    PTA object concerned.

    :ivar resqml_model_ref: Reference to the RESQML model element which
        represents this feature.
    """
    resqml_model_ref: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ResqmlModelRef",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
