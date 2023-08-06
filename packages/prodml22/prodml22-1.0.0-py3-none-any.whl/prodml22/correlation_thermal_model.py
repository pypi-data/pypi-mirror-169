from __future__ import annotations
from dataclasses import dataclass
from prodml22.abstract_correlation_model import AbstractCorrelationModel

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


@dataclass
class CorrelationThermalModel(AbstractCorrelationModel):
    """A class that AbstractCompositionalModel can inherit; it is NOT abstract
    because the concrete model types have not been specified.

    For now, use the non-abstract thermal model, and use the
    CustomPvtModelExtension to add anything needed. Later, it will be
    made abstract and have concrete classes it inherits from, similar to
    EoS.
    """
