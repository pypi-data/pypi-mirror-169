from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.abstract_temperature_pressure import AbstractTemperaturePressure
from prodml22.reference_condition import ReferenceCondition

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ReferenceTemperaturePressure(AbstractTemperaturePressure):
    """
    StdTempPress.

    :ivar reference_temp_pres: Defines the reference temperature and
        pressure to which the density has been corrected. If neither
        standardTempPres nor temp,pres are specified then the standard
        condition is defined by standardTempPres at the procuctVolume
        root.
    """
    reference_temp_pres: Optional[Union[ReferenceCondition, str]] = field(
        default=None,
        metadata={
            "name": "ReferenceTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
