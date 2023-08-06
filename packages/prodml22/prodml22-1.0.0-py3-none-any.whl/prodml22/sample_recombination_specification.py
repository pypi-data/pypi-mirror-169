from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.overall_composition import OverallComposition
from prodml22.recombined_sample_fraction import RecombinedSampleFraction
from prodml22.saturation_pressure import SaturationPressure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SampleRecombinationSpecification:
    """
    For a fluid sample that has been recombined from separate samples, e.g.
    liquid sample and vapor sample, this class records the specified:
    recombination conditions, the saturation pressure and  overall recombined
    sample composition, whichever of these are appropriate for this
    recombination.

    :ivar recombination_pressure: The recombination pressure for this
        sample recombination.
    :ivar recombination_temperature: The recombination temperature for
        this sample recombination.
    :ivar recombination_gor: The recombination gas-oil ratio for this
        sample recombination.
    :ivar recombination_saturation_pressure: The recombination
        saturation pressure for this sample recombination.
    :ivar overall_composition: The aim of the fluid sampling
        recombination was this overall composition.
    :ivar remark: Remarks and comments about this data item.
    :ivar recombined_sample_fraction: Fluid sample points to a mixture
        from other samples.
    """
    recombination_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "RecombinationPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    recombination_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "RecombinationTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    recombination_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "RecombinationGOR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    recombination_saturation_pressure: Optional[SaturationPressure] = field(
        default=None,
        metadata={
            "name": "RecombinationSaturationPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    overall_composition: Optional[OverallComposition] = field(
        default=None,
        metadata={
            "name": "OverallComposition",
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
    recombined_sample_fraction: List[RecombinedSampleFraction] = field(
        default_factory=list,
        metadata={
            "name": "RecombinedSampleFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 2,
        }
    )
