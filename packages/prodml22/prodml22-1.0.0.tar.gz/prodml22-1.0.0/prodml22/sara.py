from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.mass_per_mass_measure import MassPerMassMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class Sara:
    """SARA analysis results.

    SARA stands for saturates, asphaltenes, resins and aromatics.

    :ivar aromatics_weight_fraction: The aromatics weight fraction in
        the sample.
    :ivar asphaltenes_weight_fraction: The asphaltenes weight fraction
        in the sample.
    :ivar napthenes_weight_fraction: The napthenes weight fraction in
        the sample.
    :ivar paraffins_weight_fraction: The paraffins weight fraction in
        the sample.
    :ivar remark: Remarks and comments about this data item.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    aromatics_weight_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "AromaticsWeightFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    asphaltenes_weight_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "AsphaltenesWeightFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    napthenes_weight_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "NapthenesWeightFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    paraffins_weight_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "ParaffinsWeightFraction",
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
