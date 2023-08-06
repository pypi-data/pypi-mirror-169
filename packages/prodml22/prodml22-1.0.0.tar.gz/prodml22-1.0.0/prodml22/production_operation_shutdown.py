from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dated_comment import DatedComment
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.time_measure import TimeMeasure
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationShutdown:
    """
    Information about a shutdown event.

    :ivar installation: The name of the installation which was shut
        down. The name can be qualified by a naming system. This also
        defines the kind of facility.
    :ivar description: A general description of the shutdown with reason
        and other relevant information.
    :ivar dtim_start: The time the shutdown started.
    :ivar dtim_end: The time the shutdown ended.
    :ivar volumetric_down_time: Downtime when the installation is unable
        to produce 100% of its capability.
    :ivar loss_oil_std_temp_pres: Estimated loss of oil deliveries
        because of the shutdown. This volume has been corrected to
        standard conditions of temperature and pressure.
    :ivar loss_gas_std_temp_pres: Estimated loss of gas deliveries
        because of the shutdown. This volume has been corrected to
        standard conditions of temperature and pressure.
    :ivar activity: A description of main activities from time to time
        during the shutdown period.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    installation: Optional[FacilityIdentifierStruct] = field(
        default=None,
        metadata={
            "name": "Installation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    dtim_start: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimStart",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    dtim_end: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTimEnd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    volumetric_down_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumetricDownTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    loss_oil_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "LossOilStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    loss_gas_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "LossGasStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    activity: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "Activity",
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
