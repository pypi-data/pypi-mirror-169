from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.horizontal_radial_permeability import HorizontalRadialPermeability
from prodml22.location_in2_d import LocationIn2D
from prodml22.porosity import Porosity
from prodml22.total_thickness import TotalThickness

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ReservoirZoneSubModel:
    """Enables a zone within the reservoir model to be defined.

    This will have local properties which may vary from the rest of the
    reservoir model.  The zone is bounded by a polygon comprising a
    number of 2D points. It is left to the software application to
    verify these comprise a closed polygon, within which the zone
    properties apply.

    :ivar bounding_polygon_point: The zone is bounded by a polygon
        comprising a number of 2D points, each one is represented by
        this 2D coordinate pair.
    :ivar permeability: Horizontal Permeability within this zone. Note
        that this value should be used to represent any mobility changes
        in the zone, which may be due to effective permeability and
        viscosity changeds, eg for the inner region of an injection
        well.  If absent, the zone is assumed to have the same property
        as the overall reservoir model.
    :ivar porosity: Porosity within this zone.  If absent, the zone is
        assumed to have the same property as the overall reservoir
        model.
    :ivar thickness: Thickness within this zone.  If absent, the zone is
        assumed to have the same property as the overall reservoir
        model.
    """
    bounding_polygon_point: List[LocationIn2D] = field(
        default_factory=list,
        metadata={
            "name": "BoundingPolygonPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
    permeability: Optional[HorizontalRadialPermeability] = field(
        default=None,
        metadata={
            "name": "Permeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    porosity: Optional[Porosity] = field(
        default=None,
        metadata={
            "name": "Porosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    thickness: Optional[TotalThickness] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
