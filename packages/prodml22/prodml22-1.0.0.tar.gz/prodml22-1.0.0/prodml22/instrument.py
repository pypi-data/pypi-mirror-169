from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_dts_equipment import AbstractDtsEquipment
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Instrument(AbstractDtsEquipment):
    """
    The general class of an instrument, including vendor information, in the
    installed system.

    :ivar instrument_vendor: Contact information for the person/company
        that provided the equipment
    """
    instrument_vendor: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InstrumentVendor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
