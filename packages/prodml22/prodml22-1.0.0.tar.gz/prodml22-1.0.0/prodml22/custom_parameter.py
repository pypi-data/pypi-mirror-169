from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from prodml22.abstract_parameter import AbstractParameter
from prodml22.general_measure_type import GeneralMeasureType

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CustomParameter(AbstractParameter):
    """A single custom parameter relating to a pressure transient analysis.

    This type can be added in the Custom model section elements (for
    wellbore, near wellbore, reservoir and boundary sections of the PTA
    model), or in a Specialized Analysis.  The custom parameter is to
    enable extensibility beyond the types of parameter built in to the
    schema.  It has to have a name (for the parameter, eg
    "AlphaPressure"), an abbreviation (eg "AP") and a measure value
    using the generalMeasureType. This type does not enforce restricted
    units of measure but a uom needs to be specified which it is assumed
    will be used to work out what dimensional type this parameter
    belongs to.

    :ivar name: The name of the parameter. Expected to be one of the
        name elements of the parameters in the parameterTypeSet of the
        "Models loader file" xml.  The parameter names expected are
        those listed as "parameter" under the model within the category
        of the appropriate result section.
    :ivar abbreviation: The abbreviation of the parameter. Expected to
        be one of the abbreviation elements of the parameters in the
        parameterTypeSet of the "Models loader file" xml.
    :ivar measure_value: The value of the parameter. The measurement
        kind (length etc) is not known since it will vary according to
        parameter type. The UoM attribute is expected to match those for
        the measure class element for this Parameter as specified in the
        "Model loader file" xml for the parameterType concerned.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    abbreviation: Optional[str] = field(
        default=None,
        metadata={
            "name": "Abbreviation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
            "max_length": 64,
        }
    )
    measure_value: Optional[GeneralMeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/prodmlv2",
            "required": True,
        }
    )
