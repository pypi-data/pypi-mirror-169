from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class BalanceFlowPart(Enum):
    """
    Specifies the kinds of subdivisions of a flow related to the stock balance.

    :cvar ADJUSTED_CLOSING: Volume that remains after the operation of
        transfer.
    :cvar CLOSING_BALANCE: A volume that is the total volume on stock at
        the end of a time period.
    :cvar CLOSING_STORAGE_INVENTORY: A closing storage balance that is
        adjusted according to imbalance at end of period.
    :cvar COMPLETED_LIFTING: A volume that is the total volume of a
        hydrocarbon product  that is exported from a stock within a
        given time period.
    :cvar GAIN_LOSS: A volume that is a lack of proper proportion or
        relation between the corresponding input and lifting
        transactions.
    :cvar INPUT_TO_STORAGE: A volume that is the total volume of
        additions to a stock within a given time period.
    :cvar LIFTED: A volume that is transferred ("lifted").
    :cvar LIFTING_ENTITLEMENT: A volume that is the contracted volume
        which can be transferred.
    :cvar LIFTING_ENTITLEMENT_REMAINING: A volume that is the contracted
        volume which is not transferred but which remains available for
        subsequent transfer.
    :cvar LINEPACK: A gas volume that is the quantity of gas which the
        operator responsible for gas transportation decides must be
        provided by the gas producing fields in order to make deliveries
        as requested by gas shippers and provide operating tolerances.
    :cvar OPENING_BALANCE: A volume that is the total volume on stock at
        the beginning of a time period.
    :cvar OPFLEX: A gas volume that is the unused and available quantity
        of gas within a gas transportation system and/or at one or many
        gas producing fields that is accessible by the operator
        responsible for gas transportation for the purposes of
        alleviating field curtailment.
    :cvar PARTIAL_LIFTING: A volume that is the volume of a hydrocarbon
        product lifting up to a (not completed) determined point in
        time.
    :cvar PIPELINE_LIFTING: A volume that is the volume of a hydrocarbon
        product lifting transferred by pipeline.
    :cvar PRODUCTION_MASS_ADJUSTMENT: A part of a mass adjustment
        process of a given production volume.
    :cvar PRODUCTION_VALUE_ADJUSTMENT: A value that is adjusted due to a
        change in the value of a product.
    :cvar PRODUCTION_IMBALANCE: A gas volume that is the difference
        between gas volume entering and exiting a shipper's nomination
        portfolio. This will take into account all differences whatever
        the time or reason it occurs.
    :cvar SWAP: A swap of a volume in between different parties (often
        used in crude sales),e.g. "I have this volume with this quality
        and value and you can give me this higher volume for it with a
        lower quality."
    :cvar TANKER_LIFTING: A volume that is the volume of a hydrocarbon
        product lifting transferred by tanker.
    :cvar TRANSACTION: Typically used within the cargo shipper
        operations and in this context: is a change in ownership as
        executed between shippers of the cargo.
    :cvar TRANSFER: A volume that is the volume of a hydrocarbon product
        which changes custody in the operation.
    :cvar UNKNOWN: Unknown.
    """
    ADJUSTED_CLOSING = "adjusted closing"
    CLOSING_BALANCE = "closing balance"
    CLOSING_STORAGE_INVENTORY = "closing storage inventory"
    COMPLETED_LIFTING = "completed lifting"
    GAIN_LOSS = "gain/loss"
    INPUT_TO_STORAGE = "input to storage"
    LIFTED = "lifted"
    LIFTING_ENTITLEMENT = "lifting entitlement"
    LIFTING_ENTITLEMENT_REMAINING = "lifting entitlement remaining"
    LINEPACK = "linepack"
    OPENING_BALANCE = "opening balance"
    OPFLEX = "opflex"
    PARTIAL_LIFTING = "partial lifting"
    PIPELINE_LIFTING = "pipeline lifting"
    PRODUCTION_MASS_ADJUSTMENT = "production - mass adjustment"
    PRODUCTION_VALUE_ADJUSTMENT = "production -- value adjustment"
    PRODUCTION_IMBALANCE = "production imbalance"
    SWAP = "swap"
    TANKER_LIFTING = "tanker lifting"
    TRANSACTION = "transaction"
    TRANSFER = "transfer"
    UNKNOWN = "unknown"
