from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.resqml_model_ref import ResqmlModelRef

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DistributedParametersSubModel:
    """For a Reservoir model in which parameters are spatially distributed,
    this is the model sub class which identifies which parameters have been
    spatially sampled, and provides a reference to the RESQML object containing
    the sampled data.

    This is expected to be a numerical model.

    :ivar is_permeability_gridded: Boolean. If True then parameter
        Permeability is defined by values distributed on a grid in a
        RESQML model.  In this case the PermeabilityArrayRefIDelement
        will provide the location of the gridded properties in the
        RESQML model.
    :ivar permeability_array_ref_id: Reference to RESQML grid containing
        Permeability values.
    :ivar is_thickness_gridded: Boolean. If True then parameter
        Thickness is defined by values distributed on a grid in a RESQML
        model.  In this case the ThicknessArrayRefID element will
        provide the location of the gridded properties in the RESQML
        model.
    :ivar thickness_array_ref_id: Reference to RESQML grid containing
        Thickness values.
    :ivar is_porosity_gridded: Boolean. If True then parameter Porosity
        is defined by values distributed on a grid in a RESQML model.
        In this case the PorosityArrayRefID element will provide the
        location of the gridded properties in the RESQML model.
    :ivar porosity_array_ref_id: Reference to RESQML grid containing
        Porosity values.
    :ivar is_depth_gridded: Boolean. If True then parameter Depth is
        defined by values distributed on a grid in a RESQML model.  In
        this case the DepthArrayRefID element will provide the location
        of the gridded properties in the RESQML model.
    :ivar depth_array_ref_id: Reference to RESQML grid containing Depth
        values.
    :ivar is_kv_to_kr_gridded: Boolean. If True then parameter KvToKr is
        defined by values distributed on a grid in a RESQML model.  In
        this case the KvToKrArrayRefID element will provide the location
        of the gridded properties in the RESQML model.
    :ivar kv_to_kr_array_ref_id: Reference to RESQML grid containing
        KvToKr values.
    :ivar is_kx_to_ky_gridded: Boolean. If True then parameter KxToKy is
        defined by values distributed on a grid in a RESQML model.  In
        this case the KxToKyArrayRefID element will provide the location
        of the gridded properties in the RESQML model.
    :ivar kx_to_ky_array_ref_id: Reference to RESQML grid containing
        KxToKy values.
    """
    is_permeability_gridded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPermeabilityGridded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    permeability_array_ref_id: Optional[ResqmlModelRef] = field(
        default=None,
        metadata={
            "name": "PermeabilityArrayRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    is_thickness_gridded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsThicknessGridded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    thickness_array_ref_id: Optional[ResqmlModelRef] = field(
        default=None,
        metadata={
            "name": "ThicknessArrayRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    is_porosity_gridded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsPorosityGridded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    porosity_array_ref_id: Optional[ResqmlModelRef] = field(
        default=None,
        metadata={
            "name": "PorosityArrayRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    is_depth_gridded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDepthGridded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    depth_array_ref_id: Optional[ResqmlModelRef] = field(
        default=None,
        metadata={
            "name": "DepthArrayRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    is_kv_to_kr_gridded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsKvToKrGridded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    kv_to_kr_array_ref_id: Optional[ResqmlModelRef] = field(
        default=None,
        metadata={
            "name": "KvToKrArrayRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    is_kx_to_ky_gridded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsKxToKyGridded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    kx_to_ky_array_ref_id: Optional[ResqmlModelRef] = field(
        default=None,
        metadata={
            "name": "KxToKyArrayRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
