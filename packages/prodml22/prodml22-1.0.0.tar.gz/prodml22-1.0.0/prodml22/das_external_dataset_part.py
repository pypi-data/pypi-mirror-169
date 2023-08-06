from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.external_data_array_part import ExternalDataArrayPart

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasExternalDatasetPart(ExternalDataArrayPart):
    """Array of integer values provided explicitly by an HDF5 dataset.

    The null value must be  explicitly provided in the NullValue
    attribute of this class.

    :ivar part_start_time: The timestamp in human readable, ISO 8601
        format of the first recorded sample in the sub-record of the raw
        data array stored in the corresponding HDF data file. Time zone
        should be included. Sub-second precision should be included
        where applicable but not zero-padded.
    :ivar part_end_time: The timestamp in human readable, ISO 8601
        format of the last recorded sample in the sub-record of the raw
        data array stored in the corresponding HDF data file. Time zone
        should be included. Sub-second precision should be included
        where applicable but not zero-padded.
    """
    part_start_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartStartTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    part_end_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "PartEndTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
