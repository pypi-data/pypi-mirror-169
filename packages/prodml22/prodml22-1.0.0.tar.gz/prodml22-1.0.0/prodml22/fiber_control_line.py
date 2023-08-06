from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_cable import AbstractCable
from prodml22.control_line_encapsulation_kind import ControlLineEncapsulationKind
from prodml22.control_line_encapsulation_size import ControlLineEncapsulationSize
from prodml22.control_line_material import ControlLineMaterial
from prodml22.control_line_size import ControlLineSize
from prodml22.fiber_pump_activity import FiberPumpActivity

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberControlLine(AbstractCable):
    """
    Information regarding the control line into which a fiber cable may be
    pumped to measure a facility.

    :ivar size: Enum of the common sizes of control line. The enum list
        gives diameters and weight per length values. A fiber may be
        installed inside the control line.
    :ivar material: Enum of the common materials from which a control
        line may be made. A fiber may be installed inside the control
        line.
    :ivar encapsulation_type: Enum of square or round encapsulation for
        a control line. A fiber may be installed inside the control
        line.
    :ivar encapsulation_size: Enum of the size of encapsulation of a
        fiber within a control line.
    :ivar comment: A descriptive remark about the fiber control line.
    :ivar pump_activity: The activity of pumping the fiber downhole into
        a control line (small diameter tube).
    :ivar downhole_control_line_reference: A reference to the control
        line string in a completion data object that represents this
        control line containing a fiber.
    """
    size: Optional[ControlLineSize] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    material: Optional[ControlLineMaterial] = field(
        default=None,
        metadata={
            "name": "Material",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    encapsulation_type: Optional[ControlLineEncapsulationKind] = field(
        default=None,
        metadata={
            "name": "EncapsulationType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    encapsulation_size: Optional[ControlLineEncapsulationSize] = field(
        default=None,
        metadata={
            "name": "EncapsulationSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
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
    pump_activity: List[FiberPumpActivity] = field(
        default_factory=list,
        metadata={
            "name": "PumpActivity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    downhole_control_line_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "downholeControlLineReference",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
