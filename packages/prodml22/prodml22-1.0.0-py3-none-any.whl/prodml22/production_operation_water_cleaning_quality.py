from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.dated_comment import DatedComment
from prodml22.dimensionless_measure import DimensionlessMeasure
from prodml22.mass_measure import MassMeasure
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationWaterCleaningQuality:
    """Information about the contaminants in water, and the general water
    quality.

    The values are measured from a sample, which is described below.
    Values measured from other samples should be given in different
    instances of the type.

    :ivar sample_point: An identifier of the point from which the sample
        was taken. This is an uncontrolled string value, which should be
        as descriptive as possible.
    :ivar oil_in_water_produced: Total measured oil in the water after
        the water cleaning process, but before it is discharged from the
        installation.
    :ivar amount_of_oil: Total measured oil in the water after the water
        cleaning process, but before it is discharged from the
        installation
    :ivar ammonium: The amount of ammonium found in the water sample.
    :ivar total_organic_carbon: The amount of total organic carbon found
        in the water. The water is under high temperature and the carbon
        left is measured.
    :ivar phenol: The amount of phenol found in the water sample.
    :ivar glycol: The amount of glycol found in the water sample.
    :ivar ph_value: The pH value of the treated water. The pH value is
        best given as a value, with no unit of measure, since there are
        no variations from the pH.
    :ivar water_temperature: The temperature of the water before it is
        discharged.
    :ivar residual_chloride: Total measured residual chlorides in the
        water after the water cleaning process, but before it is
        discharged from the installation.
    :ivar oxygen: Total measured oxygen in the water after the water
        cleaning process, but before it is discharged from the
        installation.
    :ivar turbidity: A measure of the cloudiness of water caused by
        suspended particles.
    :ivar coulter_counter: A measure of the number of particles in water
        as measured by a coulter counter.
    :ivar comment: Any comment that may be useful in describing the
        water quality. There can be multiple comments.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    sample_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "SamplePoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    oil_in_water_produced: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "OilInWaterProduced",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    amount_of_oil: Optional[MassMeasure] = field(
        default=None,
        metadata={
            "name": "AmountOfOil",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    ammonium: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Ammonium",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    total_organic_carbon: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "TotalOrganicCarbon",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    phenol: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Phenol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    glycol: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Glycol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    ph_value: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "PhValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    water_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "WaterTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    residual_chloride: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "ResidualChloride",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    oxygen: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "Oxygen",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    turbidity: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "Turbidity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    coulter_counter: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "CoulterCounter",
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
