from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.mass_per_volume_measure import MassPerVolumeMeasure
from prodml22.ref_injected_gas_added import RefInjectedGasAdded
from prodml22.relative_volume_ratio import RelativeVolumeRatio
from prodml22.saturation_pressure import SaturationPressure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SwellingTestStep:
    """
    Swelling test step.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar incremental_gas_added: The amount of an injected gas for this
        step, and a reference to which Injected Gas composition it
        consists of. Note, multiple gases of different compositions may
        be injected at each test step.
    :ivar cumulative_gas_added: The cumulative amount of an injected gas
        up to and including this step, and a reference to which Injected
        Gas composition it consists of. Note, multiple gases of
        different compositions may be injected at each test step, and
        this element tracks the cumulative quantity of each of them.
    :ivar gor: The gas-oil ratio for this swelling test step.
    :ivar saturation_pressure: The saturation (or bubble point) pressure
        measured in this test.
    :ivar swollen_volume: The swollen volume for this swelling test
        step, relative to a reference volume.
    :ivar swelling_factor: The swelling factor for this swelling test
        step.
    :ivar density_at_saturation_point: The density at saturation point
        for this swelling test step.
    :ivar constant_composition_expansion_test: A reference to a constant
        composition expansion test associated with this swelling test.
    :ivar transport_property_test_reference: A reference to a transport
        property test associated with this swelling test.
    :ivar remark: Remarks and comments about this data item.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    step_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "StepNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "min_inclusive": 0,
        }
    )
    incremental_gas_added: List[RefInjectedGasAdded] = field(
        default_factory=list,
        metadata={
            "name": "IncrementalGasAdded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cumulative_gas_added: List[RefInjectedGasAdded] = field(
        default_factory=list,
        metadata={
            "name": "CumulativeGasAdded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "Gor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    saturation_pressure: Optional[SaturationPressure] = field(
        default=None,
        metadata={
            "name": "SaturationPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    swollen_volume: Optional[RelativeVolumeRatio] = field(
        default=None,
        metadata={
            "name": "SwollenVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    swelling_factor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "SwellingFactor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    density_at_saturation_point: Optional[MassPerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "DensityAtSaturationPoint",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    constant_composition_expansion_test: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConstantCompositionExpansionTest",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    transport_property_test_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "TransportPropertyTestReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
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
