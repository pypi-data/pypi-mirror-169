from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidSampleContainer(AbstractObject):
    """
    Information about the fluid container used to capture a fluid sample.

    :ivar make: The make of this fluid sample container.
    :ivar model: The model of this fluid sample container.
    :ivar serial_number: The serial number of this fluid sample
        container.
    :ivar bottle_id: The reference ID  of a bottle or a chamber.
    :ivar capacity: The volume of a bottle or chamber.
    :ivar owner: The owner of this fluid sample container.
    :ivar kind: The kind of this fluid sample container.
    :ivar metallurgy: The metallurgy of this fluid sample container.
    :ivar pressure_rating: The pressure rating of this fluid sample
        container.
    :ivar temperature_rating: The temperature rating of this fluid
        sample container.
    :ivar last_inspection_date: The date when this fluid sample
        container was last inspected.
    :ivar transport_certificate_reference: The reference uid of an
        attached object which stores the transport certificate.
    :ivar remark: Remarks and comments about this data item.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    make: Optional[str] = field(
        default=None,
        metadata={
            "name": "Make",
            "type": "Element",
            "max_length": 64,
        }
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Element",
            "max_length": 64,
        }
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SerialNumber",
            "type": "Element",
            "max_length": 64,
        }
    )
    bottle_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "BottleID",
            "type": "Element",
            "max_length": 64,
        }
    )
    capacity: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Capacity",
            "type": "Element",
        }
    )
    owner: Optional[str] = field(
        default=None,
        metadata={
            "name": "Owner",
            "type": "Element",
            "max_length": 64,
        }
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "max_length": 64,
        }
    )
    metallurgy: Optional[str] = field(
        default=None,
        metadata={
            "name": "Metallurgy",
            "type": "Element",
            "max_length": 64,
        }
    )
    pressure_rating: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "PressureRating",
            "type": "Element",
        }
    )
    temperature_rating: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TemperatureRating",
            "type": "Element",
        }
    )
    last_inspection_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "LastInspectionDate",
            "type": "Element",
        }
    )
    transport_certificate_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TransportCertificateReference",
            "type": "Element",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_length": 2000,
        }
    )
