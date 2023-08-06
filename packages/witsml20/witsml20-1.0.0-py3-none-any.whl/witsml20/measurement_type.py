from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class MeasurementType(Enum):
    """Specifies the type of sensor in a tubular string.

    The source (except for "CH density porosity", "CH neutron porosity",
    "OH density porosity" and "OH neutron porosity") of the values and
    the descriptions is the POSC V2.2 "well log trace class" standard
    instance values, which are documented as "A classification of well
    log traces based on specification of a range of characteristics.
    Traces may be classed according to the type of physical
    characteristic they are meant to measure."

    :cvar ACCELERATION: Output from an accelerometer on a logging tool.
    :cvar ACOUSTIC_CALIPER: A well log that uses an acoustic device to
        measure hole diameter.
    :cvar ACOUSTIC_CASING_COLLAR_LOCATOR: The signal measured by an
        acoustic device at the location of casing collars and other
        features (e.g., perforations).
    :cvar ACOUSTIC_IMPEDANCE: Seismic velocity multiplied by density.
    :cvar ACOUSTIC_POROSITY: Porosity calculated from an acoustic log.
    :cvar ACOUSTIC_VELOCITY: The velocity of an acoustic wave.
    :cvar ACOUSTIC_WAVE_MATRIX_TRAVEL_TIME: The time it takes for an
        acoustic wave to traverse a fixed distance of a given material
        or matrix. In this case the material or matrix is a specific,
        zero-porosity rock, e.g., sandstone, limestone or dolomite.
    :cvar ACOUSTIC_WAVE_TRAVEL_TIME: The time it takes for an acoustic
        wave to traverse a fixed distance.
    :cvar AMPLITUDE: Any measurement of the maximum departure of a wave
        from an average value.
    :cvar AMPLITUDE_OF_ACOUSTIC_WAVE: The extent of departure of an
        acoustic wave measured from the mean position.
    :cvar AMPLITUDE_OF_E_M_WAVE: The extent of departure of an
        electromagnetic wave measured from the mean position.
    :cvar AMPLITUDE_RATIO: The ratio of two amplitudes.
    :cvar AREA: A particular extent of space or surface.
    :cvar ATTENUATION: The amount of reduction in the amplitude of a
        wave.
    :cvar ATTENUATION_OF_ACOUSTIC_WAVE: The amount of reduction in the
        amplitude of an acoustic wave.
    :cvar ATTENUATION_OF_E_M_WAVE: The amount of reduction in the
        amplitude of an electromagnetic wave.
    :cvar AUXILIARY: A general classification for measurements, which
        are very specialized and not normally accessed by
        petrophysicists.
    :cvar AVERAGE_POROSITY: The pore volume of a rock averaged using
        various well log or core porosity measurements.
    :cvar AZIMUTH: In the horizontal plane, it is the clockwise angle of
        departure from magnetic north (while looking down hole).
    :cvar BARITE_MUD_CORRECTION: A trace that has been corrected for the
        effects of barite in the borehole fluid.
    :cvar BED_THICKNESS_CORRECTION: A trace that has been corrected for
        bed thickness effects.
    :cvar BIT_SIZE: The diameter of the drill bit used to drill the
        hole.
    :cvar BLOCKED: A well log trace that has been edited to reflect
        sharp bed boundaries.  The trace has a square wave appearance.
    :cvar BOREHOLE_ENVIRONMENT_CORRECTION: A trace that has been
        corrected for the effects of the borehole environment, e.g.,
        borehole size.
    :cvar BOREHOLE_FLUID_CORRECTION: A trace that has been corrected for
        the effects of borehole fluid; e.g., a mud cake correction.
    :cvar BOREHOLE_SIZE_CORRECTION: A trace that has been corrected for
        the effects of borehole size.
    :cvar BROMIDE_MUD_CORRECTION: A trace that has been corrected for
        the effects of bromide in the borehole fluid.
    :cvar BULK_COMPRESSIBILITY: The relative compressibility of a
        material.
    :cvar BULK_DENSITY: The measured density of a rock with the pore
        volume filled with fluid.  The pore fluid is generally assumed
        to be water.
    :cvar BULK_VOLUME: A quantity-per-unit volume.
    :cvar BULK_VOLUME_GAS: The quantity of gas present in a unit volume
        of rock.  The product of gas saturation and total porosity.
    :cvar BULK_VOLUME_HYDROCARBON: The quantity of hydrocarbon present
        in a unit volume of rock.  The product of hydrocarbon saturation
        and total porosity.
    :cvar BULK_VOLUME_OIL: The quantity of oil present in a unit volume
        of rock.  The product of oil saturation and total porosity.
    :cvar BULK_VOLUME_WATER: The quantity of formation water present in
        a unit volume of rock.  The product of water saturation and
        total porosity.
    :cvar C_O_RATIO: The ratio of the carbon measurement to the oxygen
        measurement.
    :cvar CALIPER: A well log used to record hole diameter (open or
        cased).
    :cvar CASED_HOLE_CORRECTION: A trace that has been corrected for the
        effects of being recorded in a cased hole, e.g., corrected for
        casing weight and thickness.
    :cvar CASING_COLLAR_LOCATOR: The signal measured by a device at the
        location of casing collars and other features (e.g.,
        perforations).
    :cvar CASING_CORRECTION: A trace that has been corrected for the
        effects of casing; this includes things such as casing weight,
        thickness and diameter.
    :cvar CASING_DIAMETER_CORRECTION: A trace that has been corrected
        for the effects of casing diameter.
    :cvar CASING_INSPECTION: Any of the measurements made for the
        purpose of determining the properties of the well casing.
    :cvar CASING_THICKNESS_CORRECTION: A trace that has been corrected
        for the effects of casing thickness.
    :cvar CASING_WEIGHT_CORRECTION: A trace that has been corrected for
        the effects of casing weight.
    :cvar CEMENT_CORRECTION: A trace that has been corrected for the
        effects of the cement surrounding the casing; this includes
        cement thickness, density and type.
    :cvar CEMENT_DENSITY_CORRECTION: A trace that has been corrected for
        the effects of cement density.
    :cvar CEMENT_EVALUATION: Any of the measurements made to determine
        the presence and quality of the cement bond to casing or to
        formation.
    :cvar CEMENT_THICKNESS_CORRECTION: A trace that  has been corrected
        for the effects of cement thickness.
    :cvar CEMENT_TYPE_CORRECTION: A trace that has been corrected for
        the effects of the type of cement used.
    :cvar CH_DENSITY_POROSITY:
    :cvar CH_DOLOMITE_DENSITY_POROSITY: Porosity calculated from the
        bulk density measurement of a cased hole density log using a
        dolomite matrix density.
    :cvar CH_DOLOMITE_NEUTRON_POROSITY: Porosity calculated from a cased
        hole neutron log using a dolomite matrix.
    :cvar CH_LIMESTONE_DENSITY_POROSITY: Porosity calculated from the
        bulk density measurement of a cased hole density log using a
        limestone matrix density.
    :cvar CH_LIMESTONE_NEUTRON_POROSITY: Porosity calculated from a
        cased-hole neutron log using a limestone matrix.
    :cvar CH_NEUTRON_POROSITY:
    :cvar CH_SANDSTONE_DENSITY_POROSITY: Porosity calculated from the
        bulk density measurement of a cased-hole density log using a
        sandstone matrix density.
    :cvar CH_SANDSTONE_NEUTRON_POROSITY: Porosity calculated from an
        openhole neutron log using a sandstone matrix.
    :cvar COMPRESSIONAL_WAVE_DOLOMITE_POROSITY: Porosity calculated from
        a compressional wave acoustic log using a dolomite matrix.
    :cvar COMPRESSIONAL_WAVE_LIMESTONE_POROSITY: Porosity calculated
        from a compressional wave acoustic log using a limestone matrix
    :cvar COMPRESSIONAL_WAVE_MATRIX_TRAVEL_TIME: The time it takes for a
        compressional acoustic wave to traverse a fixed distance of a
        given material or matrix. In this case the material or matrix is
        a specific, zero porosity rock, e.g. sandstone, limestone or
        dolomite.
    :cvar COMPRESSIONAL_WAVE_SANDSTONE_POROSITY: Porosity calculated
        from a compressional wave acoustic log using a sandstone matrix.
    :cvar COMPRESSIONAL_WAVE_TRAVEL_TIME: The time it takes for a
        compressional acoustic wave to traverse a fixed distance.
    :cvar CONDUCTIVITY: The property of a medium (solid or fluid) that
        allows the medium to conduct a form of energy; e.g., electrical
        conductivity or thermal conductivity.
    :cvar CONDUCTIVITY_FROM_ATTENUATION: Conductivity calculated from
        the attenuation of an electromagnetic wave. Generally recorded
        from a LWD resistivity tool.
    :cvar CONDUCTIVITY_FROM_PHASE_SHIFT: Conductivity calculated from
        the phase shift of an electromagnetic wave. Generally recorded
        from a LWD resistivity tool.
    :cvar CONNATE_WATER_CONDUCTIVITY: The conductivity of the water
        entrapped in the interstices of the rock.
    :cvar CONNATE_WATER_RESISTIVITY: The resistivity of the water
        entrapped in the interstices of the rock.
    :cvar CONVENTIONAL_CORE_POROSITY: Porosity from a measurement made
        on a conventional core.
    :cvar CORE_MATRIX_DENSITY: The density of a rock matrix measured on
        a core sample.
    :cvar CORE_PERMEABILITY: The permeability derived from a core.
    :cvar CORE_POROSITY: Porosity from a core measurement.
    :cvar CORRECTED: A trace that has had corrections applied; e.g.
        environmental corrections.
    :cvar COUNT_RATE: The rate of occurrences; e.g. the far counts from
        a density tool..
    :cvar COUNT_RATE_RATIO: The ratio of two count rates.
    :cvar CROSS_PLOT_POROSITY: The pore volume of a rock calculated from
        cross plotting two or more well log porosity measurements.
    :cvar DECAY_TIME: The time it takes for a population to decay,
        generally expressed as a half life.
    :cvar DEEP_CONDUCTIVITY: The conductivity that represents a
        measurement made several feet into the formation; generally
        considered a measurement of the undisturbed formation.
    :cvar DEEP_INDUCTION_CONDUCTIVITY: The conductivity, measured by an
        induction log, which represents a measurement made several feet
        into the formation; generally considered a measurement of the
        undisturbed formation.
    :cvar DEEP_INDUCTION_RESISTIVITY: The resistivity, measured by an
        induction log, which represents a measurement made several feet
        into the formation; generally considered a measurement of the
        undisturbed formation.
    :cvar DEEP_LATEROLOG_CONDUCTIVITY: The conductivity, measured by a
        laterolog, which represents a measurement made several feet into
        the formation; generally considered a measurement of the
        undisturbed formation.
    :cvar DEEP_LATEROLOG_RESISTIVITY: The resistivity, measured by a
        laterolog, which represents a measurement made several feet into
        the formation; generally considered a measurement of the
        undisturbed formation.
    :cvar DEEP_RESISTIVITY: The resistivity, which represents a
        measurement made several feet into the formation; generally
        considered a measurement of the undisturbed formation.
    :cvar DENSITY: Mass per unit Volume; well logging units are usually
        gm/cc.
    :cvar DENSITY_POROSITY: Porosity calculated using the bulk density
        measurement from a density log.
    :cvar DEPTH: The distance to a point in a wellbore.
    :cvar DEPTH_ADJUSTED: The process of depth correcting a trace by
        depth matching it to a reference trace.
    :cvar DEPTH_DERIVED_FROM_VELOCITY: The depth calculated from
        velocity information.
    :cvar DEVIATION: Departure of a borehole from vertical.  Also, the
        angle measured between the tool axis and vertical.
    :cvar DIELECTRIC: Relative permittivity.
    :cvar DIFFUSION_CORRECTION: A trace that  has been corrected for the
        effects of diffusion.
    :cvar DIP: The angle that a structural surface, e.g. a bedding or
        fault plane, makes with the horizontal, measured perpendicular
        to the strike of the structure.
    :cvar DIPMETER: Any of a number of measurements produced by a tool
        designed to measure formation dip and borehole characteristics
        through direct and indirect measurements.
    :cvar DIPMETER_CONDUCTIVITY: The conductivity, measured by a
        dipmeter, which represents a measurement made approximately one
        to two feet into the formation; generally considered to measure
        the formation where it contains fluids that are comprised
        primarily of mud filtrate.
    :cvar DIPMETER_RESISTIVITY: The resistivity, measured by a dipmeter,
        which represents a measurement made approximately one to two
        feet into the formation; generally considered to measure the
        formation where it contains fluids that are comprised primarily
        of mud filtrate.
    :cvar DOLOMITE_ACOUSTIC_POROSITY: Porosity calculated from an
        acoustic log using a dolomite matrix.
    :cvar DOLOMITE_DENSITY_POROSITY: Porosity calculated from the bulk
        density measurement of a density log using a dolomite matrix
        density.
    :cvar DOLOMITE_NEUTRON_POROSITY: Porosity calculated from a neutron
        log using a dolomite matrix.
    :cvar EDITED: A well log trace which has been corrected or adjusted
        through an editing process.
    :cvar EFFECTIVE_POROSITY: The interconnected pore volume occupied by
        free fluids.
    :cvar ELECTRIC_CURRENT: The flow of electric charge.
    :cvar ELECTRIC_POTENTIAL: The difference in electrical energy
        between two systems.
    :cvar ELECTROMAGNETIC_WAVE_MATRIX_TRAVEL_TIME: The time it takes for
        an electromagnetic wave to traverse a fixed distance of a given
        material or matrix. In this case the material or matrix is a
        specific, zero porosity rock, e.g. sandstone, limestone or
        dolomite.
    :cvar ELECTROMAGNETIC_WAVE_TRAVEL_TIME: The time it takes for an
        electromagnetic wave to traverse a fixed distance.
    :cvar ELEMENT: The elemental composition, generally in weight
        percent, of a formation as calculated from information obtained
        from a geochemical logging pass; e.g., weight percent of Al, Si,
        Ca, Fe, etc.
    :cvar ELEMENTAL_RATIO: The ratio of two different elemental
        measurements; e.g. K/U.
    :cvar ENHANCED: A well log trace that has been filtered to improve
        its value; e.g. inverse filtering for better resolution.
    :cvar FILTERED: A well log trace which has had a filter applied to
        it.
    :cvar FLOWMETER: A logging tool to measure the rate and/or direction
        of fluid flow in a wellbore.
    :cvar FLUID_DENSITY: The quantity per unit volume of fluid.
    :cvar FLUID_VELOCITY: The velocity of a flowing fluid.
    :cvar FLUID_VISCOSITY: The amount of a fluid resistance to flow.
    :cvar FLUSHED_ZONE_CONDUCTIVITY: The conductivity of the zone
        immediately behind the mud cake and which is considered to be
        flushed by mud filtrate, i.e., it is considered to have all
        mobile formation fluids displaced from it.
    :cvar FLUSHED_ZONE_RESISTIVITY: The resistivity of the zone
        immediately behind the mud cake and which is considered to be
        flushed by mud filtrate, i.e., it is considered to have all
        mobile formation fluids displaced from it.
    :cvar FLUSHED_ZONE_SATURATION: The fraction or percentage of pore
        volume of rock occupied by drilling mud or mud filtrate in the
        flushed zone.
    :cvar FORCE: Energy exerted or brought to bear.
    :cvar FORMATION_DENSITY_CORRECTION: A trace that has been corrected
        for formation density effects.
    :cvar FORMATION_PROPERTIES_CORRECTION: A trace that has been
        corrected for formation properties; e.g., salinity.
    :cvar FORMATION_SALINITY_CORRECTION: A trace that has been corrected
        for the salinity effects from the water in the formation.
    :cvar FORMATION_SATURATION_CORRECTION: A trace that has been
        corrected for formation saturation effects.
    :cvar FORMATION_VOLUME_FACTOR_CORRECTION: A trace that has been
        corrected for the effects of the hydrocarbon formation volume
        factor.
    :cvar FORMATION_WATER_DENSITY_CORRECTION: A trace that has been
        corrected for the effects of the density of the formation water.
    :cvar FORMATION_WATER_SATURATION_CORRECTION: A trace that has been
        corrected for water saturation effects.
    :cvar FREE_FLUID_INDEX: The percent of the bulk volume occupied by
        fluids that are free to flow as measured by the nuclear
        magnetism log.
    :cvar FRICTION_EFFECT_CORRECTION: A trace that has been corrected
        for the effects of friction.
    :cvar GAMMA_RAY: The measurement of naturally occurring gamma ray
        radiation being released by radioisotopes in clay or other
        minerals in the formation.
    :cvar GAMMA_RAY_MINUS_URANIUM: The measurement of the naturally
        occurring gamma radiation less the radiation attributed to
        uranium.
    :cvar GAS_SATURATION: The fraction or percentage of pore volume of
        rock occupied by gas.
    :cvar GRADIOMANOMETER: The measurement of the average density of
        fluids in a wellbore.
    :cvar HIGH_FREQUENCY_CONDUCTIVITY: A measurement of the conductivity
        of the formation, by a high frequency electromagnetic tool,
        within the first few cubic inches of the borehole wall.
    :cvar HIGH_FREQUENCY_ELECTROMAGNETIC: High frequency electromagnetic
        measurements, e.g. from a dielectric logging tool.
    :cvar HIGH_FREQUENCY_ELECTROMAGNETIC_POROSITY: Porosity calculated
        using a high frequency electromagnetic measurement as input.
    :cvar HIGH_FREQUENCY_E_M_PHASE_SHIFT: The amount of change in the
        phase of a high frequency electromagnetic wave.
    :cvar HIGH_FREQUENCY_RESISTIVITY: A measurement of the resistivity
        of the formation, by a high frequency electromagnetic tool,
        within the first few cubic inches of the borehole wall.
    :cvar HYDROCARBON_CORRECTION: A trace that has been corrected for
        the effects of hydrocarbons.
    :cvar HYDROCARBON_DENSITY_CORRECTION: A trace that has been
        corrected for the effects of hydrocarbon density.
    :cvar HYDROCARBON_GRAVITY_CORRECTION: A trace that has been
        corrected for the effects of hydrocarbon gravity.
    :cvar HYDROCARBON_SATURATION: The fraction or percentage of pore
        volume of rock occupied by hydrocarbon.
    :cvar HYDROCARBON_VISCOSITY_CORRECTION: A trace that has been
        corrected for the effects of hydrocarbon viscosity.
    :cvar IMAGE: The likeness of an object produced by an electrical
        device.
    :cvar INTERPRETATION_VARIABLE: A variable in a well log
        interpretation equation.
    :cvar IRON_MUD_CORRECTION: A trace that has been corrected for the
        effects of iron in the borehole fluid.
    :cvar JOINED: A well log trace that has had two or more runs spliced
        together to make a single trace.
    :cvar KCL_MUD_CORRECTION: A trace that has been corrected for the
        effects of KCl in the borehole fluid.
    :cvar LENGTH: A measured distance or dimension.
    :cvar LIMESTONE_ACOUSTIC_POROSITY: Porosity calculated from an
        acoustic log using a limestone matrix.
    :cvar LIMESTONE_DENSITY_POROSITY: Porosity calculated from the bulk
        density measurement of a density log using a limestone matrix
        density.
    :cvar LIMESTONE_NEUTRON_POROSITY: Porosity calculated from a neutron
        log using a limestone matrix.
    :cvar LITHOLOGY_CORRECTION: A trace that has been corrected for
        lithology effects.
    :cvar LOG_DERIVED_PERMEABILITY: The permeability derived from a well
        log.
    :cvar LOG_MATRIX_DENSITY: The density of a rock matrix used with, or
        derived from, the bulk density from a well log. The matrix is
        assumed to have zero porosity.
    :cvar MAGNETIC_CASING_COLLAR_LOCATOR: The signal measured by a
        magnetic device at the location of casing collars and other
        features (e.g., perforations).
    :cvar MATRIX_DENSITY: The density of a rock matrix.  In this case,
        the matrix is assumed to have zero porosity.
    :cvar MATRIX_TRAVEL_TIME: The time it takes for an electromagnetic
        or acoustic wave to traverse a fixed distance of a given
        material or matrix. In this case the material or matrix is a
        specific, zero porosity rock, e.g. sandstone, limestone or
        dolomite.
    :cvar MEASURED_DEPTH: The distance measured along the path of a
        wellbore.
    :cvar MECHANICAL_CALIPER: A well log which uses a mechanical device
        to measure hole diameter.
    :cvar MECHANICAL_CASING_COLLAR_LOCATOR: The signal measured by a
        mechanical device at the location of casing collars and other
        features (e.g., perforations).
    :cvar MEDIUM_CONDUCTIVITY: The conductivity which represents a
        measurement made approximately two to three feet into the
        formation; generally considered to measure the formation where
        it contain fluids which are a mixture of mud filtrate, connate
        water and possibly hydrocarbons.
    :cvar MEDIUM_INDUCTION_CONDUCTIVITY: The conductivity, made by an
        induction log, which represents a measurement made approximately
        two to three feet into the formation.
    :cvar MEDIUM_INDUCTION_RESISTIVITY: The resistivity, made by an
        induction log, which represents a measurement made approximately
        two to three feet into the formation.
    :cvar MEDIUM_LATEROLOG_CONDUCTIVITY: The conductivity, measured by a
        laterolog, which represents a measurement made approximately two
        to three feet into the formation.
    :cvar MEDIUM_LATEROLOG_RESISTIVITY: The resistivity, measured by a
        laterolog, which represents a measurement made approximately two
        to three feet into the formation.
    :cvar MEDIUM_RESISTIVITY: The resistivity which represents a
        measurement made approximately two to three feet into the
        formation; generally considered to measure the formation where
        it contain fluids which are a mixture of mud filtrate, connate
        water and possibly hydrocarbons.
    :cvar MICRO_CONDUCTIVITY: A measurement of the conductivity of the
        formation within the first few cubic inches of the borehole
        wall.
    :cvar MICRO_INVERSE_CONDUCTIVITY: A conductivity measurement made by
        a micro log tool which measures within the first few cubic
        inches of the borehole wall.
    :cvar MICRO_INVERSE_RESISTIVITY: A resistivity measurement made by a
        micro log tool which measures within the first few cubic inches
        of the borehole wall.
    :cvar MICRO_LATEROLOG_CONDUCTIVITY: A measurement of the
        conductivity of the formation, by a laterolog, within the first
        few cubic inches of the borehole wall.
    :cvar MICRO_LATEROLOG_RESISTIVITY: A measurement of the resistivity
        of the formation, by a laterolog, within the first few cubic
        inches of the borehole wall.
    :cvar MICRO_NORMAL_CONDUCTIVITY: A conductivity measurement made by
        a micro log tool which measures within the first few cubic
        inches of the borehole wall.
    :cvar MICRO_NORMAL_RESISTIVITY: A resistivity measurement made by a
        micro log tool which measures within the first few cubic inches
        of the borehole wall.
    :cvar MICRO_RESISTIVITY: A measurement of the resistivity of the
        formation within the first few cubic inches of the borehole
        wall.
    :cvar MICRO_SPHERICALLY_FOCUSED_CONDUCTIVITY: A measurement of the
        conductivity of the formation, by a spherically focused tool,
        within the first few cubic inches of the borehole wall.
    :cvar MICRO_SPHERICALLY_FOCUSED_RESISTIVITY: A measurement of the
        resistivity of the formation, by a spherically focused tool,
        within the first few cubic inches of the borehole wall.
    :cvar MINERAL: The mineral composition, generally in weight percent,
        of a formation as calculated from elemental information obtained
        from a geochemical logging pass; e.g., weight percent of
        dolomite, calcite, illite, quartzite, etc.
    :cvar MUD_CAKE_CONDUCTIVITY: The conductivity of the filter cake,
        the residue deposited on the borehole wall as mud loses filtrate
        into porous and permeable rock.
    :cvar MUD_CAKE_CORRECTION: A trace which has been corrected for the
        effects of mud cake; e.g., mud cake thickness and/or density.
    :cvar MUD_CAKE_DENSITY_CORRECTION: A trace which has been corrected
        for the effects of mud cake density.
    :cvar MUD_CAKE_RESISTIVITY: The resistivity of the filter cake, the
        residue deposited on the borehole wall as mud loses filtrate
        into porous and permeable rock.
    :cvar MUD_CAKE_RESISTIVITY_CORRECTION: A trace which has been
        corrected for the effects of mud cake resistivity.
    :cvar MUD_CAKE_THICKNESS_CORRECTION: A trace which has been
        corrected for the effects of mud cake thickness.
    :cvar MUD_COMPOSITION_CORRECTION: A trace which has been corrected
        for the effects of borehole fluid composition; e.g., a
        correction for KCl in the borehole fluid.
    :cvar MUD_CONDUCTIVITY: The conductivity of the continuous phase
        liquid used for the drilling of the well.
    :cvar MUD_FILTRATE_CONDUCTIVITY: The conductivity of the effluent of
        the continuous phase liquid of the drilling mud which permeates
        porous and permeable rock.
    :cvar MUD_FILTRATE_CORRECTION: A trace which has been corrected for
        the effects of mud filtrate.  This includes things such as
        filtrate salinity.
    :cvar MUD_FILTRATE_DENSITY_CORRECTION: A trace which has been
        corrected for the effects of mud filtrate density.
    :cvar MUD_FILTRATE_RESISTIVITY: The resistivity of the effluent of
        the continuous phase liquid of the drilling mud which permeates
        porous and permeable rock.
    :cvar MUD_FILTRATE_RESISTIVITY_CORRECTION: A trace which has been
        corrected for the effects of mud filtrate resistivity.
    :cvar MUD_FILTRATE_SALINITY_CORRECTION: A trace which has been
        corrected for the effects of mud filtrate salinity.
    :cvar MUD_RESISTIVITY: The resistivity of the continuous phase
        liquid used for the drilling of the well.
    :cvar MUD_SALINITY_CORRECTION: A trace which has been corrected for
        the effects of salinity in the borehole fluid.
    :cvar MUD_VISCOSITY_CORRECTION: A trace which has been corrected for
        the effects of the viscosity of the borehole fluid.
    :cvar MUD_WEIGHT_CORRECTION: A trace which has been corrected for
        the effects of weighting the borehole fluid.
    :cvar NEUTRON_DIE_AWAY_TIME: The time it takes for a neutron
        population to die away to half value.
    :cvar NEUTRON_POROSITY: Porosity from a neutron log.
    :cvar NUCLEAR_CALIPER: A well log which uses a nuclear device to
        measure hole diameter.
    :cvar NUCLEAR_MAGNETIC_DECAY_TIME: The decay time of a nuclear
        magnetic signal.
    :cvar NUCLEAR_MAGNETISM_LOG_PERMEABILITY: The permeability derived
        from a nuclear magnetism log.
    :cvar NUCLEAR_MAGNETISM_POROSITY: Porosity calculated using the
        measurements from a nuclear magnetism logging pass.
    :cvar OH_DENSITY_POROSITY:
    :cvar OH_DOLOMITE_DENSITY_POROSITY: Porosity calculated from the
        bulk density measurement of an open hole density log using a
        dolomite matrix density.
    :cvar OH_DOLOMITE_NEUTRON_POROSITY: Porosity calculated from an open
        hole neutron log using a dolomite matrix.
    :cvar OH_LIMESTONE_DENSITY_POROSITY: Porosity calculated from the
        bulk density measurement of an open hole density log using a
        limestone matrix density.
    :cvar OH_LIMESTONE_NEUTRON_POROSITY: Porosity calculated from an
        open hole neutron log using a limestone matrix.
    :cvar OH_NEUTRON_POROSITY:
    :cvar OH_SANDSTONE_DENSITY_POROSITY: Porosity calculated from the
        bulk density measurement of an open hole density log using a
        sandstone matrix density.
    :cvar OH_SANDSTONE_NEUTRON_POROSITY: Porosity calculated from an
        open hole neutron log using a sandstone matrix.
    :cvar OIL_BASED_MUD_CORRECTION: A trace which has been corrected for
        the effects of oil based borehole fluid.
    :cvar OIL_SATURATION: The fraction or percentage of pore volume of
        rock occupied by oil.
    :cvar PERFORATING: The procedure for introducing holes through
        casing into a formation so that formation fluids can enter into
        the casing.
    :cvar PERMEABILITY: The permeability of the surrounding formation.
    :cvar PHASE_SHIFT: A change or variation according to a harmonic law
        from a standard position or instant of starting.
    :cvar PHOTOELECTRIC_ABSORPTION: The effect measured by the density
        log and produced by the process of a photon colliding with an
        atom, and then being completely absorbed and its total energy
        used to eject one of the orbital electrons from those
        surrounding the nucleus.
    :cvar PHOTOELECTRIC_ABSORPTION_CORRECTION: The correction that is to
        be made to the photoelectric absorption curve.
    :cvar PHYSICAL_MEASUREMENT_CORRECTION: A trace which has been
        corrected for various physical measurement effects; e.g.
        spreading loss.
    :cvar PLANE_ANGLE: An angle formed by two intersecting lines.
    :cvar POROSITY: The total pore volume occupied by fluid in a rock.
        Includes isolated nonconnecting pores and volume occupied by
        absorbed, immobile fluid.
    :cvar POROSITY_CORRECTION: A trace which has been corrected for
        porosity effects.
    :cvar POTASSIUM: The measurement of gamma radiation emitted by
        potassium.
    :cvar PRESSURE: The force or thrust exerted upon a surface divided
        by the area of the surface.
    :cvar PRESSURE_CORRECTION: A trace which has been corrected for the
        effects of pressure in the borehole.
    :cvar PROCESSED: A well log trace which has been processed in some
        way; e.g., depth adjusted or environmentally corrected.
    :cvar PULSED_NEUTRON_POROSITY: Porosity calculated from a pulsed
        neutron log.
    :cvar QUALITY: Degree of excellence.
    :cvar RATIO: A relationship between two values usually expressed as
        a fraction.
    :cvar RAW: A well log trace which has not had any processing.  In
        other words, a trace which has not been depth adjusted or
        environmentally corrected.
    :cvar RELATIVE_BEARING: While looking down hole, it is the clockwise
        angle from the upper side of the sonde to the reference pad or
        electrode.
    :cvar RESISTIVITY: The property measuring the resistance to flow of
        an electrical current.
    :cvar RESISTIVITY_FACTOR_CORRECTION: A trace which has been
        corrected for resistivity factor effects.
    :cvar RESISTIVITY_FROM_ATTENUATION: Resistivity calculated from the
        attenuation of an electromagnetic wave. Generally recorded from
        a LWD resistivity tool.
    :cvar RESISTIVITY_FROM_PHASE_SHIFT: Resistivity calculated from the
        phase shift of an electromagnetic wave. Generally recorded from
        a LWD resistivity tool.
    :cvar RESISTIVITY_PHASE_SHIFT: The amount of change in the phase of
        an electrical wave.
    :cvar RESISTIVITY_RATIO: The ratio of two resistivity values.
    :cvar SALINITY: The concentration of ions in solution.
    :cvar SAMPLING: To take a sample of or from something.
    :cvar SANDSTONE_ACOUSTIC_POROSITY: Porosity calculated from an
        acoustic log using a sandstone matrix.
    :cvar SANDSTONE_DENSITY_POROSITY: Porosity calculated from the bulk
        density measurement of a density log using a sandstone matrix
        density.
    :cvar SANDSTONE_NEUTRON_POROSITY: Porosity calculated from a neutron
        log using a sandstone matrix.
    :cvar SATURATION: The fraction or percentage of the pore volume of a
        rock.
    :cvar SHALE_VOLUME: An estimate of the amount of shale present in
        the formation. Frequently calculated from a gamma ray or SP
        curve.
    :cvar SHALLOW_CONDUCTIVITY: The conductivity which represents a
        measurement made approximately one to two feet into the
        formation; generally considered to measure the formation where
        it contains fluids which are comprised primarily of mud
        filtrate.
    :cvar SHALLOW_INDUCTION_CONDUCTIVITY: The conductivity, measured by
        an induction log, which represents a measurement made
        approximately one to two feet into the formation; generally
        considered to measure the formation where it contains fluids
        which are comprised primarily of mud filtrate.
    :cvar SHALLOW_INDUCTION_RESISTIVITY: The resistivity, measured by an
        induction log, which represents a measurement made approximately
        one to two feet into the formation; generally considered to
        measure the formation where it contains fluids which are
        comprised primarily of mud filtrate.
    :cvar SHALLOW_LATEROLOG_CONDUCTIVITY: The conductivity, measured by
        a laterolog, which represents a measurement made approximately
        one to two feet into the formation; generally considered to
        measure the formation where it contains fluids which are
        comprised primarily of mud filtrate.
    :cvar SHALLOW_LATEROLOG_RESISTIVITY: The resistivity, measured by a
        laterolog, which represents a measurement made approximately one
        to two feet into the formation; generally considered to measure
        the formation where it contains fluids which are comprised
        primarily of mud filtrate.
    :cvar SHALLOW_RESISTIVITY: The resistivity which represents a
        measurement made approximately one to two feet into the
        formation; generally considered to measure the formation where
        it contains fluids which are comprised primarily of mud
        filtrate.
    :cvar SHEAR_WAVE_DOLOMITE_POROSITY: Porosity calculated from a shear
        wave acoustic log using a dolomite matrix.
    :cvar SHEAR_WAVE_LIMESTONE_POROSITY: Porosity calculated from a
        shear wave acoustic log using a limestone matrix.
    :cvar SHEAR_WAVE_MATRIX_TRAVEL_TIME: The time it takes for a shear
        acoustic wave to traverse a fixed distance of a given material
        or matrix. In this case the material or matrix is a specific,
        zero porosity rock, e.g. sandstone, limestone or dolomite.
    :cvar SHEAR_WAVE_SANDSTONE_POROSITY: Porosity calculated from a
        shear wave acoustic log using a sandstone matrix.
    :cvar SHEAR_WAVE_TRAVEL_TIME: The time it takes for a shear acoustic
        wave to traverse a fixed distance.
    :cvar SHIFTED: A well log trace which has had its original values
        shifted by some factor; e.g., added or multiplied by a constant.
    :cvar SIDEWALL_CORE_POROSITY: Porosity from a measurement made on a
        sidewall core.
    :cvar SIGMA: The macroscopic capture cross section, i.e. the
        effective cross-sectional area per unit volume for the capture
        of neutrons.
    :cvar SIGMA_FORMATION: The macroscopic capture cross section, i.e.
        the effective cross-sectional area per unit volume, of the
        formation for the capture of neutrons.
    :cvar SIGMA_GAS: The macroscopic capture cross section, i.e. the
        effective cross-sectional area per unit volume, of gas for the
        capture of neutrons.
    :cvar SIGMA_HYDROCARBON: The macroscopic capture cross section, i.e.
        the effective cross-sectional area per unit volume, of
        hydrocarbon for the capture of neutrons.
    :cvar SIGMA_MATRIX: The macroscopic capture cross section, i.e. the
        effective cross-sectional area per unit volume, of the rock
        matrix for the capture of neutrons.
    :cvar SIGMA_OIL: The macroscopic capture cross section, i.e. the
        effective cross-sectional area per unit volume, of oil for the
        capture of neutrons.
    :cvar SIGMA_WATER: The macroscopic capture cross section, i.e. the
        effective cross-sectional area per unit volume, of water for the
        capture of neutrons.
    :cvar SLIPPAGE_VELOCITY_CORRECTION: A trace which has been corrected
        for slippage velocity.
    :cvar SMOOTHED: A well log trace which has been filtered to smooth,
        or average the trace.
    :cvar SPECTRAL_GAMMA_RAY: The measurement of all the naturally
        occurring gamma radiation separated by energy windows.
    :cvar SPHERICALLY_FOCUSED_CONDUCTIVITY: The conductivity, measured
        by a spherically focused log, which represents the resistivity
        approximately one to two feet into the formation.
    :cvar SPHERICALLY_FOCUSED_RESISTIVITY: The resistivity, measured by
        a spherically focused log, which represents the resistivity
        approximately one to two feet into the formation.
    :cvar SPONTANEOUS_POTENTIAL: The difference in potential (DC
        Voltage) between a moveable electrode in the borehole and a
        distant reference electrode usually at the surface.
    :cvar SPREADING_LOSS_CORRECTION: A trace which has been corrected
        for the effects of spreading loss.
    :cvar SYNTHETIC_WELL_LOG_TRACE: A well log trace which has been
        artificially created, as opposed to an actual measurement, from
        associated measurements or information.
    :cvar TEMPERATURE: A temperature measurement.
    :cvar TEMPERATURE_CORRECTION: A trace which has been corrected for
        the effects of the temperature in the borehole.
    :cvar TENSION: The tension on the wireline cable while logging.
    :cvar TH_K_RATIO: The ratio of the Thorium measurement to the
        Potassium measurement.
    :cvar THORIUM: The measurement of gamma radiation emitted by
        thorium.
    :cvar TIME: A measured or measurable period.
    :cvar TOOL_DIAMETER_CORRECTION: A trace which has been corrected for
        the tool diameter.
    :cvar TOOL_ECCENTRICITY_CORRECTION: A trace which has been corrected
        for the effects of the tool not being centered in the borehole.
    :cvar TOTAL_GAMMA_RAY: The measurement of all the naturally
        occurring gamma radiation.
    :cvar TOTAL_POROSITY: The total pore volume occupied by fluid in a
        rock.
    :cvar TRACER_SURVEY: A well log used for the purpose of monitoring a
        traceable material; e.g. a radioactive isotope.
    :cvar TRAVEL_TIME: The time it takes for an acoustic or
        electromagnetic wave to traverse a specific distance.
    :cvar TRUE_CONDUCTIVITY: The conductivity of fluid-filled rock where
        fluid distributions and saturations are representative of those
        in the uninvaded, undisturbed part of the formation.
    :cvar TRUE_RESISTIVITY: The resistivity of fluid-filled rock where
        fluid distributions and saturations are representative of those
        in the uninvaded, undisturbed part of the formation.
    :cvar TRUE_VERTICAL_DEPTH: The distance along a straight, vertical
        path.  Usually computed from a measured depth and deviation
        information.
    :cvar TUBE_WAVE_DOLOMITE_POROSITY: Porosity calculated from a tube
        wave acoustic log using a dolomite matrix.
    :cvar TUBE_WAVE_LIMESTONE_POROSITY: Porosity calculated from a tube
        wave acoustic log using a limestone matrix.
    :cvar TUBE_WAVE_MATRIX_TRAVEL_TIME: The time it takes for a
        acoustic tube wave to traverse a fixed distance of a given
        material or matrix. In this case the material or matrix is a
        specific, zero porosity rock, e.g. sandstone, limestone or
        dolomite.
    :cvar TUBE_WAVE_SANDSTONE_POROSITY: Porosity calculated from a tube
        wave acoustic log using a sandstone matrix.
    :cvar TUBE_WAVE_TRAVEL_TIME: The time it takes for a tube acoustic
        wave to traverse a fixed distance.
    :cvar URANIUM: The measurement of gamma radiation emitted by
        uranium.
    :cvar VELOCITY: directional speed
    :cvar VOLUME: cubic capacity
    :cvar WATER_BASED_FLUID_CORRECTION: A trace which has been corrected
        for the effects of the components in a water based borehole
        fluid system; e.g., a correction for KCL in the mud.
    :cvar WATER_HOLDUP_CORRECTION: A trace which has been corrected for
        water holdup.
    :cvar WATER_SATURATED_CONDUCTIVITY: The conductivity of rock
        completely saturated with connate water.
    :cvar WATER_SATURATED_RESISTIVITY: The resistivity of rock
        completely saturated with connate water.
    :cvar WATER_SATURATION: The fraction or percentage of pore volume of
        rock occupied by water.
    """
    ACCELERATION = "acceleration"
    ACOUSTIC_CALIPER = "acoustic caliper"
    ACOUSTIC_CASING_COLLAR_LOCATOR = "acoustic casing collar locator"
    ACOUSTIC_IMPEDANCE = "acoustic impedance"
    ACOUSTIC_POROSITY = "acoustic porosity"
    ACOUSTIC_VELOCITY = "acoustic velocity"
    ACOUSTIC_WAVE_MATRIX_TRAVEL_TIME = "acoustic wave matrix travel time"
    ACOUSTIC_WAVE_TRAVEL_TIME = "acoustic wave travel time"
    AMPLITUDE = "amplitude"
    AMPLITUDE_OF_ACOUSTIC_WAVE = "amplitude of acoustic wave"
    AMPLITUDE_OF_E_M_WAVE = "amplitude of E-M wave"
    AMPLITUDE_RATIO = "amplitude ratio"
    AREA = "area"
    ATTENUATION = "attenuation"
    ATTENUATION_OF_ACOUSTIC_WAVE = "attenuation of acoustic wave"
    ATTENUATION_OF_E_M_WAVE = "attenuation of E-M wave"
    AUXILIARY = "auxiliary"
    AVERAGE_POROSITY = "average porosity"
    AZIMUTH = "azimuth"
    BARITE_MUD_CORRECTION = "barite mud correction"
    BED_THICKNESS_CORRECTION = "bed thickness correction"
    BIT_SIZE = "bit size"
    BLOCKED = "blocked"
    BOREHOLE_ENVIRONMENT_CORRECTION = "borehole environment correction"
    BOREHOLE_FLUID_CORRECTION = "borehole fluid correction"
    BOREHOLE_SIZE_CORRECTION = "borehole size correction"
    BROMIDE_MUD_CORRECTION = "bromide mud correction"
    BULK_COMPRESSIBILITY = "bulk compressibility"
    BULK_DENSITY = "bulk density"
    BULK_VOLUME = "bulk volume"
    BULK_VOLUME_GAS = "bulk volume gas"
    BULK_VOLUME_HYDROCARBON = "bulk volume hydrocarbon"
    BULK_VOLUME_OIL = "bulk volume oil"
    BULK_VOLUME_WATER = "bulk volume water"
    C_O_RATIO = "C/O ratio"
    CALIPER = "caliper"
    CASED_HOLE_CORRECTION = "cased hole correction"
    CASING_COLLAR_LOCATOR = "casing collar locator"
    CASING_CORRECTION = "casing correction"
    CASING_DIAMETER_CORRECTION = "casing diameter correction"
    CASING_INSPECTION = "casing inspection"
    CASING_THICKNESS_CORRECTION = "casing thickness correction"
    CASING_WEIGHT_CORRECTION = "casing weight correction"
    CEMENT_CORRECTION = "cement correction"
    CEMENT_DENSITY_CORRECTION = "cement density correction"
    CEMENT_EVALUATION = "cement evaluation"
    CEMENT_THICKNESS_CORRECTION = "cement thickness correction"
    CEMENT_TYPE_CORRECTION = "cement type correction"
    CH_DENSITY_POROSITY = "CH density porosity"
    CH_DOLOMITE_DENSITY_POROSITY = "CH dolomite density porosity"
    CH_DOLOMITE_NEUTRON_POROSITY = "CH dolomite neutron porosity"
    CH_LIMESTONE_DENSITY_POROSITY = "CH limestone density porosity"
    CH_LIMESTONE_NEUTRON_POROSITY = "CH limestone neutron porosity"
    CH_NEUTRON_POROSITY = "CH neutron porosity"
    CH_SANDSTONE_DENSITY_POROSITY = "CH sandstone density porosity"
    CH_SANDSTONE_NEUTRON_POROSITY = "CH sandstone neutron porosity"
    COMPRESSIONAL_WAVE_DOLOMITE_POROSITY = "compressional wave dolomite porosity"
    COMPRESSIONAL_WAVE_LIMESTONE_POROSITY = "compressional wave limestone porosity"
    COMPRESSIONAL_WAVE_MATRIX_TRAVEL_TIME = "compressional wave matrix travel time"
    COMPRESSIONAL_WAVE_SANDSTONE_POROSITY = "compressional wave sandstone porosity"
    COMPRESSIONAL_WAVE_TRAVEL_TIME = "compressional wave travel time"
    CONDUCTIVITY = "conductivity"
    CONDUCTIVITY_FROM_ATTENUATION = "conductivity from attenuation"
    CONDUCTIVITY_FROM_PHASE_SHIFT = "conductivity from phase shift"
    CONNATE_WATER_CONDUCTIVITY = "connate water conductivity"
    CONNATE_WATER_RESISTIVITY = "connate water resistivity"
    CONVENTIONAL_CORE_POROSITY = "conventional core porosity"
    CORE_MATRIX_DENSITY = "core matrix density"
    CORE_PERMEABILITY = "core permeability"
    CORE_POROSITY = "core porosity"
    CORRECTED = "corrected"
    COUNT_RATE = "count rate"
    COUNT_RATE_RATIO = "count rate ratio"
    CROSS_PLOT_POROSITY = "cross plot porosity"
    DECAY_TIME = "decay time"
    DEEP_CONDUCTIVITY = "deep conductivity"
    DEEP_INDUCTION_CONDUCTIVITY = "deep induction conductivity"
    DEEP_INDUCTION_RESISTIVITY = "deep induction resistivity"
    DEEP_LATEROLOG_CONDUCTIVITY = "deep laterolog conductivity"
    DEEP_LATEROLOG_RESISTIVITY = "deep laterolog resistivity"
    DEEP_RESISTIVITY = "deep resistivity"
    DENSITY = "density"
    DENSITY_POROSITY = "density porosity"
    DEPTH = "depth"
    DEPTH_ADJUSTED = "depth adjusted"
    DEPTH_DERIVED_FROM_VELOCITY = "depth derived from velocity"
    DEVIATION = "deviation"
    DIELECTRIC = "dielectric"
    DIFFUSION_CORRECTION = "diffusion correction"
    DIP = "dip"
    DIPMETER = "dipmeter"
    DIPMETER_CONDUCTIVITY = "dipmeter conductivity"
    DIPMETER_RESISTIVITY = "dipmeter resistivity"
    DOLOMITE_ACOUSTIC_POROSITY = "dolomite acoustic porosity"
    DOLOMITE_DENSITY_POROSITY = "dolomite density porosity"
    DOLOMITE_NEUTRON_POROSITY = "dolomite neutron porosity"
    EDITED = "edited"
    EFFECTIVE_POROSITY = "effective porosity"
    ELECTRIC_CURRENT = "electric current"
    ELECTRIC_POTENTIAL = "electric potential"
    ELECTROMAGNETIC_WAVE_MATRIX_TRAVEL_TIME = "electromagnetic wave matrix travel time"
    ELECTROMAGNETIC_WAVE_TRAVEL_TIME = "electromagnetic wave travel time"
    ELEMENT = "element"
    ELEMENTAL_RATIO = "elemental ratio"
    ENHANCED = "enhanced"
    FILTERED = "filtered"
    FLOWMETER = "flowmeter"
    FLUID_DENSITY = "fluid density"
    FLUID_VELOCITY = "fluid velocity"
    FLUID_VISCOSITY = "fluid viscosity"
    FLUSHED_ZONE_CONDUCTIVITY = "flushed zone conductivity"
    FLUSHED_ZONE_RESISTIVITY = "flushed zone resistivity"
    FLUSHED_ZONE_SATURATION = "flushed zone saturation"
    FORCE = "force"
    FORMATION_DENSITY_CORRECTION = "formation density correction"
    FORMATION_PROPERTIES_CORRECTION = "formation properties correction"
    FORMATION_SALINITY_CORRECTION = "formation salinity correction"
    FORMATION_SATURATION_CORRECTION = "formation saturation correction"
    FORMATION_VOLUME_FACTOR_CORRECTION = "formation volume factor correction"
    FORMATION_WATER_DENSITY_CORRECTION = "formation water density correction"
    FORMATION_WATER_SATURATION_CORRECTION = "formation water saturation correction"
    FREE_FLUID_INDEX = "free fluid index"
    FRICTION_EFFECT_CORRECTION = "friction effect correction"
    GAMMA_RAY = "gamma ray"
    GAMMA_RAY_MINUS_URANIUM = "gamma ray minus uranium"
    GAS_SATURATION = "gas saturation"
    GRADIOMANOMETER = "gradiomanometer"
    HIGH_FREQUENCY_CONDUCTIVITY = "high frequency conductivity"
    HIGH_FREQUENCY_ELECTROMAGNETIC = "high frequency electromagnetic"
    HIGH_FREQUENCY_ELECTROMAGNETIC_POROSITY = "high frequency electromagnetic porosity"
    HIGH_FREQUENCY_E_M_PHASE_SHIFT = "high frequency E-M phase shift"
    HIGH_FREQUENCY_RESISTIVITY = "high frequency resistivity"
    HYDROCARBON_CORRECTION = "hydrocarbon correction"
    HYDROCARBON_DENSITY_CORRECTION = "hydrocarbon density correction"
    HYDROCARBON_GRAVITY_CORRECTION = "hydrocarbon gravity correction"
    HYDROCARBON_SATURATION = "hydrocarbon saturation"
    HYDROCARBON_VISCOSITY_CORRECTION = "hydrocarbon viscosity correction"
    IMAGE = "image"
    INTERPRETATION_VARIABLE = "interpretation variable"
    IRON_MUD_CORRECTION = "iron mud correction"
    JOINED = "joined"
    KCL_MUD_CORRECTION = "KCl mud correction"
    LENGTH = "length"
    LIMESTONE_ACOUSTIC_POROSITY = "limestone acoustic porosity"
    LIMESTONE_DENSITY_POROSITY = "limestone density porosity"
    LIMESTONE_NEUTRON_POROSITY = "limestone neutron porosity"
    LITHOLOGY_CORRECTION = "lithology correction"
    LOG_DERIVED_PERMEABILITY = "log derived permeability"
    LOG_MATRIX_DENSITY = "log matrix density"
    MAGNETIC_CASING_COLLAR_LOCATOR = "magnetic casing collar locator"
    MATRIX_DENSITY = "matrix density"
    MATRIX_TRAVEL_TIME = "matrix travel time"
    MEASURED_DEPTH = "measured depth"
    MECHANICAL_CALIPER = "mechanical caliper"
    MECHANICAL_CASING_COLLAR_LOCATOR = "mechanical casing collar locator"
    MEDIUM_CONDUCTIVITY = "medium conductivity"
    MEDIUM_INDUCTION_CONDUCTIVITY = "medium induction conductivity"
    MEDIUM_INDUCTION_RESISTIVITY = "medium induction resistivity"
    MEDIUM_LATEROLOG_CONDUCTIVITY = "medium laterolog conductivity"
    MEDIUM_LATEROLOG_RESISTIVITY = "medium laterolog resistivity"
    MEDIUM_RESISTIVITY = "medium resistivity"
    MICRO_CONDUCTIVITY = "micro conductivity"
    MICRO_INVERSE_CONDUCTIVITY = "micro inverse conductivity"
    MICRO_INVERSE_RESISTIVITY = "micro inverse resistivity"
    MICRO_LATEROLOG_CONDUCTIVITY = "micro laterolog conductivity"
    MICRO_LATEROLOG_RESISTIVITY = "micro laterolog resistivity"
    MICRO_NORMAL_CONDUCTIVITY = "micro normal conductivity"
    MICRO_NORMAL_RESISTIVITY = "micro normal resistivity"
    MICRO_RESISTIVITY = "micro resistivity"
    MICRO_SPHERICALLY_FOCUSED_CONDUCTIVITY = "micro spherically focused conductivity"
    MICRO_SPHERICALLY_FOCUSED_RESISTIVITY = "micro spherically focused resistivity"
    MINERAL = "mineral"
    MUD_CAKE_CONDUCTIVITY = "mud cake conductivity"
    MUD_CAKE_CORRECTION = "mud cake correction"
    MUD_CAKE_DENSITY_CORRECTION = "mud cake density correction"
    MUD_CAKE_RESISTIVITY = "mud cake resistivity"
    MUD_CAKE_RESISTIVITY_CORRECTION = "mud cake resistivity correction"
    MUD_CAKE_THICKNESS_CORRECTION = "mud cake thickness correction"
    MUD_COMPOSITION_CORRECTION = "mud composition correction"
    MUD_CONDUCTIVITY = "mud conductivity"
    MUD_FILTRATE_CONDUCTIVITY = "mud filtrate conductivity"
    MUD_FILTRATE_CORRECTION = "mud filtrate correction"
    MUD_FILTRATE_DENSITY_CORRECTION = "mud filtrate density correction"
    MUD_FILTRATE_RESISTIVITY = "mud filtrate resistivity"
    MUD_FILTRATE_RESISTIVITY_CORRECTION = "mud filtrate resistivity correction"
    MUD_FILTRATE_SALINITY_CORRECTION = "mud filtrate salinity correction"
    MUD_RESISTIVITY = "mud resistivity"
    MUD_SALINITY_CORRECTION = "mud salinity correction"
    MUD_VISCOSITY_CORRECTION = "mud viscosity correction"
    MUD_WEIGHT_CORRECTION = "mud weight correction"
    NEUTRON_DIE_AWAY_TIME = "neutron die away time"
    NEUTRON_POROSITY = "neutron porosity"
    NUCLEAR_CALIPER = "nuclear caliper"
    NUCLEAR_MAGNETIC_DECAY_TIME = "nuclear magnetic decay time"
    NUCLEAR_MAGNETISM_LOG_PERMEABILITY = "nuclear magnetism log permeability"
    NUCLEAR_MAGNETISM_POROSITY = "nuclear magnetism porosity"
    OH_DENSITY_POROSITY = "OH density porosity"
    OH_DOLOMITE_DENSITY_POROSITY = "OH dolomite density porosity"
    OH_DOLOMITE_NEUTRON_POROSITY = "OH dolomite neutron porosity"
    OH_LIMESTONE_DENSITY_POROSITY = "OH limestone density porosity"
    OH_LIMESTONE_NEUTRON_POROSITY = "OH limestone neutron porosity"
    OH_NEUTRON_POROSITY = "OH neutron porosity"
    OH_SANDSTONE_DENSITY_POROSITY = "OH sandstone density porosity"
    OH_SANDSTONE_NEUTRON_POROSITY = "OH sandstone neutron porosity"
    OIL_BASED_MUD_CORRECTION = "oil based mud correction"
    OIL_SATURATION = "oil saturation"
    PERFORATING = "perforating"
    PERMEABILITY = "permeability"
    PHASE_SHIFT = "phase shift"
    PHOTOELECTRIC_ABSORPTION = "photoelectric absorption"
    PHOTOELECTRIC_ABSORPTION_CORRECTION = "photoelectric absorption correction"
    PHYSICAL_MEASUREMENT_CORRECTION = "physical measurement correction"
    PLANE_ANGLE = "plane angle"
    POROSITY = "porosity"
    POROSITY_CORRECTION = "porosity correction"
    POTASSIUM = "potassium"
    PRESSURE = "pressure"
    PRESSURE_CORRECTION = "pressure correction"
    PROCESSED = "processed"
    PULSED_NEUTRON_POROSITY = "pulsed neutron porosity"
    QUALITY = "quality"
    RATIO = "ratio"
    RAW = "raw"
    RELATIVE_BEARING = "relative bearing"
    RESISTIVITY = "resistivity"
    RESISTIVITY_FACTOR_CORRECTION = "resistivity factor correction"
    RESISTIVITY_FROM_ATTENUATION = "resistivity from attenuation"
    RESISTIVITY_FROM_PHASE_SHIFT = "resistivity from phase shift"
    RESISTIVITY_PHASE_SHIFT = "resistivity phase shift"
    RESISTIVITY_RATIO = "resistivity ratio"
    SALINITY = "salinity"
    SAMPLING = "sampling"
    SANDSTONE_ACOUSTIC_POROSITY = "sandstone acoustic porosity"
    SANDSTONE_DENSITY_POROSITY = "sandstone density porosity"
    SANDSTONE_NEUTRON_POROSITY = "sandstone neutron porosity"
    SATURATION = "saturation"
    SHALE_VOLUME = "shale volume"
    SHALLOW_CONDUCTIVITY = "shallow conductivity"
    SHALLOW_INDUCTION_CONDUCTIVITY = "shallow induction conductivity"
    SHALLOW_INDUCTION_RESISTIVITY = "shallow induction resistivity"
    SHALLOW_LATEROLOG_CONDUCTIVITY = "shallow laterolog conductivity"
    SHALLOW_LATEROLOG_RESISTIVITY = "shallow laterolog resistivity"
    SHALLOW_RESISTIVITY = "shallow resistivity"
    SHEAR_WAVE_DOLOMITE_POROSITY = "shear wave dolomite porosity"
    SHEAR_WAVE_LIMESTONE_POROSITY = "shear wave limestone porosity"
    SHEAR_WAVE_MATRIX_TRAVEL_TIME = "shear wave matrix travel time"
    SHEAR_WAVE_SANDSTONE_POROSITY = "shear wave sandstone porosity"
    SHEAR_WAVE_TRAVEL_TIME = "shear wave travel time"
    SHIFTED = "shifted"
    SIDEWALL_CORE_POROSITY = "sidewall core porosity"
    SIGMA = "sigma"
    SIGMA_FORMATION = "sigma formation"
    SIGMA_GAS = "sigma gas"
    SIGMA_HYDROCARBON = "sigma hydrocarbon"
    SIGMA_MATRIX = "sigma matrix"
    SIGMA_OIL = "sigma oil"
    SIGMA_WATER = "sigma water"
    SLIPPAGE_VELOCITY_CORRECTION = "slippage velocity correction"
    SMOOTHED = "smoothed"
    SPECTRAL_GAMMA_RAY = "spectral gamma ray"
    SPHERICALLY_FOCUSED_CONDUCTIVITY = "spherically focused conductivity"
    SPHERICALLY_FOCUSED_RESISTIVITY = "spherically focused resistivity"
    SPONTANEOUS_POTENTIAL = "spontaneous potential"
    SPREADING_LOSS_CORRECTION = "spreading loss correction"
    SYNTHETIC_WELL_LOG_TRACE = "synthetic well log trace"
    TEMPERATURE = "temperature"
    TEMPERATURE_CORRECTION = "temperature correction"
    TENSION = "tension"
    TH_K_RATIO = "Th/K ratio"
    THORIUM = "thorium"
    TIME = "time"
    TOOL_DIAMETER_CORRECTION = "tool diameter correction"
    TOOL_ECCENTRICITY_CORRECTION = "tool eccentricity correction"
    TOTAL_GAMMA_RAY = "total gamma ray"
    TOTAL_POROSITY = "total porosity"
    TRACER_SURVEY = "tracer survey"
    TRAVEL_TIME = "travel time"
    TRUE_CONDUCTIVITY = "true conductivity"
    TRUE_RESISTIVITY = "true resistivity"
    TRUE_VERTICAL_DEPTH = "true vertical depth"
    TUBE_WAVE_DOLOMITE_POROSITY = "tube wave dolomite porosity"
    TUBE_WAVE_LIMESTONE_POROSITY = "tube wave limestone porosity"
    TUBE_WAVE_MATRIX_TRAVEL_TIME = "tube wave matrix travel time"
    TUBE_WAVE_SANDSTONE_POROSITY = "tube wave sandstone porosity"
    TUBE_WAVE_TRAVEL_TIME = "tube wave travel time"
    URANIUM = "uranium"
    VELOCITY = "velocity"
    VOLUME = "volume"
    WATER_BASED_FLUID_CORRECTION = "water based fluid correction"
    WATER_HOLDUP_CORRECTION = "water holdup correction"
    WATER_SATURATED_CONDUCTIVITY = "water saturated conductivity"
    WATER_SATURATED_RESISTIVITY = "water saturated resistivity"
    WATER_SATURATION = "water saturation"
