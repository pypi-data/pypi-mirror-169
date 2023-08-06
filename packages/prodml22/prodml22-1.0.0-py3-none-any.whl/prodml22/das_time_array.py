from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from prodml22.integer_external_array import IntegerExternalArray
from prodml22.time_uom import TimeUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasTimeArray:
    """The Times arrays contain the ‘scan’ or ‘trace’ times at which the raw,
    FBE and spectrum arrays were acquired or processed:

    - For raw data, these are the times for which all loci in the ‘scanned’ fiber section were interrogated by a single pulse of the DAS measurement system.
    - For the processed data, these are the times of the first sample in the time window used in the frequency filter or transformation function to calculate the FBE or spectrum data.

    :ivar start_time: The timestamp in human readable, ISO 8601 format
        of the last recorded sample in the acquisition. Note that this
        is the start time of the acquisition if a raw dataset is stored
        in multiple HDF files. The end time of the sub-record stored in
        an individual HDF file is stored in PartStartTime.
    :ivar end_time: The timestamp in human readable, ISO 8601 format of
        the last recorded sample in the acquisition. Note that this is
        the end time of the corresponding data set stored in multiple
        HDF5 files. The end time of the sub-record stored in an
        individual HDF5 file is stored in PartEndTime. Time zone should
        be included. Sub-second precision should be included where
        applicable but not zero-padded.
    :ivar uom: The unit of measure of the intervals in the time array.
    :ivar time_array:
    """
    start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    uom: Optional[Union[TimeUom, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    time_array: Optional[IntegerExternalArray] = field(
        default=None,
        metadata={
            "name": "TimeArray",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
