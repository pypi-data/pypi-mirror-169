from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class SafetyType(Enum):
    """
    Specifies the types of safety issues for which a count can be defined.

    :cvar DRILL_OR_EXERCISE: drill or exercise
    :cvar FIRE: fire
    :cvar FIRST_AID: first aid
    :cvar HAZARD_REPORT_CARD: hazard report card
    :cvar JOB_OBSERVATION: job observation
    :cvar LOST_TIME_ACCIDENT: lost time accident
    :cvar LOST_TIME_INCIDENT: lost time incident
    :cvar MISCELLANEOUS: miscellaneous
    :cvar NEAR_MISS: near miss
    :cvar PERMIT_WITH_SJA: permit with SJA
    :cvar RELEASED_TO_AIR: released to air
    :cvar RELEASED_TO_WATER: released to water
    :cvar RESTRICTED_WORK: restricted work
    :cvar SAFETY_MEETING: safety meeting
    :cvar SENT_ASHORE: sent ashore
    :cvar SEVERE_ACCIDENT: severe accident
    :cvar SICK_ON_BOARD: sick on board
    :cvar SPILL_OR_LEAK: spill or leak
    :cvar TOTAL_PERMITS: total permits
    :cvar TRAFFIC_ACCIDENT: traffic accident
    :cvar YEAR_TO_DATE_INCIDENTS: year-to-date incidents
    """
    DRILL_OR_EXERCISE = "drill or exercise"
    FIRE = "fire"
    FIRST_AID = "first aid"
    HAZARD_REPORT_CARD = "hazard report card"
    JOB_OBSERVATION = "job observation"
    LOST_TIME_ACCIDENT = "lost time accident"
    LOST_TIME_INCIDENT = "lost time incident"
    MISCELLANEOUS = "miscellaneous"
    NEAR_MISS = "near miss"
    PERMIT_WITH_SJA = "permit with SJA"
    RELEASED_TO_AIR = "released to air"
    RELEASED_TO_WATER = "released to water"
    RESTRICTED_WORK = "restricted work"
    SAFETY_MEETING = "safety meeting"
    SENT_ASHORE = "sent ashore"
    SEVERE_ACCIDENT = "severe accident"
    SICK_ON_BOARD = "sick on board"
    SPILL_OR_LEAK = "spill or leak"
    TOTAL_PERMITS = "total permits"
    TRAFFIC_ACCIDENT = "traffic accident"
    YEAR_TO_DATE_INCIDENTS = "year-to-date incidents"
