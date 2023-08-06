from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.cable_kind import CableKind
from prodml22.extension_name_value import ExtensionNameValue
from prodml22.fiber_common import FiberCommon
from prodml22.fiber_conveyance import FiberConveyance
from prodml22.fiber_mode import FiberMode
from prodml22.fiber_one_way_attenuation import FiberOneWayAttenuation
from prodml22.fiber_refractive_index import FiberRefractiveIndex
from prodml22.length_measure import LengthMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FiberOpticalPathSegment(FiberCommon):
    """A single segment of the optical fiber used for distributed temperature
    surveys.

    Multiple such segments may be connected by other types of components
    including connectors, splices and fiber turnarounds.

    :ivar fiber_length: The length of fiber in this optical path
        section.
    :ivar over_stuffing: For this fiber segment, the amount of
        "overstuffing", i.e., the excess length of fiber that was
        installed compared to the length of the facility that is to be
        surveyed. Example: if 110 m of fiber were to be installed to
        measure 100 m length of pipeline, the overstuffing would be 10
        m. Overstuffing can be allowed for in the facilityMapping
        section. The overstuffing is assumed to be linear distributed
        along the facility being measured.
    :ivar core_diameter: The inner diameter of the core, generally
        measured in microns (um).
    :ivar cladded_diameter: The diameter of the core plus the cladding,
        generally measured in microns (um).
    :ivar outside_diameter: The diameter of the cable containing the
        fiber, including all its sheathing layers.
    :ivar mode: The mode of fiber. Enum. Values are single- or multi-
        mode fiber, or other/unknown.
    :ivar coating: The type of coating on the fiber.
    :ivar jacket: The type of jacket covering the fiber.
    :ivar core_type: Property of the fiber core.
    :ivar parameter: Additional parameters to define the fiber as a
        material.
    :ivar spool_number_tag: The spool number of the particular spool
        from which this fiber segment was taken. The spool number may
        contain alphanumeric characters.
    :ivar spool_length: The length of the fiber on the spool when
        purchased.
    :ivar cable_type: Enum. The type of cable used in this segment.
        Example: single-fiber-cable.
    :ivar fiber_conveyance: The means by which this fiber segment is
        conveyed into the well.
    :ivar one_way_attenuation: The power loss for one way travel of a
        beam of light, usually measured in decibels per unit length. It
        is necessary to include both the value (and its unit) and the
        wavelength. The wavelength varies with the refractive index,
        while the frequency remains constant. The wavelength given to
        specify this type is the wavelength in a vacuum (refractive
        index = 1).
    :ivar refractive_index: The refractive index of a material depends
        on the frequency (or wavelength) of the light. Hence it is
        necessary to include both the value (a unitless number) and the
        frequency (or wavelength) it was measured at. The frequency will
        be a quantity type with a frequency unit such as Hz.
    """
    fiber_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "FiberLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    over_stuffing: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OverStuffing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    core_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CoreDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cladded_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "CladdedDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    outside_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "OutsideDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    mode: Optional[FiberMode] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    coating: Optional[str] = field(
        default=None,
        metadata={
            "name": "Coating",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    jacket: Optional[str] = field(
        default=None,
        metadata={
            "name": "Jacket",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    core_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoreType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    parameter: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    spool_number_tag: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpoolNumberTag",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 64,
        }
    )
    spool_length: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "SpoolLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    cable_type: Optional[CableKind] = field(
        default=None,
        metadata={
            "name": "CableType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fiber_conveyance: Optional[FiberConveyance] = field(
        default=None,
        metadata={
            "name": "FiberConveyance",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    one_way_attenuation: List[FiberOneWayAttenuation] = field(
        default_factory=list,
        metadata={
            "name": "OneWayAttenuation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    refractive_index: List[FiberRefractiveIndex] = field(
        default_factory=list,
        metadata={
            "name": "RefractiveIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
