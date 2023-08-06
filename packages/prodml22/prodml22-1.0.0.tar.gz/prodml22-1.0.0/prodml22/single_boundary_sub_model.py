from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.boundary1_type import Boundary1Type
from prodml22.resqml_model_ref import ResqmlModelRef

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SingleBoundarySubModel:
    """For a Boundary model which has an arbitrary number, orientation and type
    of external boundaries, this is the model sub class which describes each
    boundary.

    There will be as many instances of this as there are boundaries.
    This is expected to be a numerical model. The other, regular
    geometries of boundaries may well be represented by analytical
    models.

    :ivar type_of_boundary: In any bounded reservoir model, the type of
        Boundary 1. Enumeration with choice of "no-flow" or "constant
        pressure".
    :ivar fault_ref_id: The reference to a RESQML model representation
        of this fault.
    """
    type_of_boundary: Optional[Boundary1Type] = field(
        default=None,
        metadata={
            "name": "TypeOfBoundary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fault_ref_id: Optional[ResqmlModelRef] = field(
        default=None,
        metadata={
            "name": "FaultRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
