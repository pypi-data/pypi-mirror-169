from __future__ import annotations
from dataclasses import dataclass
from prodml22.instrument import Instrument

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberOtdrinstrumentBox(Instrument):
    """
    Information about an OTDR instrument box taht is used to perform OTDR
    surveys on the optical path.
    """
    class Meta:
        name = "FiberOTDRInstrumentBox"
