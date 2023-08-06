from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.fluid_characterization_table import FluidCharacterizationTable
from prodml22.fluid_characterization_table_format_set import FluidCharacterizationTableFormatSet
from prodml22.other_measurement_test_step import OtherMeasurementTestStep

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class OtherMeasurementTest:
    """
    Other measurement test.

    :ivar test_number: An integer number to identify this test in a
        sequence of tests.
    :ivar remark: Remarks and comments about this data item.
    :ivar fluid_characterization_table_format_set: A set of table format
        definitions.
    :ivar fluid_characterization_table: Fluid characterization table.
    :ivar other_measurement_test_step: Other measurement test step.
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
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    fluid_characterization_table_format_set: Optional[FluidCharacterizationTableFormatSet] = field(
        default=None,
        metadata={
            "name": "FluidCharacterizationTableFormatSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_characterization_table: Optional[FluidCharacterizationTable] = field(
        default=None,
        metadata={
            "name": "FluidCharacterizationTable",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    other_measurement_test_step: List[OtherMeasurementTestStep] = field(
        default_factory=list,
        metadata={
            "name": "OtherMeasurementTestStep",
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
