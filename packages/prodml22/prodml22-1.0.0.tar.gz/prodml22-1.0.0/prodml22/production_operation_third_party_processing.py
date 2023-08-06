from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.facility_identifier_struct import FacilityIdentifierStruct
from prodml22.volume_measure import VolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationThirdPartyProcessing:
    """
    Production losses due to third-party processing.

    :ivar installation: The name of the installation which performed the
        processing. The name can be qualified by a naming system. This
        also defines the kind of facility.
    :ivar oil_std_temp_pres: The estimated amount of oil lost. This
        volume has been corrected to standard conditions of temperature
        and pressure
    :ivar gas_std_temp_pres: The estimated amount of gas lost. This
        volume has been corrected to standard conditions of temperature
        and pressure
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
    oil_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gas_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "GasStdTempPres",
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
