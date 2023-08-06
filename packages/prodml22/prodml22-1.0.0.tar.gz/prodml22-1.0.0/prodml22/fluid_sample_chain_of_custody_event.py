from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.data_object_reference import DataObjectReference
from prodml22.sample_action import SampleAction
from prodml22.sample_quality import SampleQuality
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSampleChainOfCustodyEvent:
    """
    Fluid sample custody history event.

    :ivar transfer_volume: The transfer volume for this chain of custody
        event.
    :ivar transfer_pressure: The transfer pressure for this chain of
        custody event.
    :ivar transfer_temperature: The transfer temperature for this chain
        of custody event.
    :ivar sample_integrity: The sample integrity for this chain of
        custody event. Enum. See sample quality.
    :ivar remaining_volume: The remaining volume of sample for this
        chain of custody event.
    :ivar lost_volume: The lost volume of sample for this chain of
        custody event.
    :ivar custody_date: The date for this chain of custody event.
    :ivar custody_action: The action for this chain of custody event.
        Enum. See sample action.
    :ivar custodian: The custodian for this chain of custody event.
    :ivar container_location: The container location for this chain of
        custody event.
    :ivar remark: Remarks and comments about this data item.
    :ivar prev_container:
    :ivar current_container:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    transfer_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "TransferVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    transfer_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "TransferPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    transfer_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TransferTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    sample_integrity: Optional[SampleQuality] = field(
        default=None,
        metadata={
            "name": "SampleIntegrity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    remaining_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "RemainingVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    lost_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "LostVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    custody_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CustodyDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    custody_action: Optional[SampleAction] = field(
        default=None,
        metadata={
            "name": "CustodyAction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    custodian: Optional[str] = field(
        default=None,
        metadata={
            "name": "Custodian",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    container_location: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContainerLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    prev_container: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PrevContainer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    current_container: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CurrentContainer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
