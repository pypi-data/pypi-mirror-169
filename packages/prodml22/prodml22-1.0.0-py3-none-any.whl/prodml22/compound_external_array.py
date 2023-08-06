from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_value_array import AbstractValueArray
from prodml22.das_calibration_column import DasCalibrationColumn
from prodml22.external_data_array import ExternalDataArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CompoundExternalArray(AbstractValueArray):
    """Three instances of the Columns element are used to provide the order of
    the columns of data in the associated Compound External Array.

    Each instance will contain one the three enum values:
    FacilityLength, LocusIndex, OpticalPathDistance, which make up the
    array.

    :ivar columns: Specifies the ordering of the columns of a
        Calibration array in the HDF5 file. A Calibration array contains
        columns for the following quantities: Facility Length, Locus
        Index and Optical Path Distance. The order of these columns is
        flexible but is specified by this element. It comprises three
        values, each of which must be one of the values of the enum
        DasCalibrationColumn, which are the three quantities listed
        above.
    :ivar values: Reference to an HDF5 dataset.
    """
    columns: List[DasCalibrationColumn] = field(
        default_factory=list,
        metadata={
            "name": "Columns",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "min_occurs": 3,
            "max_occurs": 3,
        }
    )
    values: Optional[ExternalDataArray] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
