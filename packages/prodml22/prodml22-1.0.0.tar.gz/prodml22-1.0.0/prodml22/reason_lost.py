from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReasonLost(Enum):
    """
    Specifies the reasons for lost production.

    :cvar VALUE_3RD_PARTY_PROCESSING: 3rd party processing
    :cvar DAILY_TOTAL_LOSS_OF_PROD: daily total loss of prod
    :cvar EXTENDED_MAINT_TURNAROUND: extended maint turnaround
    :cvar EXTENDED_MAINT_TURNAROUND_EXPORT: extended maint turnaround
        export
    :cvar HSE: hse
    :cvar MARKED_GAS: marked gas
    :cvar MARKED_OIL: marked oil
    :cvar MODIFICATION_PROJECT: modification project
    :cvar OPERATION_MISTAKES: operation mistakes
    :cvar OTHER: other
    :cvar PLANNED_MAINT_TURNAROUND: planned maint turnaround
    :cvar PREVENTIVE_MAINT_TOPSIDE: preventive maint topside
    :cvar PROCESS_AND_OPERATION_PROBLEM: process and operation problem
    :cvar PRODUCTION: production
    :cvar REGULATORY_REFERENCE: regulatory reference
    :cvar RESERVOIR: reservoir
    :cvar STRIKE_LOCK_OUT: strike/lock-out
    :cvar TESTING_AND_LOGGING: testing and logging
    :cvar TOPSIDE_EQUIPMENT_FAILURE_MAINT: topside equipment failure-
        maint
    :cvar UNAVAILABLE_TANKER_STORAGE: unavailable tanker storage
    :cvar UNKNOWN: unknown
    :cvar WEATHER_PROBLEM: weather problem
    :cvar WELL_EQUIPMENT_FAILURE_MAINT: well equipment failure-maint
    :cvar WELL_PLANNED_OPERATIONS: well planned operations
    :cvar WELL_PREVENTIVE_MAINT: well preventive maint
    :cvar WELL_PROBLEMS: well problems
    """
    VALUE_3RD_PARTY_PROCESSING = "3rd party processing"
    DAILY_TOTAL_LOSS_OF_PROD = "daily total loss of prod"
    EXTENDED_MAINT_TURNAROUND = "extended maint turnaround"
    EXTENDED_MAINT_TURNAROUND_EXPORT = "extended maint turnaround export"
    HSE = "hse"
    MARKED_GAS = "marked gas"
    MARKED_OIL = "marked oil"
    MODIFICATION_PROJECT = "modification project"
    OPERATION_MISTAKES = "operation mistakes"
    OTHER = "other"
    PLANNED_MAINT_TURNAROUND = "planned maint turnaround"
    PREVENTIVE_MAINT_TOPSIDE = "preventive maint topside"
    PROCESS_AND_OPERATION_PROBLEM = "process and operation problem"
    PRODUCTION = "production"
    REGULATORY_REFERENCE = "regulatory reference"
    RESERVOIR = "reservoir"
    STRIKE_LOCK_OUT = "strike/lock-out"
    TESTING_AND_LOGGING = "testing and logging"
    TOPSIDE_EQUIPMENT_FAILURE_MAINT = "topside equipment failure-maint"
    UNAVAILABLE_TANKER_STORAGE = "unavailable tanker storage"
    UNKNOWN = "unknown"
    WEATHER_PROBLEM = "weather problem"
    WELL_EQUIPMENT_FAILURE_MAINT = "well equipment failure-maint"
    WELL_PLANNED_OPERATIONS = "well planned operations"
    WELL_PREVENTIVE_MAINT = "well preventive maint"
    WELL_PROBLEMS = "well problems"
