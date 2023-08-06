from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ExistenceKind(Enum):
    """A list of lifecycle states like actual, required, planned, predicted,
    etc.

    These are used to qualify any top-level element (from Epicentre
    2.1).

    :cvar ACTUAL: The data describes a concrete, real implementation
        currently setup in the field.
    :cvar PLANNED: The data describes a planned implementation of an
        object under study and/or analysis, subject to evolve, prior to
        being concretely deployed.
    :cvar SIMULATED: The data is generated as a result of a simulation.
    :cvar TEST: The data describes a concrete implementation currently
        setup in the  field for test purpose.
    """
    ACTUAL = "actual"
    PLANNED = "planned"
    SIMULATED = "simulated"
    TEST = "test"
