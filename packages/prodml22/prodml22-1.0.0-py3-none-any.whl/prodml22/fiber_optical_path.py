from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_object import AbstractObject
from prodml22.data_object_reference import DataObjectReference
from prodml22.facility_identifier import FacilityIdentifier
from prodml22.fiber_facility_mapping import FiberFacilityMapping
from prodml22.fiber_optical_path_inventory import FiberOpticalPathInventory
from prodml22.fiber_optical_path_network import FiberOpticalPathNetwork
from prodml22.fiber_path_defect import FiberPathDefect

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberOpticalPath(AbstractObject):
    """The optical fiber path used for distributed property surveys, e.g.
    temperature (DTS) or acoustics (DAS).

    Comprises a number of items of equipment, such as fiber segments and
    connectors of various types.

    :ivar inventory: The list of equipment used in the optical path.
        Equipment may be used in the optical path for different periods
        of time, so this inventory contains all items of equipment which
        are used at some period of time.
    :ivar optical_path_network:
    :ivar facility_mapping: Relates distances measured along the optical
        path to specific lengths along facilities (wellbores or
        pipelines).
    :ivar defect: A zone of the fibre which has defective optical
        properties (e.g., darkening).
    :ivar otdr: This records the result arrays along with context
        information for an Optical Time Domain Reflectometry (OTDR)
        survey. The arrays will define the relative scattered power from
        the Rayleigh scattering vs distance along the fiber. The actual
        data values are recorded in a OTDR file and/or image file, which
        are referenced in subelements.
    :ivar installing_vendor: The vendor who performed the physical
        deployment
    :ivar facility_identifier: Contains details about the facility being
        surveyed, such as name, geographical data, etc.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/prodmlv2"

    inventory: Optional[FiberOpticalPathInventory] = field(
        default=None,
        metadata={
            "name": "Inventory",
            "type": "Element",
            "required": True,
        }
    )
    optical_path_network: List[FiberOpticalPathNetwork] = field(
        default_factory=list,
        metadata={
            "name": "OpticalPathNetwork",
            "type": "Element",
        }
    )
    facility_mapping: List[FiberFacilityMapping] = field(
        default_factory=list,
        metadata={
            "name": "FacilityMapping",
            "type": "Element",
        }
    )
    defect: List[FiberPathDefect] = field(
        default_factory=list,
        metadata={
            "name": "Defect",
            "type": "Element",
        }
    )
    otdr: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Otdr",
            "type": "Element",
        }
    )
    installing_vendor: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InstallingVendor",
            "type": "Element",
        }
    )
    facility_identifier: Optional[FacilityIdentifier] = field(
        default=None,
        metadata={
            "name": "FacilityIdentifier",
            "type": "Element",
        }
    )
