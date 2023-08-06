from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from prodml22.abstract_pta_flow_data import AbstractPtaFlowData
from prodml22.flow_test_location import FlowTestLocation
from prodml22.fluid_component_catalog import FluidComponentCatalog
from prodml22.measured_pressure_data import MeasuredPressureData
from prodml22.other_data import OtherData
from prodml22.test_period import TestPeriod

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FlowTestMeasurementSet:
    """This contains all the measurements associated with flow and/or
    measurements at one interval, e.g., a Wireline Formation Tester Station, a
    Drill Stem Test, a Rate Transient data set.

    There is a mandatory Location. There are any number of Test Periods.
    There are any number of Time Series of data, each of which contains
    point data in a Channel data object.

    :ivar remark: Textual description about the value of this field.
    :ivar test_period: Test conditions for a production well test.
    :ivar location: Describes the location of the reservoir connection
        from which pressure and/or flow are being measured. BUSINESS
        RULE: Can be one of: (i) a named wellbore (a WITSML object)
        together with a MD Interval; (ii) a named Wellbore Completion (a
        WITSML object with physical details of a completion), (iii) a
        named well (a WITSML object), (iv) a named Reporting Entity
        (which is a generic object to represent a location for flow
        reporting in the PRODML Simple Product Volume Reporting schema),
        or (v) a Probe on a wireline or LWD formation tester tool, in
        which case it has single Probe Depth and Probe Diameter. A
        wellbore + MD Interval, or a wellbore completion option would be
        expected for most tests.  The well, or well completion options
        could be used for a test commingling flow multiple wellbores or
        completions.  See the WITSML documentation for Completion for
        more details. The Reporting Entity option could be used for the
        testing of some less common combination of sources, eg a cluster
        of wells. NOTE that well, wellbore, well completion, wellbore
        completion and reporting entity elements are all Data Object
        References (see Energistics Common documentation). These are
        used to reference separate data objects which fully describe the
        real-world facilities concerned. However, it is not necessary
        for the separate data object to exist. The elements can be used
        as follows: - The Title element of the data object reference
        class is used to identify the name of the real-world facility,
        eg the well name, as a text string. - The mandatory Content Type
        element would contain the class of the referenced object (the
        same as the element name). - The mandatory  UUID String can
        contain any dummy uuid-like string.
    :ivar other_data:
    :ivar measured_flow_rate:
    :ivar measured_pressure:
    :ivar fluid_component_catalog: Fluid component catalog.
    :ivar uid: Unique identifier for this instance of the object.
    """
    remark: Optional[str] = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "max_length": 2000,
        }
    )
    test_period: Optional[TestPeriod] = field(
        default=None,
        metadata={
            "name": "TestPeriod",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    location: Optional[FlowTestLocation] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
    other_data: List[OtherData] = field(
        default_factory=list,
        metadata={
            "name": "OtherData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measured_flow_rate: List[AbstractPtaFlowData] = field(
        default_factory=list,
        metadata={
            "name": "MeasuredFlowRate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    measured_pressure: List[MeasuredPressureData] = field(
        default_factory=list,
        metadata={
            "name": "MeasuredPressure",
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
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "max_length": 64,
        }
    )
