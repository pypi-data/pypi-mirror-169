from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.distance_mid_fracture_height_to_bottom_boundary import DistanceMidFractureHeightToBottomBoundary
from prodml22.fracture_conductivity import FractureConductivity
from prodml22.fracture_face_skin import FractureFaceSkin
from prodml22.fracture_height import FractureHeight
from prodml22.fracture_model_type import FractureModelType
from prodml22.fracture_storativity_ratio import FractureStorativityRatio
from prodml22.location_in2_d import LocationIn2D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SingleFractureSubModel:
    """For a Horizontal Wellbore Multiple Variable Fractured Model, this is the
    model sub class which describes each fracture.

    There will be as many instances of this as there are fractures. This
    is expected to be a numerical model.

    :ivar fracture_tip1_location: The location of the first tip of the
        fracture in the local CRS.
    :ivar fracture_tip2_location: The location of the second tip of the
        fracture (opposite side of the wellbore to the first) in the
        local CRS.
    :ivar fracture_height: In the vertical hydraulic fracture model
        (where the wellbore is horizontal), the height of the fracture.
        In the case of a horizontal wellbore, the fractures are assumed
        to extend an equal distance above and below the wellbore.
    :ivar distance_mid_fracture_height_to_bottom_boundary: For a
        hydraulic fracture, the distance between the mid-height level of
        the fracture and the lower boundary of the layer.
    :ivar fracture_face_skin: Dimensionless value, characterizing the
        restriction to flow (+ve value, damage) or additional capacity
        for flow (-ve value, eg acidized) due to effective permeability
        across the face of a hydraulic fracture, ie controlling flow
        from reservoir into fracture. This value is stated with respect
        to radial flow using the full reservoir thickness (h), ie the
        radial flow or middle time region of a pressure transient. It
        therefore can be added, in a fractured well, to
        "ConvergenceSkinRelativeToTotalThickness" skin to yield
        "SkinRelativeToTotalThickness".
    :ivar fracture_conductivity: For an induced hydraulic fracture, the
        conductivity of the fracture, equal to Fracture Width * Fracture
        Permeability
    :ivar fracture_storativity_ratio: Dimensionless Value characterizing
        the fraction of the pore volume occupied by the fractures to the
        total of pore volume of (fractures plus reservoir).
    :ivar fracture_model_type: For a Horizontal Wellbore Multiple
        Fractured Model, the model type which applies to this fracture.
        Enumeration with choices of infinite conductivity, uniform flux,
        finite conductivity, or compressible fracture finite
        conductivity.
    """
    fracture_tip1_location: Optional[LocationIn2D] = field(
        default=None,
        metadata={
            "name": "FractureTip1Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fracture_tip2_location: Optional[LocationIn2D] = field(
        default=None,
        metadata={
            "name": "FractureTip2Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    fracture_height: Optional[FractureHeight] = field(
        default=None,
        metadata={
            "name": "FractureHeight",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    distance_mid_fracture_height_to_bottom_boundary: Optional[DistanceMidFractureHeightToBottomBoundary] = field(
        default=None,
        metadata={
            "name": "DistanceMidFractureHeightToBottomBoundary",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_face_skin: Optional[FractureFaceSkin] = field(
        default=None,
        metadata={
            "name": "FractureFaceSkin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_conductivity: Optional[FractureConductivity] = field(
        default=None,
        metadata={
            "name": "FractureConductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_storativity_ratio: Optional[FractureStorativityRatio] = field(
        default=None,
        metadata={
            "name": "FractureStorativityRatio",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fracture_model_type: Optional[FractureModelType] = field(
        default=None,
        metadata={
            "name": "FractureModelType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
