from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberPumpActivity:
    """
    The activity of pumping the fiber downhole into a control line (small
    diameter tube).

    :ivar name: A name that can be used to reference the pumping
        activity. In general, a pumping activity does not have a natural
        name, so this element is often not used.
    :ivar installed_fiber: The name of the InstalledFiberInstance that
        this activity relates to.
    :ivar pumping_date: The date of the pumping activity.
    :ivar engineer_name: The person in charge of the pumping activity.
    :ivar service_company: The company that performed the pumping
        activity.
    :ivar pump_fluid_type: The type of fluid used in the pump.
    :ivar control_line_fluid: The type of fluid used in the control
        line.
    :ivar pump_direction: The direction of the pumping.
    :ivar fiber_end_seal: The type of end seal on the fiber.
    :ivar cable_meter_type: The type of cable meter.
    :ivar cable_meter_serial_number: The serial number of the cable
        meter.
    :ivar cable_meter_calibration_date: The date the cable meter was
        calibrated.
    :ivar excess_fiber_recovered: The length of the excess fiber that
        was removed.
    :ivar comment: Comment about the pump activity.
    :ivar uid: Unique identifier of this object.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    installed_fiber: Optional[str] = field(
        default=None,
        metadata={
            "name": "InstalledFiber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    pumping_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "PumpingDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    engineer_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "EngineerName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    service_company: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceCompany",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    pump_fluid_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "PumpFluidType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    control_line_fluid: Optional[str] = field(
        default=None,
        metadata={
            "name": "ControlLineFluid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    pump_direction: Optional[str] = field(
        default=None,
        metadata={
            "name": "PumpDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    fiber_end_seal: Optional[str] = field(
        default=None,
        metadata={
            "name": "FiberEndSeal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    cable_meter_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CableMeterType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    cable_meter_serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "CableMeterSerialNumber",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    cable_meter_calibration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "CableMeterCalibrationDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    excess_fiber_recovered: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ExcessFiberRecovered",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
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
