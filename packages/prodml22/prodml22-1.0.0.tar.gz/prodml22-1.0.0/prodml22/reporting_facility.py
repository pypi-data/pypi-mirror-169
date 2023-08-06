from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class ReportingFacility(Enum):
    """
    Specifies the kinds of facilities (usage of equipment or material) that can
    be reported on.

    :cvar BLOCK_VALVE: block valve
    :cvar BOTTOMHOLE: bottomhole
    :cvar CASING: casing
    :cvar CHOKE: choke
    :cvar CLUSTER: cluster
    :cvar COMMERCIAL_ENTITY: commercial entity
    :cvar COMPANY: company
    :cvar COMPLETION: completion
    :cvar COMPRESSOR: compressor
    :cvar CONTROLLER: controller
    :cvar CONTROLLER_LIFT: controller -- lift
    :cvar COUNTRY: country
    :cvar COUNTY: county
    :cvar DOWNHOLE_MONITORING_SYSTEM: downhole monitoring system
    :cvar ELECTRIC_SUBMERSIBLE_PUMP: electric submersible pump
    :cvar FIELD: field
    :cvar FIELD_AREA: field - area
    :cvar FIELD_GROUP: field - group
    :cvar FIELD_PART: field - part
    :cvar FLOW_METER: flow meter
    :cvar FLOWLINE: flowline
    :cvar FORMATION: formation
    :cvar GAS_LIFT_VALVE_MANDREL: gas lift valve mandrel
    :cvar GENERATOR: generator
    :cvar INSTALLATION: installation
    :cvar LEASE: lease
    :cvar LICENSE: license
    :cvar MANIFOLD: manifold
    :cvar ORGANIZATIONAL_UNIT: organizational unit
    :cvar PACKER: packer
    :cvar PERFORATED_INTERVAL: perforated interval
    :cvar PIPELINE: pipeline
    :cvar PLANT_PROCESSING: plant - processing
    :cvar PLATFORM: platform
    :cvar PRESSURE_METER: pressure meter
    :cvar PROCESSING_FACILITY: processing facility
    :cvar PRODUCTION_TUBING: production tubing
    :cvar PUMP: pump
    :cvar RECTIFIER: rectifier
    :cvar REGULATING_VALVE: regulating valve
    :cvar REMOTE_TERMINAL_UNIT: remote terminal unit
    :cvar RESERVOIR: reservoir
    :cvar SEPARATOR: separator
    :cvar SLEEVE_VALVE: sleeve valve
    :cvar STATE: state
    :cvar STORAGE: storage
    :cvar TANK: tank
    :cvar TEMPERATURE_METER: temperature meter
    :cvar TEMPLATE: template
    :cvar TERMINAL: terminal
    :cvar TRAP: trap
    :cvar TRUNKLINE: trunkline
    :cvar TUBING_HEAD: tubing head
    :cvar TURBINE: turbine
    :cvar UNKNOWN: unknown
    :cvar WELL: well
    :cvar WELL_GROUP: well group
    :cvar WELLBORE: wellbore
    :cvar WELLHEAD: wellhead
    :cvar ZONE: zone
    """
    BLOCK_VALVE = "block valve"
    BOTTOMHOLE = "bottomhole"
    CASING = "casing"
    CHOKE = "choke"
    CLUSTER = "cluster"
    COMMERCIAL_ENTITY = "commercial entity"
    COMPANY = "company"
    COMPLETION = "completion"
    COMPRESSOR = "compressor"
    CONTROLLER = "controller"
    CONTROLLER_LIFT = "controller -- lift"
    COUNTRY = "country"
    COUNTY = "county"
    DOWNHOLE_MONITORING_SYSTEM = "downhole monitoring system"
    ELECTRIC_SUBMERSIBLE_PUMP = "electric submersible pump"
    FIELD = "field"
    FIELD_AREA = "field - area"
    FIELD_GROUP = "field - group"
    FIELD_PART = "field - part"
    FLOW_METER = "flow meter"
    FLOWLINE = "flowline"
    FORMATION = "formation"
    GAS_LIFT_VALVE_MANDREL = "gas lift valve mandrel"
    GENERATOR = "generator"
    INSTALLATION = "installation"
    LEASE = "lease"
    LICENSE = "license"
    MANIFOLD = "manifold"
    ORGANIZATIONAL_UNIT = "organizational unit"
    PACKER = "packer"
    PERFORATED_INTERVAL = "perforated interval"
    PIPELINE = "pipeline"
    PLANT_PROCESSING = "plant - processing"
    PLATFORM = "platform"
    PRESSURE_METER = "pressure meter"
    PROCESSING_FACILITY = "processing facility"
    PRODUCTION_TUBING = "production tubing"
    PUMP = "pump"
    RECTIFIER = "rectifier"
    REGULATING_VALVE = "regulating valve"
    REMOTE_TERMINAL_UNIT = "remote terminal unit"
    RESERVOIR = "reservoir"
    SEPARATOR = "separator"
    SLEEVE_VALVE = "sleeve valve"
    STATE = "state"
    STORAGE = "storage"
    TANK = "tank"
    TEMPERATURE_METER = "temperature meter"
    TEMPLATE = "template"
    TERMINAL = "terminal"
    TRAP = "trap"
    TRUNKLINE = "trunkline"
    TUBING_HEAD = "tubing head"
    TURBINE = "turbine"
    UNKNOWN = "unknown"
    WELL = "well"
    WELL_GROUP = "well group"
    WELLBORE = "wellbore"
    WELLHEAD = "wellhead"
    ZONE = "zone"
