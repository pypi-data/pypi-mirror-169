from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_measure_data import AbstractMeasureData
from prodml22.product_volume_alert import ProductVolumeAlert

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductVolumeParameterValue:
    """
    Parameter Value Schema.

    :ivar dtim: The date and time at which the parameter applies. If no
        time is specified then the value is static.
    :ivar dtim_end: The date and time at which the parameter no longer
        applies. The "active" time interval is inclusive of this point.
        If dTimEnd is given then dTim shall also be given.
    :ivar port: A port related to the parameter. If a port is given then
        the corresponding unit usually must be given. For example, an
        "offset along network" parameter must specify a port from which
        the offset was measured.
    :ivar unit: A unit related to the parameter. For example, an "offset
        along network" parameter must specify a port (on a unit) from
        which the offset was measured.
    :ivar measure_data_type:
    :ivar alert: An indication of some sort of abnormal condition
        relative this parameter.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    port: Optional[str] = field(
        default=None,
        metadata={
            "name": "Port",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    measure_data_type: List[AbstractMeasureData] = field(
        default_factory=list,
        metadata={
            "name": "MeasureDataType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 1,
        }
    )
    alert: Optional[ProductVolumeAlert] = field(
        default=None,
        metadata={
            "name": "Alert",
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
