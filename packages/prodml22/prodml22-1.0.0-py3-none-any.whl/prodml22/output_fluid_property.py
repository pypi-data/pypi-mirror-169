from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/prodmlv2"


class OutputFluidProperty(Enum):
    """
    Specifies the output fluid properties.

    :cvar COMPRESSIBILITY: Compressibility (expected to be defined for a
        phase). UoM: 1/pressure.
    :cvar DENSITY: Density (expected to be defined for a phase). UoM:
        mass/volume.
    :cvar DERIVATIVE_OF_DENSITY_W_R_T_PRESSURE: Derivative of density
        w.r.t pressure (expected to be defined for a phase). UoM:
        density/pressure.
    :cvar DERIVATIVE_OF_DENSITY_W_R_T_TEMPERATURE: Derivative of density
        w.r.t temperature (expected to be defined for a phase). UoM:
        density/temperature.
    :cvar ENTHALPY: Enthalpy (expected to be defined for a phase). UoM:
        energy/mass.
    :cvar ENTROPY: Entropy (expected to be defined for a phase). UoM:
        energy/temperature.
    :cvar EXPANSION_FACTOR: Expansion factor - volume expanded/volume in
        reservoir (expected to be defined for a phase). UoM:
        volume/volume.
    :cvar FORMATION_VOLUME_FACTOR: Formation volume factor - volume in
        reservoir/volume expanded (expected to be defined for a phase).
        UoM: volume/volume.
    :cvar GAS_OIL_INTERFACIAL_TENSION: Gas-oil interfacial tension. UoM:
        force/length.
    :cvar GAS_WATER_INTERFACIAL_TENSION: Gas-water interfacial tension.
        UoM: force/length.
    :cvar INDEX: Index number (which will be the index of a row in the
        table). UoM: integer.
    :cvar K_VALUE: The ratio of vapor concentration to liquid
        concentration at equilibrium (expected to be defined for a
        phase). UoM: dimensionless.
    :cvar MISC_BANK_CRITICAL_SOLVENT_SATURATION: The critical solvent
        saturation of a miscible bank . UoM: volume/volume.
    :cvar MISC_BANK_PHASE_DENSITY: The density of a phase within a
        miscible bank  (expected to be defined for a phase). UoM:
        density.
    :cvar MISC_BANK_PHASE_VISCOSITY: The viscosity of a phase within a
        miscible bank  (expected to be defined for a phase). UoM:
        viscosity.
    :cvar MISCIBILITY_PARAMETER_ALPHA: The critical solvent saturation
        of a miscible bank.
    :cvar MIXING_PARAMETER_OIL_GAS: Mixing parameter for oil and gas.
    :cvar NORMALIZED_PSEUDO_PRESSURE: Normalised pseudo pressure derived
        from Pseudo Pressure m(P) as follows Normalized pseudo pressure
        = m(P)*ref viscosity/ref pressure. The reference viscosity and
        pressure used in this normalization should be reported as Table
        Constants in the table in which this Normalized pseudo pressure
        is tabulated versus pressure. Normalized pseudo pressure is used
        in gas well and multi-phase pressure transient analysis.
    :cvar OIL_GAS_RATIO: The oil-gas ratio in a vapour-liquid system.
        UoM: volume/volume.
    :cvar OIL_WATER_INTERFACIAL_TENSION: Oil-water interfacial tension.
    :cvar PARACHOR: Parachor is the quantity defined according to the
        formula: P = ?1/4 M / D. Where ?1/4 is the fourth root of
        surface tension.
    :cvar PRESSURE: Pressure. UoM: pressure.
    :cvar PSEUDO_PRESSURE: Pseudo pressure with measurement units
        pressure^2/viscosity and usual symbol m(P). Tabulated versus
        pressure and used in gas well pressure transient analysis.
    :cvar P_T_CROSS_TERM: This is a specific parameter unique to CMG
        software.
    :cvar SATURATION_PRESSURE: The saturation pressure of a mixture.
        UoM: pressure.
    :cvar SOLUTION_GOR: The gas-oil ratio in a liquid-vapour system.
        UoM: volume/volume.
    :cvar SOLVENT_DENSITY: The density of a solvent phase. UoM: density.
    :cvar SPECIFIC_HEAT: The amount of heat per unit mass required to
        raise the temperature by one unit temperature (expected to be
        defined for a phase). UoM: energy/mass/temperature.
    :cvar TEMPERATURE: Temperature. UoM: temperature.
    :cvar THERMAL_CONDUCTIVITY: Thermal conductivity (expected to be
        defined for a phase). UoM: power/length.temperature.
    :cvar VISCOSITY: Viscosity (expected to be defined for a phase).
        UoM: viscosity.
    :cvar VISCOSITY_COMPRESSIBILITY: Slope of viscosity change with
        pressure in a semi-log plot (1/psi) (expected to be defined for
        a phase). UoM: viscosity/pressure.
    :cvar WATER_VAPOR_MASS_FRACTION_IN_GAS_PHASE: The mass fraction of
        water in a gas phase. UoM: mass/mass.
    :cvar Z_FACTOR: The compressibility factor (z).
    """
    COMPRESSIBILITY = "Compressibility"
    DENSITY = "Density"
    DERIVATIVE_OF_DENSITY_W_R_T_PRESSURE = "Derivative of Density w.r.t Pressure"
    DERIVATIVE_OF_DENSITY_W_R_T_TEMPERATURE = "Derivative of Density w.r.t Temperature"
    ENTHALPY = "Enthalpy"
    ENTROPY = "Entropy"
    EXPANSION_FACTOR = "Expansion Factor"
    FORMATION_VOLUME_FACTOR = "Formation Volume Factor"
    GAS_OIL_INTERFACIAL_TENSION = "Gas-Oil Interfacial Tension"
    GAS_WATER_INTERFACIAL_TENSION = "Gas-Water Interfacial Tension"
    INDEX = "Index"
    K_VALUE = "K value"
    MISC_BANK_CRITICAL_SOLVENT_SATURATION = "Misc Bank Critical Solvent Saturation"
    MISC_BANK_PHASE_DENSITY = "Misc Bank Phase Density"
    MISC_BANK_PHASE_VISCOSITY = "Misc Bank Phase Viscosity"
    MISCIBILITY_PARAMETER_ALPHA = "Miscibility Parameter (Alpha)"
    MIXING_PARAMETER_OIL_GAS = "Mixing Parameter Oil-Gas"
    NORMALIZED_PSEUDO_PRESSURE = "Normalized Pseudo Pressure"
    OIL_GAS_RATIO = "Oil-Gas Ratio"
    OIL_WATER_INTERFACIAL_TENSION = "Oil-Water Interfacial Tension"
    PARACHOR = "Parachor"
    PRESSURE = "Pressure"
    PSEUDO_PRESSURE = "Pseudo Pressure"
    P_T_CROSS_TERM = "P-T Cross Term"
    SATURATION_PRESSURE = "Saturation Pressure"
    SOLUTION_GOR = "Solution GOR"
    SOLVENT_DENSITY = "Solvent Density"
    SPECIFIC_HEAT = "Specific Heat"
    TEMPERATURE = "Temperature"
    THERMAL_CONDUCTIVITY = "Thermal Conductivity"
    VISCOSITY = "Viscosity"
    VISCOSITY_COMPRESSIBILITY = "Viscosity Compressibility"
    WATER_VAPOR_MASS_FRACTION_IN_GAS_PHASE = "Water vapor mass fraction in gas phase"
    Z_FACTOR = "Z Factor"
