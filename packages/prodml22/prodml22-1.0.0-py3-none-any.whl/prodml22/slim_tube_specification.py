from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.area_measure import AreaMeasure
from prodml22.injected_gas import InjectedGas
from prodml22.length_measure import LengthMeasure
from prodml22.permeability_rock_measure import PermeabilityRockMeasure
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SlimTubeSpecification:
    """Specifications of the slim tube used during a slim-tube test.

    For definition of a slim tube and slim-tube test, see http://www.glossary.oilfield.slb.com/Terms/s/slim-tube_test.aspx

    :ivar length: The length of the slim tube.
    :ivar outer_diameter: The outer diameter of the slim tube.
    :ivar inner_diameter: The inner diameter of the slim tube.
    :ivar cross_section_area: The cross section area of the slim tube.
    :ivar packing_material: The packing material used in the slim tube.
    :ivar pore_volume: The pore volume of the slim tube.
    :ivar porosity: The porosity of the slim tube.
    :ivar permeability: The permeability of the slim tube.
    :ivar injected_gas: Reference to the gas injected into the slim
        tube.
    :ivar remark: Remarks and comments about this data item.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    outer_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OuterDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    inner_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "InnerDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cross_section_area: Optional[AreaMeasure] = field(
        default=None,
        metadata={
            "name": "CrossSectionArea",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    packing_material: Optional[str] = field(
        default=None,
        metadata={
            "name": "PackingMaterial",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    pore_volume: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "PoreVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    porosity: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Porosity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    permeability: Optional[PermeabilityRockMeasure] = field(
        default=None,
        metadata={
            "name": "Permeability",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    injected_gas: List[InjectedGas] = field(
        default_factory=list,
        metadata={
            "name": "InjectedGas",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
