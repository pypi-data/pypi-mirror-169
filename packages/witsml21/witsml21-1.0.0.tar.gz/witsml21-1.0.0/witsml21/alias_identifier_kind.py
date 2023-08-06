from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class AliasIdentifierKind(Enum):
    """
    :cvar ABBREVIATION: A shortened form of a word or phrase.
    :cvar ACRONYM: An abbreviation formed from the initial letters of
        the full name and often pronounced as a word.
    :cvar COMMON_NAME: A common name by which a person, company, or
        other entity is known.
    :cvar INDUSTRY_CODE: Short identifier from industry standard
        register.
    :cvar INDUSTRY_NAME: Name from industry standard register.
    :cvar LEASE_IDENTIFIER: A name usually associated with the lease or
        block, the leaseholder, or other entity associated with the
        lease.
    :cvar LOCAL_LANGUAGE_NAME: An alias name in local language.
    :cvar PREFERRED_NAME: Preferred name assigned by the firm.
    :cvar PROJECT_NUMBER: This is the number by which a project is
        known.
    :cvar REGULATORY_IDENTIFIER: The identifier assigned and used by the
        regulatory agency that permitted the facility (e.g. well,
        wellbore, completion).
    :cvar REGULATORY_NAME: The name assigned and used by the regulatory
        agency that permitted the facility (e.g. well).
    :cvar SHORT_NAME: A short name or abbreviated name.
    :cvar SUBSCRIPTION_WELL_NAME: Well name supplied by subscription
        organisation.
    :cvar UNIQUE_IDENTIFIER: Unique company identifier tagged to an
        object throughout its lifecycle (e.g. well, wellbore).
    :cvar WELLBORE_NUMBER: A wellbore identifier in context of a
        regulatory agency, e.g. NPD, OGA.
    """
    ABBREVIATION = "abbreviation"
    ACRONYM = "acronym"
    COMMON_NAME = "common name"
    INDUSTRY_CODE = "industry code"
    INDUSTRY_NAME = "industry name"
    LEASE_IDENTIFIER = "lease identifier"
    LOCAL_LANGUAGE_NAME = "local language name"
    PREFERRED_NAME = "preferred name"
    PROJECT_NUMBER = "project number"
    REGULATORY_IDENTIFIER = "regulatory identifier"
    REGULATORY_NAME = "regulatory name"
    SHORT_NAME = "short name"
    SUBSCRIPTION_WELL_NAME = "subscription well name"
    UNIQUE_IDENTIFIER = "unique identifier"
    WELLBORE_NUMBER = "wellbore number"
