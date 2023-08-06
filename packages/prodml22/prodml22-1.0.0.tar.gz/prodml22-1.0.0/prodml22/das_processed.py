from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from prodml22.das_fbe import DasFbe
from prodml22.das_spectra import DasSpectra

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasProcessed:
    """This object contains data objects for processed data types and has no
    data attributes.

    Currently only two processed data types have been defined: the
    frequency band extracted (FBE) and spectra. In the future other
    processed data types may be added. Note that a DasProcessed object
    is optional and only present if DAS FBE or DAS spectra data is
    exchanged.
    """
    fbe: List[DasFbe] = field(
        default_factory=list,
        metadata={
            "name": "Fbe",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    spectra: List[DasSpectra] = field(
        default_factory=list,
        metadata={
            "name": "Spectra",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
