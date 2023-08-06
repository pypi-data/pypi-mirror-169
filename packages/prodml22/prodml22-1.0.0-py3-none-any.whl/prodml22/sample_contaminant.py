from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_contaminant import FluidContaminant
from prodml22.liquid_composition import LiquidComposition
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.molecular_weight_measure import MolecularWeightMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SampleContaminant:
    """
    Sample contaminant information.

    :ivar contaminant_kind: The kind of contaminant.
    :ivar weight_fraction_stock_tank: The contaminant weight percent in
        stock tank oil.
    :ivar volume_fraction_stock_tank: The contaminant volume percent in
        stock tank oil.
    :ivar weight_fraction_live_sample: The weight fraction of
        contaminant in the fluid sample.
    :ivar volume_fraction_live_sample: The volume fraction of
        contaminant in the fluid sample.
    :ivar molecular_weight: The molecular weight of contaminant in the
        fluid sample.
    :ivar density: The density of contaminant in the fluid sample.
    :ivar contaminant_composition: The composition of contaminant in the
        fluid sample.
    :ivar description: Description of the contaminant.
    :ivar remark: Remarks and comments about this data item.
    :ivar sample_of_contaminant:
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    contaminant_kind: Optional[FluidContaminant] = field(
        default=None,
        metadata={
            "name": "ContaminantKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    weight_fraction_stock_tank: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "WeightFractionStockTank",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    volume_fraction_stock_tank: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeFractionStockTank",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    weight_fraction_live_sample: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "WeightFractionLiveSample",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    volume_fraction_live_sample: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "VolumeFractionLiveSample",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    molecular_weight: Optional[MolecularWeightMeasure] = field(
        default=None,
        metadata={
            "name": "MolecularWeight",
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
    contaminant_composition: Optional[LiquidComposition] = field(
        default=None,
        metadata={
            "name": "ContaminantComposition",
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
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    sample_of_contaminant: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SampleOfContaminant",
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
