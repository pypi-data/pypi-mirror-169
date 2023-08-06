from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_reference_kind import VolumeReferenceKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FluidVolumeReference:
    """
    The reference conditions and optionally, reference volume, against which
    volume fractions in test steps are recorded.

    :ivar kind: The kind of fluid volume references. Enum, see volume
        reference kind.
    :ivar reference_volume: The reference volume for this analysis.
    :ivar remark: Remarks and comments about this data item.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    kind: Optional[Union[VolumeReferenceKind, str]] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    reference_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "ReferenceVolume",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
