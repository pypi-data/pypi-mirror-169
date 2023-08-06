from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.production_operation_safety import ProductionOperationSafety
from prodml22.production_operation_weather import ProductionOperationWeather
from prodml22.time_measure import TimeMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class ProductionOperationHse:
    """
    Operational Health, Safety and Environment Schema.

    :ivar incident_count: The number of incidents or accidents and
        injuries that were reported.
    :ivar since_lost_time: The amount of time since the most recent
        lost-time accident.
    :ivar since_prevention_exercise: The amount of time since the most
        recent accident-prevention exercise.
    :ivar since_defined_situation: The amount of time since the most
        recent defined hazard and accident situation (Norwegian DFU).
    :ivar medical_treatment_count: The number of medical treatments that
        have occurred.
    :ivar alarm_count: The number of system alarms that have occurred.
    :ivar safety_intro_count: The number of personnel safety
        introductions that have occurred.
    :ivar safety_description: A textual description of safety
        considerations.
    :ivar weather: Information about the weather at a point in time.
    :ivar safety: Safety information at a specific installatino.
    :ivar uid: A unique identifier for this data element. It is not
        globally unique (not a uuid) and only need be unique within the
        context of the parent top-level object.
    """
    class Meta:
        name = "ProductionOperationHSE"

    incident_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "IncidentCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    since_lost_time: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "SinceLostTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    since_prevention_exercise: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "SincePreventionExercise",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    since_defined_situation: Optional[TimeMeasure] = field(
        default=None,
        metadata={
            "name": "SinceDefinedSituation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    medical_treatment_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "MedicalTreatmentCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    alarm_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "AlarmCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    safety_intro_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SafetyIntroCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    safety_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "SafetyDescription",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    weather: List[ProductionOperationWeather] = field(
        default_factory=list,
        metadata={
            "name": "Weather",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    safety: List[ProductionOperationSafety] = field(
        default_factory=list,
        metadata={
            "name": "Safety",
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
