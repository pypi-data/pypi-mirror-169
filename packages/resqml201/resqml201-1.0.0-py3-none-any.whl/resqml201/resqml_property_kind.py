from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class ResqmlPropertyKind(Enum):
    """
    Enumeration of the standard set of RESQML property kinds.

    :cvar ABSORBED_DOSE: The amount of energy absorbed per mass.
    :cvar ACCELERATION_LINEAR:
    :cvar ACTIVITY_OF_RADIOACTIVITY: A measure of the radiation being
        emitted.
    :cvar AMOUNT_OF_SUBSTANCE: Molar amount of a substance.
    :cvar AMPLITUDE: Amplitude of the acoustic signal recorded. It is
        not a physical property, only a value.
    :cvar ANGLE_PER_LENGTH:
    :cvar ANGLE_PER_TIME: The angular velocity. The rate of change of an
        angle.
    :cvar ANGLE_PER_VOLUME:
    :cvar ANGULAR_ACCELERATION:
    :cvar AREA:
    :cvar AREA_PER_AREA: A dimensionless quantity where the basis of the
        ratio is area.
    :cvar AREA_PER_VOLUME:
    :cvar ATTENUATION: A logarithmic, fractional change of some measure,
        generally power or amplitude, over a standard range. This is
        generally used for frequency attenuation over an octave.
    :cvar ATTENUATION_PER_LENGTH:
    :cvar AZIMUTH: Angle between the North and the projection of the
        normal to the horizon surface estimated on a local area of the
        interface.
    :cvar BUBBLE_POINT_PRESSURE: The pressure at which the first gas
        bubble appears while decreasing pressure on a fluid sample.
    :cvar BULK_MODULUS: Bulk modulus, K
    :cvar CAPACITANCE:
    :cvar CATEGORICAL: The abstract supertype of all enumerated string
        properties.
    :cvar CELL_LENGTH: distance from cell face center to cell face
        center in the specified direction, DI, DJ, DK
    :cvar CHARGE_DENSITY:
    :cvar CHEMICAL_POTENTIAL:
    :cvar CODE: A discrete code.
    :cvar COMPRESSIBILITY:
    :cvar CONCENTRATION_OF_B: molar concentration of a substance.
    :cvar CONDUCTIVITY:
    :cvar CONTINUOUS: The abstract supertype of all floating point
        properties.
    :cvar CROSS_SECTION_ABSORPTION:
    :cvar CURRENT_DENSITY:
    :cvar DARCY_FLOW_COEFFICIENT:
    :cvar DATA_TRANSMISSION_SPEED: used primarily for computer
        transmission rates.
    :cvar DELTA_TEMPERATURE: Delta temperature refers to temperature
        differences. For non-zero offset temperature scales, Fahrenheit
        and Celsius, the conversion formulas are different than for
        absolute temperatures.
    :cvar DENSITY:
    :cvar DEPTH: The perpendicular measurement downward from a surface.
        Also, the direct linear measurement from the point of viewing
        usually from front to back.
    :cvar DIFFUSION_COEFFICIENT:
    :cvar DIGITAL_STORAGE:
    :cvar DIMENSIONLESS: A dimensionless quantity is the ratio of two
        dimensional quantities. The quantity types are not apparent from
        the basic dimensionless class, but may be apparent in variations
        - such as area per area, volume per volume, or mass per mass.
    :cvar DIP: In the azimuth direction, Angle between an horizon plane
        and an estimated plane on a local area of the interface.
    :cvar DISCRETE: The abstract supertype of all integer properties.
    :cvar DOSE_EQUIVALENT:
    :cvar DOSE_EQUIVALENT_RATE:
    :cvar DYNAMIC_VISCOSITY:
    :cvar ELECTRIC_CHARGE:
    :cvar ELECTRIC_CONDUCTANCE:
    :cvar ELECTRIC_CURRENT:
    :cvar ELECTRIC_DIPOLE_MOMENT:
    :cvar ELECTRIC_FIELD_STRENGTH:
    :cvar ELECTRIC_POLARIZATION:
    :cvar ELECTRIC_POTENTIAL:
    :cvar ELECTRICAL_RESISTIVITY:
    :cvar ELECTROCHEMICAL_EQUIVALENT: An electrochemical equivalent
        differs from molarity in that the valence (oxidation reduction
        potential) of the element is also considered.
    :cvar ELECTROMAGNETIC_MOMENT:
    :cvar ENERGY_LENGTH_PER_AREA:
    :cvar ENERGY_LENGTH_PER_TIME_AREA_TEMPERATURE:
    :cvar ENERGY_PER_AREA:
    :cvar ENERGY_PER_LENGTH:
    :cvar EQUIVALENT_PER_MASS:
    :cvar EQUIVALENT_PER_VOLUME:
    :cvar EXPOSURE_RADIOACTIVITY:
    :cvar FLUID_VOLUME: Volume of fluid
    :cvar FORCE:
    :cvar FORCE_AREA:
    :cvar FORCE_LENGTH_PER_LENGTH:
    :cvar FORCE_PER_FORCE: A dimensionless quantity where the basis of
        the ratio is force.
    :cvar FORCE_PER_LENGTH:
    :cvar FORCE_PER_VOLUME:
    :cvar FORMATION_VOLUME_FACTOR: Ratio of volumes at subsurface and
        surface conditions
    :cvar FREQUENCY:
    :cvar FREQUENCY_INTERVAL: An octave is a doubling of a frquency.
    :cvar GAMMA_RAY_API_UNIT: This class is defined by the API, and is
        used for units of gamma ray log response.
    :cvar HEAT_CAPACITY:
    :cvar HEAT_FLOW_RATE:
    :cvar HEAT_TRANSFER_COEFFICIENT: PRESSURE PER VELOCITY PER AREA
    :cvar ILLUMINANCE:
    :cvar INDEX: Serial ordering
    :cvar IRRADIANCE:
    :cvar ISOTHERMAL_COMPRESSIBILITY:
    :cvar KINEMATIC_VISCOSITY:
    :cvar LAMBDA_RHO: Product of Lame constant and density, LR
    :cvar LAME_CONSTANT: Lame constant, Lambda
    :cvar LENGTH:
    :cvar LENGTH_PER_LENGTH: A dimensionless quantity where the basis of
        the ratio is length.
    :cvar LENGTH_PER_TEMPERATURE:
    :cvar LENGTH_PER_VOLUME:
    :cvar LEVEL_OF_POWER_INTENSITY:
    :cvar LIGHT_EXPOSURE:
    :cvar LINEAR_THERMAL_EXPANSION:
    :cvar LUMINANCE:
    :cvar LUMINOUS_EFFICACY:
    :cvar LUMINOUS_FLUX:
    :cvar LUMINOUS_INTENSITY:
    :cvar MAGNETIC_DIPOLE_MOMENT:
    :cvar MAGNETIC_FIELD_STRENGTH:
    :cvar MAGNETIC_FLUX:
    :cvar MAGNETIC_INDUCTION:
    :cvar MAGNETIC_PERMEABILITY:
    :cvar MAGNETIC_VECTOR_POTENTIAL:
    :cvar MASS: M/L2T
    :cvar MASS_ATTENUATION_COEFFICIENT:
    :cvar MASS_CONCENTRATION: A dimensionless quantity where the basis
        of the ratio is mass.
    :cvar MASS_FLOW_RATE:
    :cvar MASS_LENGTH:
    :cvar MASS_PER_ENERGY:
    :cvar MASS_PER_LENGTH: M /L4T
    :cvar MASS_PER_TIME_PER_AREA:
    :cvar MASS_PER_TIME_PER_LENGTH:
    :cvar MASS_PER_VOLUME_PER_LENGTH:
    :cvar MOBILITY:
    :cvar MODULUS_OF_COMPRESSION:
    :cvar MOLAR_CONCENTRATION: molar concentration of a substance.
    :cvar MOLAR_HEAT_CAPACITY:
    :cvar MOLAR_VOLUME:
    :cvar MOLE_PER_AREA:
    :cvar MOLE_PER_TIME:
    :cvar MOLE_PER_TIME_PER_AREA:
    :cvar MOMENT_OF_FORCE:
    :cvar MOMENT_OF_INERTIA:
    :cvar MOMENT_OF_SECTION:
    :cvar MOMENTUM:
    :cvar MU_RHO: Product of Shear modulus and density, MR
    :cvar NET_TO_GROSS_RATIO: Ratio of net rock volume to gross rock
        volume, NTG
    :cvar NEUTRON_API_UNIT:
    :cvar NON_DARCY_FLOW_COEFFICIENT:
    :cvar OPERATIONS_PER_TIME:
    :cvar PARACHOR:
    :cvar PER_AREA:
    :cvar PER_ELECTRIC_POTENTIAL:
    :cvar PER_FORCE:
    :cvar PER_LENGTH:
    :cvar PER_MASS:
    :cvar PER_VOLUME:
    :cvar PERMEABILITY_LENGTH:
    :cvar PERMEABILITY_ROCK:
    :cvar PERMEABILITY_THICKNESS: Product of permeability and thickness
    :cvar PERMEANCE:
    :cvar PERMITTIVITY:
    :cvar P_H: The pH is a class that measures the hydrogen ion
        concentration (acidity).
    :cvar PLANE_ANGLE:
    :cvar POISSON_RATIO: Poisson's ratio, Sigma
    :cvar PORE_VOLUME: Volume of the Pore Space of the Rock
    :cvar POROSITY: porosity
    :cvar POTENTIAL_DIFFERENCE_PER_POWER_DROP:
    :cvar POWER:
    :cvar POWER_PER_VOLUME:
    :cvar PRESSURE:
    :cvar PRESSURE_PER_TIME:
    :cvar PRESSURE_SQUARED:
    :cvar PRESSURE_SQUARED_PER_FORCE_TIME_PER_AREA:
    :cvar PRESSURE_TIME_PER_VOLUME:
    :cvar PRODUCTIVITY_INDEX:
    :cvar PROPERTY_MULTIPLIER: Unitless multiplier to apply to any
        property
    :cvar QUANTITY: The abstract supertype of all floating point
        properties with a unit of measure.
    :cvar QUANTITY_OF_LIGHT:
    :cvar RADIANCE:
    :cvar RADIANT_INTENSITY:
    :cvar RELATIVE_PERMEABILITY: Ratio of phase permeability, which is a
        function of saturation, to the rock permeability
    :cvar RELATIVE_POWER: A dimensionless quantity where the basis of
        the ratio is power.
    :cvar RELATIVE_TIME: A dimensionless quantity where the basis of the
        ratio is time.
    :cvar RELUCTANCE:
    :cvar RESISTANCE:
    :cvar RESISTIVITY_PER_LENGTH:
    :cvar RESQML_ROOT_PROPERTY: The abstract supertype of all
        properties. This property does not have a parent.
    :cvar ROCK_IMPEDANCE: Acoustic impedence, Ip, Is
    :cvar ROCK_PERMEABILITY: See "permeability rock"
    :cvar ROCK_VOLUME: Rock Volume
    :cvar SATURATION: Ratio of phase fluid volume to pore volume
    :cvar SECOND_MOMENT_OF_AREA:
    :cvar SHEAR_MODULUS: Shear modulus, Mu
    :cvar SOLID_ANGLE:
    :cvar SOLUTION_GAS_OIL_RATIO: Ratio of solution gas volume to oil
        volume at reservoir conditions
    :cvar SPECIFIC_ACTIVITY_OF_RADIOACTIVITY:
    :cvar SPECIFIC_ENERGY:
    :cvar SPECIFIC_HEAT_CAPACITY:
    :cvar SPECIFIC_PRODUCTIVITY_INDEX:
    :cvar SPECIFIC_VOLUME:
    :cvar SURFACE_DENSITY:
    :cvar TEMPERATURE_PER_LENGTH:
    :cvar TEMPERATURE_PER_TIME:
    :cvar THERMAL_CONDUCTANCE:
    :cvar THERMAL_CONDUCTIVITY:
    :cvar THERMAL_DIFFUSIVITY:
    :cvar THERMAL_INSULANCE:
    :cvar THERMAL_RESISTANCE:
    :cvar THERMODYNAMIC_TEMPERATURE:
    :cvar THICKNESS: Distance measured in a volume between two surfaces
        ( e.G. Geological Top Boundary and Geological Bottom Boundary of
        a Geological unit).
    :cvar TIME:
    :cvar TIME_PER_LENGTH:
    :cvar TIME_PER_VOLUME:
    :cvar TRANSMISSIBILITY: Volumetric flux per unit area per unit
        pressure drop for unit viscosity fluid
    :cvar UNIT_PRODUCTIVITY_INDEX:
    :cvar UNITLESS: The abstract supertype of all floating point
        properties with NO unit of measure. In order to allow the unit
        information to be required for all continuous properties, the
        special unit of measure of "NONE" has been assigned to all
        children of this class. In addition, the special dimensional
        class of "0" has been assigned to all children of this class.
    :cvar VAPOR_OIL_GAS_RATIO: Ratio of oil vapor volume to gas volume
        at reservoir conditions
    :cvar VELOCITY:
    :cvar VOLUME:
    :cvar VOLUME_FLOW_RATE:
    :cvar VOLUME_LENGTH_PER_TIME:
    :cvar VOLUME_PER_AREA:
    :cvar VOLUME_PER_LENGTH:
    :cvar VOLUME_PER_TIME_PER_AREA:
    :cvar VOLUME_PER_TIME_PER_LENGTH:
    :cvar VOLUME_PER_TIME_PER_TIME:
    :cvar VOLUME_PER_TIME_PER_VOLUME:
    :cvar VOLUME_PER_VOLUME: A dimensionless quantity where the basis of
        the ratio is volume.
    :cvar VOLUMETRIC_HEAT_TRANSFER_COEFFICIENT:
    :cvar VOLUMETRIC_THERMAL_EXPANSION:
    :cvar WORK:
    :cvar YOUNG_MODULUS: Young's modulus, E
    """
    ABSORBED_DOSE = "absorbed dose"
    ACCELERATION_LINEAR = "acceleration linear"
    ACTIVITY_OF_RADIOACTIVITY = "activity (of radioactivity)"
    AMOUNT_OF_SUBSTANCE = "amount of substance"
    AMPLITUDE = "amplitude"
    ANGLE_PER_LENGTH = "angle per length"
    ANGLE_PER_TIME = "angle per time"
    ANGLE_PER_VOLUME = "angle per volume"
    ANGULAR_ACCELERATION = "angular acceleration"
    AREA = "area"
    AREA_PER_AREA = "area per area"
    AREA_PER_VOLUME = "area per volume"
    ATTENUATION = "attenuation"
    ATTENUATION_PER_LENGTH = "attenuation per length"
    AZIMUTH = "azimuth"
    BUBBLE_POINT_PRESSURE = "bubble point pressure"
    BULK_MODULUS = "bulk modulus"
    CAPACITANCE = "capacitance"
    CATEGORICAL = "categorical"
    CELL_LENGTH = "cell length"
    CHARGE_DENSITY = "charge density"
    CHEMICAL_POTENTIAL = "chemical potential"
    CODE = "code"
    COMPRESSIBILITY = "compressibility"
    CONCENTRATION_OF_B = "concentration of B"
    CONDUCTIVITY = "conductivity"
    CONTINUOUS = "continuous"
    CROSS_SECTION_ABSORPTION = "cross section absorption"
    CURRENT_DENSITY = "current density"
    DARCY_FLOW_COEFFICIENT = "Darcy flow coefficient"
    DATA_TRANSMISSION_SPEED = "data transmission speed"
    DELTA_TEMPERATURE = "delta temperature"
    DENSITY = "density"
    DEPTH = "depth"
    DIFFUSION_COEFFICIENT = "diffusion coefficient"
    DIGITAL_STORAGE = "digital storage"
    DIMENSIONLESS = "dimensionless"
    DIP = "dip"
    DISCRETE = "discrete"
    DOSE_EQUIVALENT = "dose equivalent"
    DOSE_EQUIVALENT_RATE = "dose equivalent rate"
    DYNAMIC_VISCOSITY = "dynamic viscosity"
    ELECTRIC_CHARGE = "electric charge"
    ELECTRIC_CONDUCTANCE = "electric conductance"
    ELECTRIC_CURRENT = "electric current"
    ELECTRIC_DIPOLE_MOMENT = "electric dipole moment"
    ELECTRIC_FIELD_STRENGTH = "electric field strength"
    ELECTRIC_POLARIZATION = "electric polarization"
    ELECTRIC_POTENTIAL = "electric potential"
    ELECTRICAL_RESISTIVITY = "electrical resistivity"
    ELECTROCHEMICAL_EQUIVALENT = "electrochemical equivalent"
    ELECTROMAGNETIC_MOMENT = "electromagnetic moment"
    ENERGY_LENGTH_PER_AREA = "energy length per area"
    ENERGY_LENGTH_PER_TIME_AREA_TEMPERATURE = "energy length per time area temperature"
    ENERGY_PER_AREA = "energy per area"
    ENERGY_PER_LENGTH = "energy per length"
    EQUIVALENT_PER_MASS = "equivalent per mass"
    EQUIVALENT_PER_VOLUME = "equivalent per volume"
    EXPOSURE_RADIOACTIVITY = "exposure (radioactivity)"
    FLUID_VOLUME = "fluid volume"
    FORCE = "force"
    FORCE_AREA = "force area"
    FORCE_LENGTH_PER_LENGTH = "force length per length"
    FORCE_PER_FORCE = "force per force"
    FORCE_PER_LENGTH = "force per length"
    FORCE_PER_VOLUME = "force per volume"
    FORMATION_VOLUME_FACTOR = "formation volume factor"
    FREQUENCY = "frequency"
    FREQUENCY_INTERVAL = "frequency interval"
    GAMMA_RAY_API_UNIT = "gamma ray API unit"
    HEAT_CAPACITY = "heat capacity"
    HEAT_FLOW_RATE = "heat flow rate"
    HEAT_TRANSFER_COEFFICIENT = "heat transfer coefficient"
    ILLUMINANCE = "illuminance"
    INDEX = "index"
    IRRADIANCE = "irradiance"
    ISOTHERMAL_COMPRESSIBILITY = "isothermal compressibility"
    KINEMATIC_VISCOSITY = "kinematic viscosity"
    LAMBDA_RHO = "Lambda Rho"
    LAME_CONSTANT = "Lame constant"
    LENGTH = "length"
    LENGTH_PER_LENGTH = "length per length"
    LENGTH_PER_TEMPERATURE = "length per temperature"
    LENGTH_PER_VOLUME = "length per volume"
    LEVEL_OF_POWER_INTENSITY = "level of power intensity"
    LIGHT_EXPOSURE = "light exposure"
    LINEAR_THERMAL_EXPANSION = "linear thermal expansion"
    LUMINANCE = "luminance"
    LUMINOUS_EFFICACY = "luminous efficacy"
    LUMINOUS_FLUX = "luminous flux"
    LUMINOUS_INTENSITY = "luminous intensity"
    MAGNETIC_DIPOLE_MOMENT = "magnetic dipole moment"
    MAGNETIC_FIELD_STRENGTH = "magnetic field strength"
    MAGNETIC_FLUX = "magnetic flux"
    MAGNETIC_INDUCTION = "magnetic induction"
    MAGNETIC_PERMEABILITY = "magnetic permeability"
    MAGNETIC_VECTOR_POTENTIAL = "magnetic vector potential"
    MASS = "mass"
    MASS_ATTENUATION_COEFFICIENT = "mass attenuation coefficient"
    MASS_CONCENTRATION = "mass concentration"
    MASS_FLOW_RATE = "mass flow rate"
    MASS_LENGTH = "mass length"
    MASS_PER_ENERGY = "mass per energy"
    MASS_PER_LENGTH = "mass per length"
    MASS_PER_TIME_PER_AREA = "mass per time per area"
    MASS_PER_TIME_PER_LENGTH = "mass per time per length"
    MASS_PER_VOLUME_PER_LENGTH = "mass per volume per length"
    MOBILITY = "mobility"
    MODULUS_OF_COMPRESSION = "modulus of compression"
    MOLAR_CONCENTRATION = "molar concentration"
    MOLAR_HEAT_CAPACITY = "molar heat capacity"
    MOLAR_VOLUME = "molar volume"
    MOLE_PER_AREA = "mole per area"
    MOLE_PER_TIME = "mole per time"
    MOLE_PER_TIME_PER_AREA = "mole per time per area"
    MOMENT_OF_FORCE = "moment of force"
    MOMENT_OF_INERTIA = "moment of inertia"
    MOMENT_OF_SECTION = "moment of section"
    MOMENTUM = "momentum"
    MU_RHO = "Mu Rho"
    NET_TO_GROSS_RATIO = "net to gross ratio"
    NEUTRON_API_UNIT = "neutron API unit"
    NON_DARCY_FLOW_COEFFICIENT = "nonDarcy flow coefficient"
    OPERATIONS_PER_TIME = "operations per time"
    PARACHOR = "parachor"
    PER_AREA = "per area"
    PER_ELECTRIC_POTENTIAL = "per electric potential"
    PER_FORCE = "per force"
    PER_LENGTH = "per length"
    PER_MASS = "per mass"
    PER_VOLUME = "per volume"
    PERMEABILITY_LENGTH = "permeability length"
    PERMEABILITY_ROCK = "permeability rock"
    PERMEABILITY_THICKNESS = "permeability thickness"
    PERMEANCE = "permeance"
    PERMITTIVITY = "permittivity"
    P_H = "pH"
    PLANE_ANGLE = "plane angle"
    POISSON_RATIO = "Poisson ratio"
    PORE_VOLUME = "pore volume"
    POROSITY = "porosity"
    POTENTIAL_DIFFERENCE_PER_POWER_DROP = "potential difference per power drop"
    POWER = "power"
    POWER_PER_VOLUME = "power per volume"
    PRESSURE = "pressure"
    PRESSURE_PER_TIME = "pressure per time"
    PRESSURE_SQUARED = "pressure squared"
    PRESSURE_SQUARED_PER_FORCE_TIME_PER_AREA = "pressure squared per force time per area"
    PRESSURE_TIME_PER_VOLUME = "pressure time per volume"
    PRODUCTIVITY_INDEX = "productivity index"
    PROPERTY_MULTIPLIER = "property multiplier"
    QUANTITY = "quantity"
    QUANTITY_OF_LIGHT = "quantity of light"
    RADIANCE = "radiance"
    RADIANT_INTENSITY = "radiant intensity"
    RELATIVE_PERMEABILITY = "relative permeability"
    RELATIVE_POWER = "relative power"
    RELATIVE_TIME = "relative time"
    RELUCTANCE = "reluctance"
    RESISTANCE = "resistance"
    RESISTIVITY_PER_LENGTH = "resistivity per length"
    RESQML_ROOT_PROPERTY = "RESQML root property"
    ROCK_IMPEDANCE = "Rock Impedance"
    ROCK_PERMEABILITY = "rock permeability"
    ROCK_VOLUME = "rock volume"
    SATURATION = "saturation"
    SECOND_MOMENT_OF_AREA = "second moment of area"
    SHEAR_MODULUS = "shear modulus"
    SOLID_ANGLE = "solid angle"
    SOLUTION_GAS_OIL_RATIO = "solution gas-oil ratio"
    SPECIFIC_ACTIVITY_OF_RADIOACTIVITY = "specific activity (of radioactivity)"
    SPECIFIC_ENERGY = "specific energy"
    SPECIFIC_HEAT_CAPACITY = "specific heat capacity"
    SPECIFIC_PRODUCTIVITY_INDEX = "specific productivity index"
    SPECIFIC_VOLUME = "specific volume"
    SURFACE_DENSITY = "surface density"
    TEMPERATURE_PER_LENGTH = "temperature per length"
    TEMPERATURE_PER_TIME = "temperature per time"
    THERMAL_CONDUCTANCE = "thermal conductance"
    THERMAL_CONDUCTIVITY = "thermal conductivity"
    THERMAL_DIFFUSIVITY = "thermal diffusivity"
    THERMAL_INSULANCE = "thermal insulance"
    THERMAL_RESISTANCE = "thermal resistance"
    THERMODYNAMIC_TEMPERATURE = "thermodynamic temperature"
    THICKNESS = "thickness"
    TIME = "time"
    TIME_PER_LENGTH = "time per length"
    TIME_PER_VOLUME = "time per volume"
    TRANSMISSIBILITY = "transmissibility"
    UNIT_PRODUCTIVITY_INDEX = "unit productivity index"
    UNITLESS = "unitless"
    VAPOR_OIL_GAS_RATIO = "vapor oil-gas ratio"
    VELOCITY = "velocity"
    VOLUME = "volume"
    VOLUME_FLOW_RATE = "volume flow rate"
    VOLUME_LENGTH_PER_TIME = "volume length per time"
    VOLUME_PER_AREA = "volume per area"
    VOLUME_PER_LENGTH = "volume per length"
    VOLUME_PER_TIME_PER_AREA = "volume per time per area"
    VOLUME_PER_TIME_PER_LENGTH = "volume per time per length"
    VOLUME_PER_TIME_PER_TIME = "volume per time per time"
    VOLUME_PER_TIME_PER_VOLUME = "volume per time per volume"
    VOLUME_PER_VOLUME = "volume per volume"
    VOLUMETRIC_HEAT_TRANSFER_COEFFICIENT = "volumetric heat transfer coefficient"
    VOLUMETRIC_THERMAL_EXPANSION = "volumetric thermal expansion"
    WORK = "work"
    YOUNG_MODULUS = "Young modulus"
