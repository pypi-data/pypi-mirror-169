from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class DasCalibrationColumn(Enum):
    """
    This enum controls the possible types of columns allowed in a Calibration
    record in HDF5.
    """
    FACILITY_LENGTH = "FacilityLength"
    LOCUS_INDEX = "LocusIndex"
    OPTICAL_PATH_DISTANCE = "OpticalPathDistance"
