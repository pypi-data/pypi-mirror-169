from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class BalanceEventKind(Enum):
    """
    Specifies the types of events related to a product balance.

    :cvar BILL_OF_LADING: For a cargo, the date of the bill of lading
        for the cargo involved.
    :cvar TRANSACTION_DATE: For a transaction (e.g. gas sales
        transaction), the date for the transaction involved.
    :cvar UNKNOWN: Unknown.
    """
    BILL_OF_LADING = "bill of lading"
    TRANSACTION_DATE = "transaction date"
    UNKNOWN = "unknown"
