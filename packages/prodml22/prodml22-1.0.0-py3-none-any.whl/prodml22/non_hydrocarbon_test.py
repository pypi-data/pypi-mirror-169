from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.extension_name_value import ExtensionNameValue
from prodml22.overall_composition import OverallComposition
from prodml22.phase_present import PhasePresent
from prodml22.pressure_measure_ext import PressureMeasureExt
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_measure_ext import VolumeMeasureExt

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class NonHydrocarbonTest:
    """
    :ivar test_number:
    :ivar test_time:
    :ivar test_volume:
    :ivar phases_tested:
    :ivar test_temperature:
    :ivar test_pressure:
    :ivar analysis_method:
    :ivar sampling_point:
    :ivar cell_id:
    :ivar instrument_id:
    :ivar non_hydrocarbon_concentrations:
    :ivar other_measured_properties: A generic measurement which does
        not result in a concentration measurement can be reported using
        this element with variable measure class. Example, radioactivity
        measured in units of radioactivity per unit volume.
    :ivar remark:
    """
    test_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "TestNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
    test_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "TestTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    test_volume: Optional[VolumeMeasureExt] = field(
        default=None,
        metadata={
            "name": "TestVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    phases_tested: Optional[PhasePresent] = field(
        default=None,
        metadata={
            "name": "PhasesTested",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    test_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "TestTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    test_pressure: Optional[PressureMeasureExt] = field(
        default=None,
        metadata={
            "name": "TestPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    analysis_method: Optional[str] = field(
        default=None,
        metadata={
            "name": "AnalysisMethod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    sampling_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "SamplingPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    cell_id: Optional[int] = field(
        default=None,
        metadata={
            "name": "CellId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_inclusive": 0,
        }
    )
    instrument_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstrumentId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    non_hydrocarbon_concentrations: Optional[OverallComposition] = field(
        default=None,
        metadata={
            "name": "NonHydrocarbonConcentrations",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    other_measured_properties: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "OtherMeasuredProperties",
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
