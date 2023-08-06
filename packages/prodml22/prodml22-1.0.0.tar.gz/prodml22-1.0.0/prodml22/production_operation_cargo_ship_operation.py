from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dated_comment import DatedComment
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationCargoShipOperation:
    """
    Information about an operation involving a cargo ship.

    :ivar vessel_name: Name of the cargo vessel.
    :ivar dtim_start: The date and time that the vessel arrived.
    :ivar dtim_end: The date and time that the vessel left.
    :ivar captain: Name of the captain of the vessel.
    :ivar cargo_number: The cargo identifier.
    :ivar cargo_batch_number: The cargo batch number. Used if the vessel
        needs to temporarily disconnect for some reason (e.g., weather).
    :ivar cargo: Description of cargo on the vessel.
    :ivar oil_gross_std_temp_pres: Gross oil loaded to the ship during
        the report period. Gross oil includes BS and W. This volume has
        been corrected to standard conditions of temperature and
        pressure.
    :ivar oil_gross_total_std_temp_pres: Gross oil loaded to the ship in
        total during the operation. Gross oil includes BS and W. This
        volume has been corrected to standard conditions of temperature
        and pressure.
    :ivar oil_net_std_temp_pres: Net oil loaded to the ship during the
        report period. Net oil excludes BS and W, fuel, spills, and
        leaks. This volume has been corrected to standard conditions of
        temperature and pressure.
    :ivar oil_net_month_to_date_std_temp_pres: Net oil loaded to the
        ship from the beginning of the month to the end of the reporting
        period. Net oil excludes BS and W, fuel, spills, and leaks. This
        volume has been corrected to standard conditions of temperature
        and pressure.
    :ivar density_std_temp_pres: Density of the liquid loaded to the
        tanker. This density has been corrected to standard conditions
        of temperature and pressure.
    :ivar density: Density of the liquid loaded to the tanker.
    :ivar rvp: Reid vapor pressure of the liquid.
    :ivar bsw: Basic sediment and water is measured from a liquid sample
        the production stream. It includes free water, sediment and
        emulsion and is measured as a volume percentage of the liquid.
    :ivar salt: Salt content. The product formed by neutralization of an
        acid and a base. The term is more specifically applied to sodium
        chloride.
    :ivar comment: A commnet about the operation.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    vessel_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "VesselName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
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
    captain: Optional[str] = field(
        default=None,
        metadata={
            "name": "Captain",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    cargo_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CargoNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    cargo_batch_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "CargoBatchNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cargo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Cargo",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    oil_gross_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilGrossStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_gross_total_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilGrossTotalStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_net_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilNetStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oil_net_month_to_date_std_temp_pres: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "OilNetMonthToDateStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    density_std_temp_pres: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityStdTempPres",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    density: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Density",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    rvp: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "Rvp",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    bsw: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Bsw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    salt: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Salt",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    comment: List[DatedComment] = field(
        default_factory=list,
        metadata={
            "name": "Comment",
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
