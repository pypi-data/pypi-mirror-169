from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.length_per_time_measure import LengthPerTimeMeasure
from prodml22.mass_balance import MassBalance
from prodml22.pressure_measure import PressureMeasure
from prodml22.produced_gas_properties import ProducedGasProperties
from prodml22.produced_oil_properties import ProducedOilProperties
from prodml22.volume_measure import VolumeMeasure
from prodml22.volume_per_volume_measure import VolumePerVolumeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class SlimTubeTestVolumeStep:
    """
    Slim-tube test volume step.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar differential_pressure: The differential pressure of the slim-
        tube test volume step.
    :ivar run_time: The run time of the slim-tube test volume step.
    :ivar injection_volume_at_pump_temperature: The injection volume at
        pump temperature of the slim-tube test volume step.
    :ivar injection_volume_at_test_temperature: The injection volume at
        test temperature of the slim-tube test volume step.
    :ivar injected_pore_volume_fraction: The injected pore volume
        fraction of the slim-tube test volume step.
    :ivar darcy_velocity: The Darcy velocity of the slim-tube test
        volume step.
    :ivar cumulative_oil_production_perc_ooip: The cumulative oil
        production as a fraction of the original oil in place of the
        slim-tube test volume step.
    :ivar cumulative_oil_production_sto: The cumulative oil production
        of stock stank oil for the slim-tube test volume step.
    :ivar incremental_produced_gor: The incremental produced GOR of the
        slim-tube test volume step.
    :ivar cumulative_produced_gor: The cumulative oil production GOR for
        the slim-tube test volume step.
    :ivar remark: Remarks and comments about this data item.
    :ivar produced_gas_properties:
    :ivar produced_oil_properties:
    :ivar mass_balance:
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
    differential_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "DifferentialPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    run_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    injection_volume_at_pump_temperature: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "InjectionVolumeAtPumpTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    injection_volume_at_test_temperature: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "InjectionVolumeAtTestTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    injected_pore_volume_fraction: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "InjectedPoreVolumeFraction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    darcy_velocity: Optional[LengthPerTimeMeasure] = field(
        default=None,
        metadata={
            "name": "DarcyVelocity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cumulative_oil_production_perc_ooip: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CumulativeOilProductionPercOOIP",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cumulative_oil_production_sto: Optional[VolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CumulativeOilProductionSTO",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    incremental_produced_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "IncrementalProducedGOR",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cumulative_produced_gor: Optional[VolumePerVolumeMeasure] = field(
        default=None,
        metadata={
            "name": "CumulativeProducedGOR",
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
    produced_gas_properties: Optional[ProducedGasProperties] = field(
        default=None,
        metadata={
            "name": "ProducedGasProperties",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    produced_oil_properties: Optional[ProducedOilProperties] = field(
        default=None,
        metadata={
            "name": "ProducedOilProperties",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mass_balance: Optional[MassBalance] = field(
        default=None,
        metadata={
            "name": "MassBalance",
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
