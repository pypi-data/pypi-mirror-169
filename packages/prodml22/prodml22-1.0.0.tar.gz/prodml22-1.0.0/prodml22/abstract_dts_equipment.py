from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractDtsEquipment:
    """
    The abstract class of equipment in the optical path from which all
    components in the optical path inherit.

    :ivar name: The DTS instrument equipment name.
    :ivar manufacturer: The manufacturer for this item of equipment.
    :ivar manufacturing_date: Date when the equipment (e.g., instrument
        box) was manufactured.
    :ivar type: The type of equipment. This might include the model
        type.
    :ivar supply_date: The date on which this fiber segment was
        supplied.
    :ivar supplier_model_number: The model number (alphanumeric) that is
        used by the supplier to reference the type of fiber that is
        supplied to the user.
    :ivar software_version: Latest known version of the
        software/firmware that is running in the equipment
    :ivar comment: A descriptive remark about the equipment (e.g.,
        optical fiber).
    :ivar supplier: Contact details for the company/person supplying the
        equipment.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    manufacturing_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ManufacturingDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    type: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    supply_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "SupplyDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    supplier_model_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SupplierModelNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    software_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "SoftwareVersion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    supplier: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Supplier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
