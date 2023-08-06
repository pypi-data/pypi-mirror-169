from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class OsdulineageRelationshipKind(Enum):
    """
    :cvar DIRECT: A resource which was used to derive the asserting work
        product component through a set of processes and
        transformations.  The prior data type is usually the same as the
        derived data type.  For example, the input well log used in
        creating a new log curve.
    :cvar INDIRECT: A resource which was used during the derivation of
        the asserting work product component to control the process, but
        is not directly transformed.  The prior data type is usually
        different from the derived data type. For example, the velocity
        model used in migrating a seismic volume, the horizons used to
        constrain a velocity model.
    :cvar REFERENCE: A resource which captures information about the
        process to create the asserting work product component, but is
        not used directly in the process. The prior data type is not a
        required ancestor of the asserting object.  For example, a
        bibliography relative to a published paper, a published paper
        used as the basis for the processing algorithm, a geologic
        interpretation used to QC a seismic velocity model.
    """
    DIRECT = "direct"
    INDIRECT = "indirect"
    REFERENCE = "reference"
