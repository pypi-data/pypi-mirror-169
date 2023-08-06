from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dated_comment import DatedComment
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.name_struct import NameStruct
from prodml22.product_volume_flow import ProductVolumeFlow
from prodml22.product_volume_parameter_set import ProductVolumeParameterSet
from prodml22.time_measure import TimeMeasure
from prodml22.volume_measure import VolumeMeasure
from prodml22.well_fluid import WellFluid
from prodml22.well_operation_method import WellOperationMethod
from prodml22.well_status import WellStatus

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeFacility:
    """
    Report Facility Schema.

    :ivar facility_parent: Facility parent.
    :ivar facility_parent2: Facility parent2.
    :ivar facility_alias: An alternative name of a facility. This is
        generally unique within a naming system. The above contextually
        unique name (that is, within the context of a parent) should
        also be listed as an alias.
    :ivar unit: Unit.
    :ivar net_work: Network.
    :ivar name: The name of the facility. The name can be qualified by a
        naming system. This also defines the kind of facility.
    :ivar status_well: Status of the well.
    :ivar fluid_well: POSC well fluid. The type of fluid being produced
        from or injected into a well facility.
    :ivar operating_method: The lift method being used to operate the
        well.
    :ivar well_producing: True (or 1) indicates that the well is
        producing. False (or 0) or not given indicates that the well is
        not producing. This only applies if the facility is a well or
        wellbore.
    :ivar well_injecting: True (or 1) indicates that the well is
        injecting. False (or 0) or not given indicates that the well is
        not injecting. This only applies if the facility is a well or
        wellbore.
    :ivar capacity: The storage capacity of the facility (e.g., a tank).
    :ivar operation_time: The amount of time that the facility was
        active during the reporting period.
    :ivar flow: Reports a flow of a product.
    :ivar parameter_set:
    :ivar comment:
    :ivar downtime_reason:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    facility_parent: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "FacilityParent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    facility_parent2: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "FacilityParent2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    facility_alias: List[NameStruct] = field(
        default_factory=list,
        metadata={
            "name": "FacilityAlias",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    net_work: Optional[str] = field(
        default=None,
        metadata={
            "name": "NetWork",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    name: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    status_well: Optional[WellStatus] = field(
        default=None,
        metadata={
            "name": "StatusWell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_well: Optional[WellFluid] = field(
        default=None,
        metadata={
            "name": "FluidWell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    operating_method: Optional[WellOperationMethod] = field(
        default=None,
        metadata={
            "name": "OperatingMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    well_producing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WellProducing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    well_injecting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WellInjecting",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    capacity: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Capacity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    operation_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "OperationTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flow: List[ProductVolumeFlow] = field(
        default_factory=list,
        metadata={
            "name": "Flow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    parameter_set: List[ProductVolumeParameterSet] = field(
        default_factory=list,
        metadata={
            "name": "ParameterSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    comment: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    downtime_reason: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "DowntimeReason",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
