from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.fracture_conductivity import FractureConductivity
from prodml22.resqml_model_ref import ResqmlModelRef
from prodml22.transmissibility_reduction_factor_of_linear_front import TransmissibilityReductionFactorOfLinearFront

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InternalFaultSubModel:
    """Internal Fault sub model describes each internal fault within the
    reservoir.

    There will be as many instances of this as there are internal
    faults.  This is expected to be a numerical model.

    :ivar is_leaky: Boolean - value of True means that the fault is
        leaky and therefore that the parameter Leakage should be used to
        quantify this.
    :ivar transmissibility_reduction_ratio_of_linear_front: The
        transmissibility reduction factor of a fault in a Linear
        Composite model where the boundary of the inner and outer zones
        is a leaky fault. If T is the complete transmissibility which
        would be computed without any fault between point A and point B
        (T is a function of permeability, etc), then Tf = T * leakage.
        Therefore: leakage = 1 implies that the fault is not a barrier
        to flow at all, leakage = 0 implies that the fault is sealing
        (no transmissibility anymore at all between points A and B).
    :ivar is_conductive: Boolean - value of True means that the fault is
        conductive. If the boolean IsFiniteConductive is also True, then
        the parameter Conductivity should be used to quantify this. If
        IsFiniteConductive is False, then the fault is regarded as
        infinite conductive, and the parameter Conductivity is not
        required.
    :ivar is_finite_conductive: Boolean - value of True means that the
        fault is finite conductive and the parameter Conductivity should
        be used to quantify this. If IsFiniteConductive is False, then
        the fault is regarded as infinite conductive, and the parameter
        Conductivity is not required.
    :ivar conductivity: For a finite conductivity fault, the
        conductivity of the fault (which may be regarded as a fracture),
        equal to Fracture Width * Fracture Permeability.
    :ivar fault_ref_id: The reference to a RESQML model representation
        of this fault.
    """
    is_leaky: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsLeaky",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    transmissibility_reduction_ratio_of_linear_front: Optional[TransmissibilityReductionFactorOfLinearFront] = field(
        default=None,
        metadata={
            "name": "TransmissibilityReductionRatioOfLinearFront ",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    is_conductive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsConductive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    is_finite_conductive: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFiniteConductive",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    conductivity: Optional[FractureConductivity] = field(
        default=None,
        metadata={
            "name": "Conductivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
