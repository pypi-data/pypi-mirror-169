from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.dimensionless_measure import DimensionlessMeasure
from prodml22.force_per_length_measure import ForcePerLengthMeasure
from prodml22.mass_per_mass_measure import MassPerMassMeasure
from prodml22.pressure_measure import PressureMeasure
from prodml22.thermodynamic_temperature_measure import ThermodynamicTemperatureMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class InterfacialTensionTestStep:
    """
    The interfacial tension test step.

    :ivar step_number: The step number is the index of a (P,T) step in
        the overall test.
    :ivar step_pressure: The pressure for this test step.
    :ivar step_temperature: The temperature for this test step.
    :ivar wetting_phase_saturation: The wetting phase saturation for
        this test step.
    :ivar surfactant_concentration: The surfactant concentration for
        this test step.
    :ivar interfacial_tension: The interfacial tension for this test
        step.
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
    step_pressure: Optional[PressureMeasure] = field(
        default=None,
        metadata={
            "name": "StepPressure",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    step_temperature: Optional[ThermodynamicTemperatureMeasure] = field(
        default=None,
        metadata={
            "name": "StepTemperature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wetting_phase_saturation: Optional[DimensionlessMeasure] = field(
        default=None,
        metadata={
            "name": "WettingPhaseSaturation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    surfactant_concentration: Optional[MassPerMassMeasure] = field(
        default=None,
        metadata={
            "name": "SurfactantConcentration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    interfacial_tension: Optional[ForcePerLengthMeasure] = field(
        default=None,
        metadata={
            "name": "InterfacialTension",
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
