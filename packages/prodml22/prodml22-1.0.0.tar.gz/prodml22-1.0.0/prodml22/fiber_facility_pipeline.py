from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_fiber_facility import AbstractFiberFacility
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.name_struct import NameStruct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberFacilityPipeline(AbstractFiberFacility):
    """
    If facility mapping is to a pipeline, this element shows what optical path
    distances map to pipeline lengths.

    :ivar name: The name of this facilityMapping instance.
    :ivar datum_port_reference: A description of which "port" (i.e.,
        connection/end or defined point on a pipeline) the
        facilityLength is indexed from.
    :ivar installation: The name of the facility that is represented by
        this facilityMapping.
    :ivar kind: The kind of facility mapped to the optical path.
        Expected to be a pipeline, but this element can be used to show
        other facilities being mapped to fiber length in future.
    :ivar context_facility: The name and type of a facility whose
        context is relevant to the represented installation.
    """
    name: Optional[NameStruct] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    datum_port_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "DatumPortReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    installation: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Installation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    kind: Optional[str] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    context_facility: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "ContextFacility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
