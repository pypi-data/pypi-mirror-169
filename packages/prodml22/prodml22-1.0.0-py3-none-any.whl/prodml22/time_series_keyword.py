from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class TimeSeriesKeyword(Enum):
    """
    Specifies the keywords used for defining keyword-value pairs in a time
    series.

    :cvar ASSET_IDENTIFIER: asset identifier
    :cvar FLOW: flow
    :cvar PRODUCT: product
    :cvar QUALIFIER: qualifier
    :cvar SUBQUALIFIER: subqualifier
    :cvar UNKNOWN: unknown
    """
    ASSET_IDENTIFIER = "asset identifier"
    FLOW = "flow"
    PRODUCT = "product"
    QUALIFIER = "qualifier"
    SUBQUALIFIER = "subqualifier"
    UNKNOWN = "unknown"
