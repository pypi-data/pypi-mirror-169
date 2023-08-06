from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.pvt_model_parameter_kind import PvtModelParameterKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class PvtModelParameter:
    """
    PVT model parameter.

    :ivar value:
    :ivar kind: The kind of model parameter. Extensible enum.  See PVT
        model parameter kind ext.
    :ivar name: The  user-defined name of a parameter, which can be
        added to any model.
    """
    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    kind: Optional[Union[PvtModelParameterKind, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
