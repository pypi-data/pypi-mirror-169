from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.pressure_measure import PressureMeasure
from prodml22.slim_tube_test_volume_step import SlimTubeTestVolumeStep

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SlimTubeTestStep:
    """
    Slim-tube test step.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar step_average_pressure: The average pressure for this slim-tube
        test step.
    :ivar remark: Remarks and comments about this data item.
    :ivar slim_tube_test_volume_step:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    step_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "StepNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    step_average_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StepAveragePressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    slim_tube_test_volume_step: List[SlimTubeTestVolumeStep] = field(
        default_factory=list,
        metadata={
            "name": "SlimTubeTestVolumeStep",
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
