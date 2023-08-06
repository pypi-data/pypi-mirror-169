from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.amount_of_substance_per_amount_of_substance_measure import AmountOfSubstancePerAmountOfSubstanceMeasure
from prodml22.data_object_reference import DataObjectReference
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class RecombinedSampleFraction:
    """For a fluid sample that has been recombined from separate samples, each
    sample has its fraction recorded in this class and the source sample is
    referenced.

    E.g., a fraction and reference to an oil sample and a second
    instance with fraction and reference to gas sample.

    :ivar volume_fraction: The volume fraction of this parent sample
        within this combined sample.
    :ivar mass_fraction: The mass fraction of this parent sample within
        this combined sample.
    :ivar mole_fraction: The mole fraction of this parent sample within
        this combined sample.
    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_sample: The fluid sample.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    volume_fraction: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_fraction: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "MassFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mole_fraction: Optional[AmountOfSubstancePerAmountOfSubstanceMeasure] = field(
        default=None,
        metadata={
            "name": "MoleFraction",
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
    fluid_sample: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidSample",
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
