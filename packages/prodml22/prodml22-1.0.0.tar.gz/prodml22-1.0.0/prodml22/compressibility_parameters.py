from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.reciprocal_pressure_measure_ext import ReciprocalPressureMeasureExt
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CompressibilityParameters:
    """
    Compressibility and saturation values.

    :ivar formation_compressibility: Formation Compressibility of the
        reservoir.
    :ivar oil_phase_saturation: Oil Phase Saturation in the reservoir.
    :ivar gas_phase_saturation: Gas Phase Saturation in the reservoir.
    :ivar water_phase_saturation: Water Phase Saturation in the
        reservoir.
    :ivar total_compressibility: Total system compressibility -
        formation compressibility + saturation-weighted fluid
        compressibilities.
    """
    formation_compressibility: Optional[ReciprocalPressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "FormationCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_phase_saturation: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilPhaseSaturation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_phase_saturation: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasPhaseSaturation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_phase_saturation: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "WaterPhaseSaturation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_compressibility: Optional[ReciprocalPressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalCompressibility",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
