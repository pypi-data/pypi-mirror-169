from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_model_section import AbstractModelSection
from prodml22.fluid_density import FluidDensity
from prodml22.tubing_interal_diameter import TubingInteralDiameter
from prodml22.wellbore_deviation_angle import WellboreDeviationAngle
from prodml22.wellbore_fluid_compressibility import WellboreFluidCompressibility
from prodml22.wellbore_radius import WellboreRadius
from prodml22.wellbore_storage_coefficient import WellboreStorageCoefficient
from prodml22.wellbore_storage_mechanism_type import WellboreStorageMechanismType
from prodml22.wellbore_volume import WellboreVolume

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WellboreBaseModel(AbstractModelSection):
    """
    Abstract wellbore response model from which the other wellbore response
    model types are derived.
    """
    wellbore_radius: Optional[WellboreRadius] = field(
        default=None,
        metadata={
            "name": "WellboreRadius",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    wellbore_storage_coefficient: Optional[WellboreStorageCoefficient] = field(
        default=None,
        metadata={
            "name": "WellboreStorageCoefficient",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    wellbore_volume: Optional[WellboreVolume] = field(
        default=None,
        metadata={
            "name": "WellboreVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wellbore_fluid_compressibility: Optional[WellboreFluidCompressibility] = field(
        default=None,
        metadata={
            "name": "WellboreFluidCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    tubing_interal_diameter: Optional[TubingInteralDiameter] = field(
        default=None,
        metadata={
            "name": "TubingInteralDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_density: Optional[FluidDensity] = field(
        default=None,
        metadata={
            "name": "FluidDensity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wellbore_deviation_angle: Optional[WellboreDeviationAngle] = field(
        default=None,
        metadata={
            "name": "WellboreDeviationAngle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wellbore_storage_mechanism_type: Optional[WellboreStorageMechanismType] = field(
        default=None,
        metadata={
            "name": "WellboreStorageMechanismType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
