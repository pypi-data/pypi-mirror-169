from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractParameter:
    """Abstract for a single parameter relating to a pressure transient
    analysis.

    Collected together in Result Section Models. Eg, all the parameters
    needed for a closed boundary model will be found in the
    ClosedRectangleModel.

    :ivar source_result_ref_id: This is a reference to a different
        Result, which is the source for this parameter. It therefore
        only applies when the Direction is "input". Example: an estimate
        for permeability may be obtained in one result and then used as
        input to constrain a second result, such as one estimating
        distance to a fault. In this case, the second result would show
        "input" direction for permeability parameter, and its
        SourceResultRefID would point to the first result from which
        permeability was obtained.
    :ivar remark: Textual description about the value of this field.
    :ivar uid: Unique identifier for this instance of the object.
    """
    source_result_ref_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceResultRefID",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uid",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
