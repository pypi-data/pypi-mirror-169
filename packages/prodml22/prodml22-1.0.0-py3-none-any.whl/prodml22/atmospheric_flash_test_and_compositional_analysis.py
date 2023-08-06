from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_pressure_value import AbstractPressureValue
from prodml22.flashed_gas import FlashedGas
from prodml22.flashed_liquid import FlashedLiquid
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.overall_composition import OverallComposition
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AtmosphericFlashTestAndCompositionalAnalysis:
    """
    The flash test and compositional analysis.

    :ivar test_number: An integer number to identify this test in a
        sequence of tests.
    :ivar date: The date when this test was performed.
    :ivar flash_to_pressure: The pressure to which the sample is flashed
        in this analysis. This pressure may differ from the Standard
        Conditions at which the results are reported. Standard
        Conditions are reported for all the Analyses in the parent
        element FluidAnalysis.
    :ivar flash_to_temperature: The temperature to which the sample is
        flashed in this analysis. This temperature may differ from the
        Standard Conditions at which the results are reported. Standard
        Conditions are reported for all the Analyses in the parent
        element FluidAnalysis.
    :ivar flash_from_pressure: This is the starting pressure for the
        sample having the Atmospheric Flash Test.
    :ivar flash_from_temperature: This is the starting temperature for
        the sample having the Atmospheric Flash Test.
    :ivar flash_gor: The gas-oil ratio of the flash in this analysis.
    :ivar oil_formation_volume_factor: The formation volume factor for
        the oil (liquid) phase at the conditions of this test--volume at
        test conditions/volume at standard conditions.
    :ivar density_at_flash_from_pressure_and_temperature: The density of
        the sample at the pressure and temperature conditions of this
        test.
    :ivar avg_molecular_weight: The average molecular weight of the
        sample for this test.
    :ivar remark: Remarks and comments about this data item.
    :ivar flashed_liquid: Flashed liquid.
    :ivar overall_composition: Overall composition.
    :ivar flashed_gas: Flashed gas.
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
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flash_to_pressure: Optional[AbstractPressureValue] = field(
        default=None,
        metadata={
            "name": "FlashToPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flash_to_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "FlashToTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flash_from_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "FlashFromPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flash_from_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "FlashFromTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    flash_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "FlashGOR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_formation_volume_factor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilFormationVolumeFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    density_at_flash_from_pressure_and_temperature: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityAtFlashFromPressureAndTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    avg_molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "AvgMolecularWeight",
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
    flashed_liquid: Optional[FlashedLiquid] = field(
        default=None,
        metadata={
            "name": "FlashedLiquid",
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
    flashed_gas: Optional[FlashedGas] = field(
        default=None,
        metadata={
            "name": "FlashedGas",
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
