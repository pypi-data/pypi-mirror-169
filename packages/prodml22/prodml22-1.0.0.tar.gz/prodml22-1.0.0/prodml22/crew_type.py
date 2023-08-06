from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class CrewType(Enum):
    """
    Specifies the types of production operations personnel grouping.

    :cvar CATERING_CREW: A count that is the number of persons from the
        catering contractor spending the night at the installation.
    :cvar CONTRACTOR_CREW: A count that is the number of persons from
        other than operator spending the night at the installation.
    :cvar DAY_VISITORS: A count that is the number of persons visiting
        the installation but not  spending the night at the
        installation.
    :cvar DRILLING_CONTRACT_CREW: A count that is the number of persons
        from the drilling contractor spending the night at the
        installation.
    :cvar OTHER_CREW: A count that is the number of persons from an
        unknown source, normally not working on the installation but
        spending the night there.
    :cvar OWN_CREW: A count that is the number of persons from the
        operator, normally working on the installation and spending the
        night there.
    :cvar OWN_OTHER_CREW: A count that is the number of persons from the
        operator, normally not working on the installation but spending
        the night there.
    :cvar PERSONNEL_ON_BOARD: A count of the total personnel on board.
    """
    CATERING_CREW = "catering crew"
    CONTRACTOR_CREW = "contractor crew"
    DAY_VISITORS = "day visitors"
    DRILLING_CONTRACT_CREW = "drilling contract crew"
    OTHER_CREW = "other crew"
    OWN_CREW = "own crew"
    OWN_OTHER_CREW = "own other crew"
    PERSONNEL_ON_BOARD = "personnel on board"
