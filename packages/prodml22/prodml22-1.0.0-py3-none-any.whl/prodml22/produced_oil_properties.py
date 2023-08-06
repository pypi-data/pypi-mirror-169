from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.apigravity_measure import ApigravityMeasure
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProducedOilProperties:
    """
    Properties of produced oil.

    :ivar stodensity: The stock tank oil density of this produced oil.
    :ivar stoapi_gravity: The stock tank oil API gravity of this
        produced oil.
    :ivar stomw: The stock tank oil molecular weight of this produced
        oil.
    :ivar stowater_content: The stock tank oil water content of this
        produced oil.
    :ivar asphaltene_content: The asphaltene content of this produced
        oil.
    """
    stodensity: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "STODensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    stoapi_gravity: Optional[ApigravityMeasure] = field(
        default=None,
        metadata={
            "name": "STOApiGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    stomw: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "STOMW",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    stowater_content: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "STOWaterContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    asphaltene_content: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "AsphalteneContent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
