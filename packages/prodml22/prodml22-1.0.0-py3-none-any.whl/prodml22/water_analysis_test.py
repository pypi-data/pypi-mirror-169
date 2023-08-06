from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_mass_measure_ext import MassPerMassMeasureExt
from prodml22.mass_per_volume_measure_ext import MassPerVolumeMeasureExt
from prodml22.water_analysis_test_step import WaterAnalysisTestStep

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class WaterAnalysisTest:
    """
    Water analysis test.

    :ivar test_number: An integer number to identify this test in a
        sequence of tests.
    :ivar liquid_gravity: The liquid gravity for the water analysis
        test.
    :ivar salinity_per_mass: The salinity for the water analysis test.
    :ivar total_dissolved_solids_per_mass: The total dissolved solids
        for the water analysis test.
    :ivar total_suspended_solids_per_mass: The total suspended solids
        for the water analysis test.
    :ivar total_hardness_per_mass: The total water hardness for the
        water analysis test.
    :ivar total_alkalinity_per_mass:
    :ivar total_sediment_solids_per_mass:
    :ivar salinity_per_volume:
    :ivar total_dissolved_solids_per_volume:
    :ivar total_suspended_solids_per_volume:
    :ivar total_hardness_per_volume:
    :ivar total_alkalinity_per_volume:
    :ivar total_sediment_solids_per_volume:
    :ivar test_method:
    :ivar remark: Remarks and comments about this data item.
    :ivar water_analysis_test_step: Water analysis test step.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    test_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "TestNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    liquid_gravity: Optional[float] = field(
        default=None,
        metadata={
            "name": "LiquidGravity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    salinity_per_mass: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "SalinityPerMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_dissolved_solids_per_mass: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalDissolvedSolidsPerMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_suspended_solids_per_mass: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalSuspendedSolidsPerMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_hardness_per_mass: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalHardnessPerMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_alkalinity_per_mass: Optional[MassPerMassMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalAlkalinityPerMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_sediment_solids_per_mass: Optional[MassPerMassMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalSedimentSolidsPerMass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    salinity_per_volume: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "SalinityPerVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_dissolved_solids_per_volume: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalDissolvedSolidsPerVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_suspended_solids_per_volume: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalSuspendedSolidsPerVolume ",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_hardness_per_volume: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalHardnessPerVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_alkalinity_per_volume: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalAlkalinityPerVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_sediment_solids_per_volume: Optional[MassPerVolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "TotalSedimentSolidsPerVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    test_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
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
    water_analysis_test_step: List[WaterAnalysisTestStep] = field(
        default_factory=list,
        metadata={
            "name": "WaterAnalysisTestStep",
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
