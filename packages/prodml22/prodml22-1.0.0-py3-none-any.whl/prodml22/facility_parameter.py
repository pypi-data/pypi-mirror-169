from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class FacilityParameter(Enum):
    """
    Specifies the kinds of facility parameters.

    :cvar ABSORBED_DOSE_CLASS: The amount of energy absorbed per mass.
    :cvar ACCELERATION_LINEAR_CLASS: Acceleration linear class.
    :cvar ACTIVITY_OF_RADIOACTIVITY_CLASS: A measure of the radiation
        being emitted.
    :cvar ALARM_ABSOLUTE_PRESSURE: Absolute minimum pressure of the flow
        stream before the system gives an alarm. Equivalent to element
        absoluteMinPres in the ProductVolume data schema.
    :cvar AMOUNT_OF_SUBSTANCE_CLASS: Molar amount of a substance.
    :cvar ANGLE_PER_LENGTH: Angle per length.
    :cvar ANGLE_PER_TIME: The angular velocity. The rate of change of an
        angle.
    :cvar ANGLE_PER_VOLUME: Angle per volume.
    :cvar ANGULAR_ACCELERATION_CLASS: Angular acceleration class.
    :cvar ANNULUS_INNER_DIAMETER: Annulus inner diameter.
    :cvar ANNULUS_OUTER_DIAMETER: Annulus outer diameter.
    :cvar AREA_CLASS: Area class.
    :cvar AREA_PER_AREA: A dimensionless quantity where the basis of the
        ratio is area.
    :cvar AREA_PER_VOLUME: Area per volume.
    :cvar ATMOSPHERIC_PRESSURE: The average atmospheric pressure during
        the reporting period. Equivalent to element atmosphere in the
        ProductVolume data schema.
    :cvar ATTENUATION_CLASS: A logarithmic, fractional change of some
        measure, generally power or amplitude, over a standard range.
        This is generally used for frequency attenuation over an octave.
    :cvar ATTENUATION_PER_LENGTH: Attenuation per length.
    :cvar AVAILABLE: Indicates the availability of the facility. This
        should be implemented as a string value. A value of "true"
        indicates that it is available for use. That is, it may be
        currently shut-down but it can be restarted. A value of "false"
        indicates that the facility is not available to be used. That
        is, it cannot be restarted at this time.
    :cvar AVAILABLE_ROOM: Defines the unoccupied volume of a tank. Zero
        indicates that the tank is full.
    :cvar BLOCK_VALVE_STATUS: Indicates the status of a block valve.
        This should be implemented as a string value. A value of "open"
        indicates that it is open. A value of "closed" indicates that it
        is closed.
    :cvar CAPACITANCE_CLASS: Capacitance class.
    :cvar CATEGORICAL: The abstract supertype of all enumerated string
        properties.
    :cvar CATHODIC_PROTECTION_OUTPUT_CURRENT: Rectifier DC output
        current.
    :cvar CATHODIC_PROTECTION_OUTPUT_VOLTAGE: Rectifier DC output
        voltage.
    :cvar CHARGE_DENSITY_CLASS: Charge density class.
    :cvar CHEMICAL_POTENTIAL_CLASS: Chemical potential class.
    :cvar CHOKE_POSITION: A coded value describing the position of the
        choke (open, close, traveling).
    :cvar CHOKE_SETTING: A fraction value (percentage) of the choke
        opening.
    :cvar CODE: A property whose values are constrained to specific
        string values
    :cvar COMPRESSIBILITY_CLASS: Compressibility class.
    :cvar CONCENTRATION_OF_B_CLASS: Concentration of B class.
    :cvar CONDUCTIVITY_CLASS: Conductivity class.
    :cvar CONTINUOUS: Continuous.
    :cvar CROSS_SECTION_ABSORPTION_CLASS: Cross section absorption
        class.
    :cvar CURRENT_DENSITY_CLASS: Current density class.
    :cvar DARCY_FLOW_COEFFICIENT_CLASS: Darcy flow coefficient class.
    :cvar DATA_TRANSMISSION_SPEED_CLASS: Data transmission speed class.
    :cvar DELTA_TEMPERATURE_CLASS: Delta temperature class.
    :cvar DENSITY: Density.
    :cvar DENSITY_CLASS: Density class.
    :cvar DENSITY_FLOW_RATE: Density flow rate.
    :cvar DENSITY_STANDARD: Density standard.
    :cvar DEWPOINT_TEMPERATURE: Dewpoint temperature.
    :cvar DIFFERENTIAL_PRESSURE: Differential pressure.
    :cvar DIFFERENTIAL_TEMPERATURE: differential temperature
    :cvar DIFFUSION_COEFFICIENT_CLASS: diffusion coefficient class
    :cvar DIGITAL_STORAGE_CLASS: digital storage class
    :cvar DIMENSIONLESS_CLASS: dimensionless class
    :cvar DISCRETE: discrete
    :cvar DOSE_EQUIVALENT_CLASS: dose equivalent class
    :cvar DOSE_EQUIVALENT_RATE_CLASS: dose equivalent rate class
    :cvar DYNAMIC_VISCOSITY_CLASS: dynamic viscosity class
    :cvar ELECTRIC_CHARGE_CLASS: electric charge class
    :cvar ELECTRIC_CONDUCTANCE_CLASS: electric conductance class
    :cvar ELECTRIC_CURRENT_CLASS: electric current class
    :cvar ELECTRIC_DIPOLE_MOMENT_CLASS: electric dipole moment class
    :cvar ELECTRIC_FIELD_STRENGTH_CLASS: electric field strength class
    :cvar ELECTRIC_POLARIZATION_CLASS: electric polarization class
    :cvar ELECTRIC_POTENTIAL_CLASS: electric potential class
    :cvar ELECTRICAL_RESISTIVITY_CLASS: electrical resistivity class
    :cvar ELECTROCHEMICAL_EQUIVALENT_CLASS: electrochemical equivalent
        class
    :cvar ELECTROMAGNETIC_MOMENT_CLASS: electromagnetic moment class
    :cvar ENERGY_LENGTH_PER_AREA: energy length per area
    :cvar ENERGY_LENGTH_PER_TIME_AREA_TEMPERATURE: energy length per
        time area temperature
    :cvar ENERGY_PER_AREA: energy per area
    :cvar ENERGY_PER_LENGTH: energy per length
    :cvar EQUIVALENT_PER_MASS: equivalent per mass
    :cvar EQUIVALENT_PER_VOLUME: equivalent per volume
    :cvar EXPOSURE_RADIOACTIVITY_CLASS: exposure (radioactivity) class
    :cvar FACILITY_UPTIME: facility uptime
    :cvar FLOW_RATE: flow rate
    :cvar FLOW_RATE_STANDARD: flow rate standard
    :cvar FORCE_AREA_CLASS: force area class
    :cvar FORCE_CLASS: force class
    :cvar FORCE_LENGTH_PER_LENGTH: force length per length
    :cvar FORCE_PER_FORCE: force per force
    :cvar FORCE_PER_LENGTH: force per length
    :cvar FORCE_PER_VOLUME: force per volume
    :cvar FREQUENCY_CLASS: frequency class
    :cvar FREQUENCY_INTERVAL_CLASS: frequency interval class
    :cvar GAMMA_RAY_API_UNIT_CLASS: gamma ray API unit class
    :cvar GAS_LIQUID_RATIO: gas liquid ratio
    :cvar GAS_OIL_RATIO: gas oil ratio
    :cvar GROSS_CALORIFIC_VALUE_STANDARD: gross calorific value standard
    :cvar HEAT_CAPACITY_CLASS: heat capacity class
    :cvar HEAT_FLOW_RATE_CLASS: heat flow rate class
    :cvar HEAT_TRANSFER_COEFFICIENT_CLASS: heat transfer coefficient
        class
    :cvar ILLUMINANCE_CLASS: illuminance class
    :cvar INTERNAL_CONTROL_VALVE_STATUS: internal control valve status
    :cvar IRRADIANCE_CLASS: irradiance class
    :cvar ISOTHERMAL_COMPRESSIBILITY_CLASS: isothermal compressibility
        class
    :cvar KINEMATIC_VISCOSITY_CLASS: kinematic viscosity class
    :cvar LENGTH_CLASS: length class
    :cvar LENGTH_PER_LENGTH: length per length
    :cvar LENGTH_PER_TEMPERATURE: length per temperature
    :cvar LENGTH_PER_VOLUME: length per volume
    :cvar LEVEL_OF_POWER_INTENSITY_CLASS: level of power intensity class
    :cvar LIGHT_EXPOSURE_CLASS: light exposure class
    :cvar LINEAR_THERMAL_EXPANSION_CLASS: linear thermal expansion class
    :cvar LUMINANCE_CLASS: luminance class
    :cvar LUMINOUS_EFFICACY_CLASS: luminous efficacy class
    :cvar LUMINOUS_FLUX_CLASS: luminous flux class
    :cvar LUMINOUS_INTENSITY_CLASS: luminous intensity class
    :cvar MAGNETIC_DIPOLE_MOMENT_CLASS: magnetic dipole moment class
    :cvar MAGNETIC_FIELD_STRENGTH_CLASS: magnetic field strength class
    :cvar MAGNETIC_FLUX_CLASS: magnetic flux class
    :cvar MAGNETIC_INDUCTION_CLASS: magnetic induction class
    :cvar MAGNETIC_PERMEABILITY_CLASS: magnetic permeability class
    :cvar MAGNETIC_VECTOR_POTENTIAL_CLASS: magnetic vector potential
        class
    :cvar MASS: mass
    :cvar MASS_ATTENUATION_COEFFICIENT_CLASS: mass attenuation
        coefficient class
    :cvar MASS_CLASS: mass class
    :cvar MASS_CONCENTRATION: mass concentration
    :cvar MASS_CONCENTRATION_CLASS: mass concentration class
    :cvar MASS_FLOW_RATE_CLASS: mass flow rate class
    :cvar MASS_LENGTH_CLASS: mass length class
    :cvar MASS_PER_ENERGY: mass per energy
    :cvar MASS_PER_LENGTH: mass per length
    :cvar MASS_PER_TIME_PER_AREA: mass per time per area
    :cvar MASS_PER_TIME_PER_LENGTH: mass per time per length
    :cvar MASS_PER_VOLUME_PER_LENGTH: mass per volume per length
    :cvar MEASURED_DEPTH: measured depth
    :cvar MOBILITY_CLASS: mobility class
    :cvar MODULUS_OF_COMPRESSION_CLASS: modulus of compression class
    :cvar MOLAR_CONCENTRATION: molar concentration
    :cvar MOLAR_FRACTION: molar fraction
    :cvar MOLAR_HEAT_CAPACITY_CLASS: molar heat capacity class
    :cvar MOLAR_VOLUME_CLASS: molar volume class
    :cvar MOLE_PER_AREA: mole per area
    :cvar MOLE_PER_TIME: mole per time
    :cvar MOLE_PER_TIME_PER_AREA: mole per time per area
    :cvar MOLECULAR_WEIGHT: molecular weight
    :cvar MOMENT_OF_FORCE_CLASS: moment of force class
    :cvar MOMENT_OF_INERTIA_CLASS: moment of inertia class
    :cvar MOMENT_OF_SECTION_CLASS: moment of section class
    :cvar MOMENTUM_CLASS: momentum class
    :cvar MOTOR_CURRENT: motor current
    :cvar MOTOR_CURRENT_LEAKAGE: motor current leakage
    :cvar MOTOR_SPEED: motor speed
    :cvar MOTOR_TEMPERATURE: motor temperature
    :cvar MOTOR_VIBRATION: motor vibration
    :cvar MOTOR_VOLTAGE: motor voltage
    :cvar NEUTRON_API_UNIT_CLASS: neutron API unit class
    :cvar NON_DARCY_FLOW_COEFFICIENT_CLASS: nonDarcy flow coefficient
        class
    :cvar OPENING_SIZE: opening size
    :cvar OPERATIONS_PER_TIME: operations per time
    :cvar PARACHOR_CLASS: parachor class
    :cvar PER_AREA: per area
    :cvar PER_ELECTRIC_POTENTIAL: per electric potential
    :cvar PER_FORCE: per force
    :cvar PER_LENGTH: per length
    :cvar PER_MASS: per mass
    :cvar PER_VOLUME: per volume
    :cvar PERMEABILITY_LENGTH_CLASS: permeability length class
    :cvar PERMEABILITY_ROCK_CLASS: permeability rock class
    :cvar PERMEANCE_CLASS: permeance class
    :cvar PERMITTIVITY_CLASS: permittivity class
    :cvar P_H_CLASS: pH class
    :cvar PLANE_ANGLE_CLASS: plane angle class
    :cvar POTENTIAL_DIFFERENCE_PER_POWER_DROP: potential difference per
        power drop
    :cvar POWER_CLASS: power class
    :cvar POWER_PER_VOLUME: power per volume
    :cvar PRESSURE: pressure
    :cvar PRESSURE_CLASS: pressure class
    :cvar PRESSURE_PER_TIME: pressure per time
    :cvar PRESSURE_SQUARED_CLASS: pressure squared class
    :cvar PRESSURE_SQUARED_PER_FORCE_TIME_PER_AREA: pressure squared per
        force time per area
    :cvar PRESSURE_TIME_PER_VOLUME: pressure time per volume
    :cvar PRODUCTIVITY_INDEX_CLASS: productivity index class
    :cvar PUMP_COUNT_ONLINE: pump count online
    :cvar PUMP_STATUS: pump status
    :cvar QUANTITY: quantity
    :cvar QUANTITY_OF_LIGHT_CLASS: quantity of light class
    :cvar RADIANCE_CLASS: radiance class
    :cvar RADIANT_INTENSITY_CLASS: radiant intensity class
    :cvar RECIPROCATING_SPEED: reciprocating speed
    :cvar RECTIFIER_STRUCTURE_POTENTIAL: rectifier structure potential
    :cvar REID_VAPOR_PRESSURE: reid vapor pressure
    :cvar RELATIVE_OPENING_SIZE: relative opening size
    :cvar RELATIVE_POWER_CLASS: relative power class
    :cvar RELATIVE_TANK_LEVEL: relative tank level
    :cvar RELATIVE_TIME_CLASS: relative time class
    :cvar RELATIVE_VALVE_OPENING: relative valve opening
    :cvar RELUCTANCE_CLASS: reluctance class
    :cvar RESISTANCE_CLASS: resistance class
    :cvar RESISTIVITY_PER_LENGTH: resistivity per length
    :cvar ROOT_PROPERTY: root property
    :cvar SCHEDULED_DOWNTIME: scheduled downtime
    :cvar SECOND_MOMENT_OF_AREA_CLASS: second moment of area class
    :cvar SHUTDOWN_ORDER: shutdown order
    :cvar SHUTIN_PRESSURE: shutin pressure
    :cvar SHUTIN_TEMPERATURE: shutin temperature
    :cvar SOLID_ANGLE_CLASS: solid angle class
    :cvar SPECIFIC_ACTIVITY_OF_RADIOACTIVITY: specific activity (of
        radioactivity)
    :cvar SPECIFIC_ENERGY_CLASS: specific energy class
    :cvar SPECIFIC_GRAVITY: specific gravity
    :cvar SPECIFIC_HEAT_CAPACITY_CLASS: specific heat capacity class
    :cvar SPECIFIC_PRODUCTIVITY_INDEX_CLASS: specific productivity index
        class
    :cvar SPECIFIC_VOLUME_CLASS: specific volume class
    :cvar SUB_SURFACE_SAFETY_VALVE_STATUS: sub surface safety valve
        status
    :cvar SURFACE_DENSITY_CLASS: surface density class
    :cvar SURFACE_SAFETY_VALVE_STATUS: surface safety valve status
    :cvar TANK_FLUID_LEVEL: tank fluid level
    :cvar TANK_PRODUCT_STANDARD_VOLUME: tank product standard volume
    :cvar TANK_PRODUCT_VOLUME: tank product volume
    :cvar TEMPERATURE: temperature
    :cvar TEMPERATURE_PER_LENGTH: temperature per length
    :cvar TEMPERATURE_PER_TIME: temperature per time
    :cvar THERMAL_CONDUCTANCE_CLASS: thermal conductance class
    :cvar THERMAL_CONDUCTIVITY_CLASS: thermal conductivity class
    :cvar THERMAL_DIFFUSIVITY_CLASS: thermal diffusivity class
    :cvar THERMAL_INSULANCE_CLASS: thermal insulance class
    :cvar THERMAL_RESISTANCE_CLASS: thermal resistance class
    :cvar THERMODYNAMIC_TEMPERATURE_CLASS: thermodynamic temperature
        class
    :cvar TIME_CLASS: time class
    :cvar TIME_PER_LENGTH: time per length
    :cvar TIME_PER_VOLUME: time per volume
    :cvar TRUE_VAPOR_PRESSURE: true vapor pressure
    :cvar UNIT_PRODUCTIVITY_INDEX_CLASS: unit productivity index class
    :cvar UNITLESS: unitless
    :cvar UNKNOWN: unknown
    :cvar VALVE_OPENING: valve opening
    :cvar VALVE_STATUS: valve status
    :cvar VELOCITY_CLASS: velocity class
    :cvar VOLUME: volume
    :cvar VOLUME_CLASS: volume class
    :cvar VOLUME_CONCENTRATION: volume concentration
    :cvar VOLUME_FLOW_RATE_CLASS: volume flow rate class
    :cvar VOLUME_LENGTH_PER_TIME: volume length per time
    :cvar VOLUME_PER_AREA: volume per area
    :cvar VOLUME_PER_LENGTH: volume per length
    :cvar VOLUME_PER_TIME_PER_AREA: volume per time per area
    :cvar VOLUME_PER_TIME_PER_LENGTH: volume per time per length
    :cvar VOLUME_PER_TIME_PER_TIME: volume per time per time
    :cvar VOLUME_PER_TIME_PER_VOLUME: volume per time per volume
    :cvar VOLUME_PER_VOLUME: volume per volume
    :cvar VOLUME_STANDARD: volume standard
    :cvar VOLUMETRIC_EFFICIENCY: volumetric efficiency
    :cvar VOLUMETRIC_HEAT_TRANSFER_COEFFICIENT: volumetric heat transfer
        coefficient
    :cvar VOLUMETRIC_THERMAL_EXPANSION_CLASS: volumetric thermal
        expansion class
    :cvar WELL_OPERATING_STATUS: well operating status
    :cvar WELL_OPERATION_TYPE: well operation type
    :cvar WOBBE_INDEX: wobbe index
    :cvar WORK: work
    :cvar WORK_CLASS: work class
    """
    ABSORBED_DOSE_CLASS = "absorbed dose class"
    ACCELERATION_LINEAR_CLASS = "acceleration linear class"
    ACTIVITY_OF_RADIOACTIVITY_CLASS = "activity (of radioactivity) class"
    ALARM_ABSOLUTE_PRESSURE = "alarm absolute pressure"
    AMOUNT_OF_SUBSTANCE_CLASS = "amount of substance class"
    ANGLE_PER_LENGTH = "angle per length"
    ANGLE_PER_TIME = "angle per time"
    ANGLE_PER_VOLUME = "angle per volume"
    ANGULAR_ACCELERATION_CLASS = "angular acceleration class"
    ANNULUS_INNER_DIAMETER = "annulus inner diameter"
    ANNULUS_OUTER_DIAMETER = "annulus outer diameter"
    AREA_CLASS = "area class"
    AREA_PER_AREA = "area per area"
    AREA_PER_VOLUME = "area per volume"
    ATMOSPHERIC_PRESSURE = "atmospheric pressure"
    ATTENUATION_CLASS = "attenuation class"
    ATTENUATION_PER_LENGTH = "attenuation per length"
    AVAILABLE = "available"
    AVAILABLE_ROOM = "available room"
    BLOCK_VALVE_STATUS = "block valve status"
    CAPACITANCE_CLASS = "capacitance class"
    CATEGORICAL = "categorical"
    CATHODIC_PROTECTION_OUTPUT_CURRENT = "cathodic protection output current"
    CATHODIC_PROTECTION_OUTPUT_VOLTAGE = "cathodic protection output voltage"
    CHARGE_DENSITY_CLASS = "charge density class"
    CHEMICAL_POTENTIAL_CLASS = "chemical potential class"
    CHOKE_POSITION = "choke position"
    CHOKE_SETTING = "choke setting"
    CODE = "code"
    COMPRESSIBILITY_CLASS = "compressibility class"
    CONCENTRATION_OF_B_CLASS = "concentration of B class"
    CONDUCTIVITY_CLASS = "conductivity class"
    CONTINUOUS = "continuous"
    CROSS_SECTION_ABSORPTION_CLASS = "cross section absorption class"
    CURRENT_DENSITY_CLASS = "current density class"
    DARCY_FLOW_COEFFICIENT_CLASS = "darcy flow coefficient class"
    DATA_TRANSMISSION_SPEED_CLASS = "data transmission speed class"
    DELTA_TEMPERATURE_CLASS = "delta temperature class"
    DENSITY = "density"
    DENSITY_CLASS = "density class"
    DENSITY_FLOW_RATE = "density flow rate"
    DENSITY_STANDARD = "density standard"
    DEWPOINT_TEMPERATURE = "dewpoint temperature"
    DIFFERENTIAL_PRESSURE = "differential pressure"
    DIFFERENTIAL_TEMPERATURE = "differential temperature"
    DIFFUSION_COEFFICIENT_CLASS = "diffusion coefficient class"
    DIGITAL_STORAGE_CLASS = "digital storage class"
    DIMENSIONLESS_CLASS = "dimensionless class"
    DISCRETE = "discrete"
    DOSE_EQUIVALENT_CLASS = "dose equivalent class"
    DOSE_EQUIVALENT_RATE_CLASS = "dose equivalent rate class"
    DYNAMIC_VISCOSITY_CLASS = "dynamic viscosity class"
    ELECTRIC_CHARGE_CLASS = "electric charge class"
    ELECTRIC_CONDUCTANCE_CLASS = "electric conductance class"
    ELECTRIC_CURRENT_CLASS = "electric current class"
    ELECTRIC_DIPOLE_MOMENT_CLASS = "electric dipole moment class"
    ELECTRIC_FIELD_STRENGTH_CLASS = "electric field strength class"
    ELECTRIC_POLARIZATION_CLASS = "electric polarization class"
    ELECTRIC_POTENTIAL_CLASS = "electric potential class"
    ELECTRICAL_RESISTIVITY_CLASS = "electrical resistivity class"
    ELECTROCHEMICAL_EQUIVALENT_CLASS = "electrochemical equivalent class"
    ELECTROMAGNETIC_MOMENT_CLASS = "electromagnetic moment class"
    ENERGY_LENGTH_PER_AREA = "energy length per area"
    ENERGY_LENGTH_PER_TIME_AREA_TEMPERATURE = "energy length per time area temperature"
    ENERGY_PER_AREA = "energy per area"
    ENERGY_PER_LENGTH = "energy per length"
    EQUIVALENT_PER_MASS = "equivalent per mass"
    EQUIVALENT_PER_VOLUME = "equivalent per volume"
    EXPOSURE_RADIOACTIVITY_CLASS = "exposure (radioactivity) class"
    FACILITY_UPTIME = "facility uptime"
    FLOW_RATE = "flow rate"
    FLOW_RATE_STANDARD = "flow rate standard"
    FORCE_AREA_CLASS = "force area class"
    FORCE_CLASS = "force class"
    FORCE_LENGTH_PER_LENGTH = "force length per length"
    FORCE_PER_FORCE = "force per force"
    FORCE_PER_LENGTH = "force per length"
    FORCE_PER_VOLUME = "force per volume"
    FREQUENCY_CLASS = "frequency class"
    FREQUENCY_INTERVAL_CLASS = "frequency interval class"
    GAMMA_RAY_API_UNIT_CLASS = "gamma ray API unit class"
    GAS_LIQUID_RATIO = "gas liquid ratio"
    GAS_OIL_RATIO = "gas oil ratio"
    GROSS_CALORIFIC_VALUE_STANDARD = "gross calorific value standard"
    HEAT_CAPACITY_CLASS = "heat capacity class"
    HEAT_FLOW_RATE_CLASS = "heat flow rate class"
    HEAT_TRANSFER_COEFFICIENT_CLASS = "heat transfer coefficient class"
    ILLUMINANCE_CLASS = "illuminance class"
    INTERNAL_CONTROL_VALVE_STATUS = "internal control valve status"
    IRRADIANCE_CLASS = "irradiance class"
    ISOTHERMAL_COMPRESSIBILITY_CLASS = "isothermal compressibility class"
    KINEMATIC_VISCOSITY_CLASS = "kinematic viscosity class"
    LENGTH_CLASS = "length class"
    LENGTH_PER_LENGTH = "length per length"
    LENGTH_PER_TEMPERATURE = "length per temperature"
    LENGTH_PER_VOLUME = "length per volume"
    LEVEL_OF_POWER_INTENSITY_CLASS = "level of power intensity class"
    LIGHT_EXPOSURE_CLASS = "light exposure class"
    LINEAR_THERMAL_EXPANSION_CLASS = "linear thermal expansion class"
    LUMINANCE_CLASS = "luminance class"
    LUMINOUS_EFFICACY_CLASS = "luminous efficacy class"
    LUMINOUS_FLUX_CLASS = "luminous flux class"
    LUMINOUS_INTENSITY_CLASS = "luminous intensity class"
    MAGNETIC_DIPOLE_MOMENT_CLASS = "magnetic dipole moment class"
    MAGNETIC_FIELD_STRENGTH_CLASS = "magnetic field strength class"
    MAGNETIC_FLUX_CLASS = "magnetic flux class"
    MAGNETIC_INDUCTION_CLASS = "magnetic induction class"
    MAGNETIC_PERMEABILITY_CLASS = "magnetic permeability class"
    MAGNETIC_VECTOR_POTENTIAL_CLASS = "magnetic vector potential class"
    MASS = "mass"
    MASS_ATTENUATION_COEFFICIENT_CLASS = "mass attenuation coefficient class"
    MASS_CLASS = "mass class"
    MASS_CONCENTRATION = "mass concentration"
    MASS_CONCENTRATION_CLASS = "mass concentration class"
    MASS_FLOW_RATE_CLASS = "mass flow rate class"
    MASS_LENGTH_CLASS = "mass length class"
    MASS_PER_ENERGY = "mass per energy"
    MASS_PER_LENGTH = "mass per length"
    MASS_PER_TIME_PER_AREA = "mass per time per area"
    MASS_PER_TIME_PER_LENGTH = "mass per time per length"
    MASS_PER_VOLUME_PER_LENGTH = "mass per volume per length"
    MEASURED_DEPTH = "measured depth"
    MOBILITY_CLASS = "mobility class"
    MODULUS_OF_COMPRESSION_CLASS = "modulus of compression class"
    MOLAR_CONCENTRATION = "molar concentration"
    MOLAR_FRACTION = "molar fraction"
    MOLAR_HEAT_CAPACITY_CLASS = "molar heat capacity class"
    MOLAR_VOLUME_CLASS = "molar volume class"
    MOLE_PER_AREA = "mole per area"
    MOLE_PER_TIME = "mole per time"
    MOLE_PER_TIME_PER_AREA = "mole per time per area"
    MOLECULAR_WEIGHT = "molecular weight"
    MOMENT_OF_FORCE_CLASS = "moment of force class"
    MOMENT_OF_INERTIA_CLASS = "moment of inertia class"
    MOMENT_OF_SECTION_CLASS = "moment of section class"
    MOMENTUM_CLASS = "momentum class"
    MOTOR_CURRENT = "motor current"
    MOTOR_CURRENT_LEAKAGE = "motor current leakage"
    MOTOR_SPEED = "motor speed"
    MOTOR_TEMPERATURE = "motor temperature"
    MOTOR_VIBRATION = "motor vibration"
    MOTOR_VOLTAGE = "motor voltage"
    NEUTRON_API_UNIT_CLASS = "neutron API unit class"
    NON_DARCY_FLOW_COEFFICIENT_CLASS = "nonDarcy flow coefficient class"
    OPENING_SIZE = "opening size"
    OPERATIONS_PER_TIME = "operations per time"
    PARACHOR_CLASS = "parachor class"
    PER_AREA = "per area"
    PER_ELECTRIC_POTENTIAL = "per electric potential"
    PER_FORCE = "per force"
    PER_LENGTH = "per length"
    PER_MASS = "per mass"
    PER_VOLUME = "per volume"
    PERMEABILITY_LENGTH_CLASS = "permeability length class"
    PERMEABILITY_ROCK_CLASS = "permeability rock class"
    PERMEANCE_CLASS = "permeance class"
    PERMITTIVITY_CLASS = "permittivity class"
    P_H_CLASS = "pH class"
    PLANE_ANGLE_CLASS = "plane angle class"
    POTENTIAL_DIFFERENCE_PER_POWER_DROP = "potential difference per power drop"
    POWER_CLASS = "power class"
    POWER_PER_VOLUME = "power per volume"
    PRESSURE = "pressure"
    PRESSURE_CLASS = "pressure class"
    PRESSURE_PER_TIME = "pressure per time"
    PRESSURE_SQUARED_CLASS = "pressure squared class"
    PRESSURE_SQUARED_PER_FORCE_TIME_PER_AREA = "pressure squared per force time per area"
    PRESSURE_TIME_PER_VOLUME = "pressure time per volume"
    PRODUCTIVITY_INDEX_CLASS = "productivity index class"
    PUMP_COUNT_ONLINE = "pump count online"
    PUMP_STATUS = "pump status"
    QUANTITY = "quantity"
    QUANTITY_OF_LIGHT_CLASS = "quantity of light class"
    RADIANCE_CLASS = "radiance class"
    RADIANT_INTENSITY_CLASS = "radiant intensity class"
    RECIPROCATING_SPEED = "reciprocating speed"
    RECTIFIER_STRUCTURE_POTENTIAL = "rectifier structure potential"
    REID_VAPOR_PRESSURE = "reid vapor pressure"
    RELATIVE_OPENING_SIZE = "relative opening size"
    RELATIVE_POWER_CLASS = "relative power class"
    RELATIVE_TANK_LEVEL = "relative tank level"
    RELATIVE_TIME_CLASS = "relative time class"
    RELATIVE_VALVE_OPENING = "relative valve opening"
    RELUCTANCE_CLASS = "reluctance class"
    RESISTANCE_CLASS = "resistance class"
    RESISTIVITY_PER_LENGTH = "resistivity per length"
    ROOT_PROPERTY = "root property"
    SCHEDULED_DOWNTIME = "scheduled downtime"
    SECOND_MOMENT_OF_AREA_CLASS = "second moment of area class"
    SHUTDOWN_ORDER = "shutdown order"
    SHUTIN_PRESSURE = "shutin pressure"
    SHUTIN_TEMPERATURE = "shutin temperature"
    SOLID_ANGLE_CLASS = "solid angle class"
    SPECIFIC_ACTIVITY_OF_RADIOACTIVITY = "specific activity (of radioactivity)"
    SPECIFIC_ENERGY_CLASS = "specific energy class"
    SPECIFIC_GRAVITY = "specific gravity"
    SPECIFIC_HEAT_CAPACITY_CLASS = "specific heat capacity class"
    SPECIFIC_PRODUCTIVITY_INDEX_CLASS = "specific productivity index class"
    SPECIFIC_VOLUME_CLASS = "specific volume class"
    SUB_SURFACE_SAFETY_VALVE_STATUS = "sub surface safety valve status"
    SURFACE_DENSITY_CLASS = "surface density class"
    SURFACE_SAFETY_VALVE_STATUS = "surface safety valve status"
    TANK_FLUID_LEVEL = "tank fluid level"
    TANK_PRODUCT_STANDARD_VOLUME = "tank product standard volume"
    TANK_PRODUCT_VOLUME = "tank product volume"
    TEMPERATURE = "temperature"
    TEMPERATURE_PER_LENGTH = "temperature per length"
    TEMPERATURE_PER_TIME = "temperature per time"
    THERMAL_CONDUCTANCE_CLASS = "thermal conductance class"
    THERMAL_CONDUCTIVITY_CLASS = "thermal conductivity class"
    THERMAL_DIFFUSIVITY_CLASS = "thermal diffusivity class"
    THERMAL_INSULANCE_CLASS = "thermal insulance class"
    THERMAL_RESISTANCE_CLASS = "thermal resistance class"
    THERMODYNAMIC_TEMPERATURE_CLASS = "thermodynamic temperature class"
    TIME_CLASS = "time class"
    TIME_PER_LENGTH = "time per length"
    TIME_PER_VOLUME = "time per volume"
    TRUE_VAPOR_PRESSURE = "true vapor pressure"
    UNIT_PRODUCTIVITY_INDEX_CLASS = "unit productivity index class"
    UNITLESS = "unitless"
    UNKNOWN = "unknown"
    VALVE_OPENING = "valve opening"
    VALVE_STATUS = "valve status"
    VELOCITY_CLASS = "velocity class"
    VOLUME = "volume"
    VOLUME_CLASS = "volume class"
    VOLUME_CONCENTRATION = "volume concentration"
    VOLUME_FLOW_RATE_CLASS = "volume flow rate class"
    VOLUME_LENGTH_PER_TIME = "volume length per time"
    VOLUME_PER_AREA = "volume per area"
    VOLUME_PER_LENGTH = "volume per length"
    VOLUME_PER_TIME_PER_AREA = "volume per time per area"
    VOLUME_PER_TIME_PER_LENGTH = "volume per time per length"
    VOLUME_PER_TIME_PER_TIME = "volume per time per time"
    VOLUME_PER_TIME_PER_VOLUME = "volume per time per volume"
    VOLUME_PER_VOLUME = "volume per volume"
    VOLUME_STANDARD = "volume standard"
    VOLUMETRIC_EFFICIENCY = "volumetric efficiency"
    VOLUMETRIC_HEAT_TRANSFER_COEFFICIENT = "volumetric heat transfer coefficient"
    VOLUMETRIC_THERMAL_EXPANSION_CLASS = "volumetric thermal expansion class"
    WELL_OPERATING_STATUS = "well operating status"
    WELL_OPERATION_TYPE = "well operation type"
    WOBBE_INDEX = "wobbe index"
    WORK = "work"
    WORK_CLASS = "work class"
