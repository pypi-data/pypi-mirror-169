from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReportingEntityKind(Enum):
    """
    Specifies the kinds of entities (usage of equipment or material) that can
    be reported on.

    :cvar BUSINESS_UNIT: business unit
    :cvar FPSO: fpso
    :cvar WELL_COMPLETION: well completion
    :cvar WELLBORE_COMPLETION: wellbore completion
    :cvar COMMERCIAL_ENTITY: commercial entity
    :cvar COMPANY: company
    :cvar CONTACT_INTERVAL: contact interval
    :cvar COUNTRY: country
    :cvar COUNTY: county
    :cvar FACILITY: facility
    :cvar FIELD: field
    :cvar FIELD_PART: field - part
    :cvar FLOW_METER: flow meter
    :cvar FORMATION: formation
    :cvar GAS_PLANT: gas plant
    :cvar LEASE: lease
    :cvar LICENSE: license
    :cvar PIPELINE: pipeline
    :cvar PLATFORM: platform
    :cvar PRODUCTION_PROCESSING_FACILITY: production processing facility
    :cvar RESERVOIR: reservoir
    :cvar ROCK_FLUID_UNIT_FEATURE: rock-fluid unit feature
    :cvar STATE: state
    :cvar TANK: tank
    :cvar TERMINAL: terminal
    :cvar WELL: well
    :cvar WELL_GROUP: well group
    :cvar WELLBORE: wellbore
    :cvar OIL_TANKER: oil tanker - ship
    :cvar TANKER_TRUCK: truck
    """
    BUSINESS_UNIT = "business unit"
    FPSO = "fpso"
    WELL_COMPLETION = "well completion"
    WELLBORE_COMPLETION = "wellbore completion"
    COMMERCIAL_ENTITY = "commercial entity"
    COMPANY = "company"
    CONTACT_INTERVAL = "contact interval"
    COUNTRY = "country"
    COUNTY = "county"
    FACILITY = "facility"
    FIELD = "field"
    FIELD_PART = "field - part"
    FLOW_METER = "flow meter"
    FORMATION = "formation"
    GAS_PLANT = "gas plant"
    LEASE = "lease"
    LICENSE = "license"
    PIPELINE = "pipeline"
    PLATFORM = "platform"
    PRODUCTION_PROCESSING_FACILITY = "production processing facility"
    RESERVOIR = "reservoir"
    ROCK_FLUID_UNIT_FEATURE = "rock-fluid unit feature"
    STATE = "state"
    TANK = "tank"
    TERMINAL = "terminal"
    WELL = "well"
    WELL_GROUP = "well group"
    WELLBORE = "wellbore"
    OIL_TANKER = "oil tanker"
    TANKER_TRUCK = "tanker truck"
