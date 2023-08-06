from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from prodml22.abstract_object import AbstractObject
from prodml22.abstract_temperature_pressure import AbstractTemperaturePressure
from prodml22.data_object_reference import DataObjectReference
from prodml22.fluid_component_catalog import FluidComponentCatalog
from prodml22.geographic_context import GeographicContext

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class AbstractSimpleProductVolume(AbstractObject):
    """The parent abstract class for any object that will be included in a
    regulatory report.

    Those objects must inherit from this abstract object.

    :ivar standard_conditions: The condition-dependant measurements
        (e.g.,  volumes) in this transfer are taken to be measured at
        standard conditions. The element is mandatory in all the SPVR
        objects.  A choice is available – either to supply the
        temperature and pressure for all the volumes that follow, or to
        choose from a list of standards organizations’ reference
        conditions. Note that the enum list of standard conditions is
        extensible, allowing for local measurement condition standards
        to be used
    :ivar approval_date: The date on which the report was approved.
    :ivar geographic_context: Geographic context for reporting entities.
    :ivar operator:
    :ivar fluid_component_catalog: Fluid component catalog.
    """
    standard_conditions: Optional[AbstractTemperaturePressure] = field(
        default=None,
        metadata={
            "name": "StandardConditions",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    approval_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "ApprovalDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    geographic_context: Optional[GeographicContext] = field(
        default=None,
        metadata={
            "name": "GeographicContext",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    operator: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    fluid_component_catalog: Optional[FluidComponentCatalog] = field(
        default=None,
        metadata={
            "name": "FluidComponentCatalog",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
