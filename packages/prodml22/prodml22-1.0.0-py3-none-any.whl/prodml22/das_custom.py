from __future__ import annotations
from dataclasses import dataclass

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class DasCustom:
    """This object contains service–provider-specific customization parameters.

    Service providers can define the contents of this data element as
    required. This data object has intentionally not been described in
    detail to allow for flexibility. Note that this object is optional
    and if used, the service provider needs to provide a description of
    the data elements to the customer.
    """
