from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.data_object_reference import DataObjectReference
from prodml22.length_measure import LengthMeasure
from prodml22.md_interval import MdInterval
from prodml22.reference_point_kind import ReferencePointKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class FlowTestLocation:
    """Describes the location of the reservoir connection from which pressure
    and/or flow are being measured. BUSINESS RULE: Can be one of: (i) a named
    wellbore (a WITSML object) together with a MD Interval; (ii) a named
    Wellbore Completion (a WITSML object with physical details of a
    completion), (iii) a named well (a WITSML object), (iv) a named Reporting
    Entity (which is a generic object to represent a location for flow
    reporting in the PRODML Simple Product Volume Reporting schema), or (v) a
    Probe on a wireline or LWD formation tester tool, in which case it has
    single Probe Depth and Probe Diameter. A wellbore + MD Interval, or a
    wellbore completion option would be expected for most tests.  The well, or
    well completion options could be used for a test commingling flow multiple
    wellbores or completions.  See the WITSML documentation for Completion for
    more details. The Reporting Entity option could be used for the testing of
    some less common combination of sources, eg a cluster of wells. NOTE that
    well, wellbore, well completion, wellbore completion and reporting entity
    elements are all Data Object References (see Energistics Common
    documentation). These are used to reference separate data objects which
    fully describe the real-world facilities concerned. However, it is not
    necessary for the separate data object to exist. The elements can be used
    as follows:

    - The Title element of the data object reference class is used to identify the name of the real-world facility, eg the well name, as a text string.
    - The mandatory Content Type element would contain the class of the referenced object (the same as the element name).
    - The mandatory  UUID String can contain any dummy uuid-like string.

    :ivar wellbore: A reference, using data object reference, to the
        Wellbore which represents this flowing interval.
    :ivar md_interval: A reference, using data object reference, to the
        MdInterval which represents this flowing interval.
    :ivar wellbore_completion: A reference, using data object reference,
        to the WellboreCompletion which represents this flowing
        interval.
    :ivar well: A reference, using data object reference, to the Well
        which represents this flowing interval.
    :ivar well_completion: A reference, using data object reference, to
        the WellCompletion which represents this flowing interval.
    :ivar reporting_entity: A reference, using data object reference, to
        the ReportingEntity which represents this flowing interval.
    :ivar remark: Textual description about the value of this field.
    :ivar probe_depth: The depth of a probe if this is the connection to
        reservoir in a wireline or LWD formation tester tool. A single
        depth rather than a range.
    :ivar probe_diameter: The diameter of a probe if this is the
        connection to reservoir in a wireline or LWD formation tester
        tool. The probe diameter governs the area open to flow from the
        formation.
    :ivar datum: Textual description about the value of this field.
    """
    wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Wellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    wellbore_completion: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WellboreCompletion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Well",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    well_completion: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WellCompletion",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    reporting_entity: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ReportingEntity",
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
    probe_depth: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ProbeDepth",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    probe_diameter: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "ProbeDiameter",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
    datum: Optional[ReferencePointKind] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
        }
    )
