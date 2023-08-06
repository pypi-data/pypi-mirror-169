from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReportingFlow(Enum):
    """
    Specifies the types of flow for volume reports.

    :cvar CONSUME: consume
    :cvar CONSUME_BLACK_START: consume - black start
    :cvar CONSUME_COMPRESSOR: consume - compressor
    :cvar CONSUME_EMITTED: consume - emitted
    :cvar CONSUME_FLARE: consume - flare
    :cvar CONSUME_FUEL: consume - fuel
    :cvar CONSUME_HP_FLARE: consume - HP flare
    :cvar CONSUME_LP_FLARE: consume - LP flare
    :cvar CONSUME_NON_COMPRESSOR: consume - non compressor
    :cvar CONSUME_VENTING: consume - venting
    :cvar DISPOSAL: disposal
    :cvar EXPORT: export
    :cvar EXPORT_NOMINATED: export - nominated
    :cvar EXPORT_REQUESTED: export - requested
    :cvar EXPORT_SHORTFALL: export - shortfall
    :cvar GAS_LIFT: gas lift
    :cvar HYDROCARBON_ACCOUNTING: hydrocarbon accounting
    :cvar IMPORT: import
    :cvar INJECTION: injection
    :cvar INVENTORY: inventory
    :cvar OVERBOARD: overboard
    :cvar PRODUCTION: production
    :cvar SALE: sale
    :cvar STORAGE: storage
    :cvar UNKNOWN: unknown
    """
    CONSUME = "consume"
    CONSUME_BLACK_START = "consume - black start"
    CONSUME_COMPRESSOR = "consume - compressor"
    CONSUME_EMITTED = "consume - emitted"
    CONSUME_FLARE = "consume - flare"
    CONSUME_FUEL = "consume - fuel"
    CONSUME_HP_FLARE = "consume - HP flare"
    CONSUME_LP_FLARE = "consume - LP flare"
    CONSUME_NON_COMPRESSOR = "consume - non compressor"
    CONSUME_VENTING = "consume - venting"
    DISPOSAL = "disposal"
    EXPORT = "export"
    EXPORT_NOMINATED = "export - nominated"
    EXPORT_REQUESTED = "export - requested"
    EXPORT_SHORTFALL = "export - shortfall"
    GAS_LIFT = "gas lift"
    HYDROCARBON_ACCOUNTING = "hydrocarbon accounting"
    IMPORT = "import"
    INJECTION = "injection"
    INVENTORY = "inventory"
    OVERBOARD = "overboard"
    PRODUCTION = "production"
    SALE = "sale"
    STORAGE = "storage"
    UNKNOWN = "unknown"
