from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class WellPurpose(Enum):
    """
    Specifies values that represent the classification of a well or wellbore by
    the purpose for which it was initially drilled.

    :cvar APPRAISAL: A well drilled into a formation shown to be
        potentially productive of oil or gas by an earlier well for the
        purpose of obtaining more information about the reservoir. Also
        known as a delineation well.
    :cvar APPRAISAL_CONFIRMATION_APPRAISAL: An appraisal well, generally
        drilled in a location interpreted to be in the reservoir, whose
        purpose is to confirm the interpretation.
    :cvar APPRAISAL_EXPLORATORY_APPRAISAL: An appraisal well, generally
        drilled in an area unknown to be part of the reservoir, whose
        purpose is to determine the extent of the reservoir.
    :cvar EXPLORATION: An exploratory well drilled in an unproved area
        to test for a new field, a new pay, a deeper reservoir, or a
        shallower reservoir. Also known as a wildcat.
    :cvar EXPLORATION_DEEPER_POOL_WILDCAT: An exploratory well drilled
        to search for additional pools of hydrocarbon near known pools
        of hydrocarbon but at deeper stratigraphic levels than known
        pools.
    :cvar EXPLORATION_NEW_FIELD_WILDCAT: An exploratory well drilled to
        search for an occurrence of hydrocarbon at a relatively
        considerable distance outside the limits of known pools of
        hydrocarbon, as those limits were understood at the time.
    :cvar EXPLORATION_NEW_POOL_WILDCAT: An exploratory well drilled to
        search for additional pools of hydrocarbon near and at the same
        stratigraphic level as known pools.
    :cvar EXPLORATION_OUTPOST_WILDCAT: An exploratory well drilled to
        search for additional pools of hydrocarbon or to extend the
        limits of a known pool by searching in the same interval at some
        distance from a known pool.
    :cvar EXPLORATION_SHALLOWER_POOL_WILDCAT: An exploratory well
        drilled to search for additional pools of hydrocarbon near but
        at a shallower stratigraphic levels than known pools.
    :cvar DEVELOPMENT: A well drilled in a zone in an area already
        proved productive.
    :cvar DEVELOPMENT_INFILL_DEVELOPMENT: A development well drilled to
        fill in between established wells, usually as part of a drilling
        program to reduce the spacing between wells to increase
        production.
    :cvar DEVELOPMENT_INJECTOR: A development well drilled with the
        intent of injecting fluids into the reservoir for the purpose of
        improving reservoir production.
    :cvar DEVELOPMENT_PRODUCER: A development well drilled with the
        intent of producing fluids.
    :cvar FLUID_STORAGE: A well drilled for storing fluids - generally
        either hydrocarbons or waste disposal.
    :cvar FLUID_STORAGE_GAS_STORAGE: A well drilled with the intent of
        injecting gas into the reservoir rock as a storage facility.
    :cvar GENERAL_SRVC: A well drilled with the intent of providing a
        general service as opposed to producing or injecting fluids.
        Examples of such services are geologic tests, pressure relief
        (for blowouts), and monitoring and observation.
    :cvar GENERAL_SRVC_BOREHOLE_RE_ACQUISITION: A service well drilled
        to intersect another well below the surface for the purpose of
        extending the life of a well whose surface borehole has been
        lost or damaged.
    :cvar GENERAL_SRVC_OBSERVATION: A service well drilled for the
        purpose of monitoring fluids in a reservoir, or observing some
        other subsurface phenomena. Also called a monitor well.
    :cvar GENERAL_SRVC_RELIEF: A service well drilled with the specific
        purpose to provide communication at some point below the surface
        to another well that is out of control.
    :cvar GENERAL_SRVC_RESEARCH: A well drilled with the purpose of
        obtaining information on the stratigraphy, on drilling
        practices, for logging tests, or other such purpose. It is not
        expected to find economic reserves of hydrocarbons.
    :cvar GENERAL_SRVC_RESEARCH_DRILL_TEST: A research well drilled to
        test the suitablity of a particular type of equipment or
        drilling practice.
    :cvar GENERAL_SRVC_RESEARCH_STRAT_TEST: A research well drilled for
        the purpose of gathering geologic information on the
        stratigraphy of an area. A C.O.S.T. well would be included in
        this category.
    :cvar GENERAL_SRVC_WASTE_DISPOSAL: A service well drilled for the
        purpose of injection of sewage, industrial waste, or other waste
        fluids into the subsurface for disposal.
    :cvar MINERAL: A non-oil and gas well drilled for the purpose of
        locating and/or extracting a mineral from the subsurface,
        usually through the injection and/or extraction of mineral-
        bearing fluids.
    """
    APPRAISAL = "appraisal"
    APPRAISAL_CONFIRMATION_APPRAISAL = "appraisal -- confirmation appraisal"
    APPRAISAL_EXPLORATORY_APPRAISAL = "appraisal -- exploratory appraisal"
    EXPLORATION = "exploration"
    EXPLORATION_DEEPER_POOL_WILDCAT = "exploration -- deeper-pool wildcat"
    EXPLORATION_NEW_FIELD_WILDCAT = "exploration -- new-field wildcat"
    EXPLORATION_NEW_POOL_WILDCAT = "exploration -- new-pool wildcat"
    EXPLORATION_OUTPOST_WILDCAT = "exploration -- outpost wildcat"
    EXPLORATION_SHALLOWER_POOL_WILDCAT = "exploration -- shallower-pool wildcat"
    DEVELOPMENT = "development"
    DEVELOPMENT_INFILL_DEVELOPMENT = "development -- infill development"
    DEVELOPMENT_INJECTOR = "development -- injector"
    DEVELOPMENT_PRODUCER = "development -- producer"
    FLUID_STORAGE = "fluid storage"
    FLUID_STORAGE_GAS_STORAGE = "fluid storage -- gas storage"
    GENERAL_SRVC = "general srvc"
    GENERAL_SRVC_BOREHOLE_RE_ACQUISITION = "general srvc -- borehole re-acquisition"
    GENERAL_SRVC_OBSERVATION = "general srvc -- observation"
    GENERAL_SRVC_RELIEF = "general srvc -- relief"
    GENERAL_SRVC_RESEARCH = "general srvc -- research"
    GENERAL_SRVC_RESEARCH_DRILL_TEST = "general srvc -- research -- drill test"
    GENERAL_SRVC_RESEARCH_STRAT_TEST = "general srvc -- research -- strat test"
    GENERAL_SRVC_WASTE_DISPOSAL = "general srvc -- waste disposal"
    MINERAL = "mineral"
