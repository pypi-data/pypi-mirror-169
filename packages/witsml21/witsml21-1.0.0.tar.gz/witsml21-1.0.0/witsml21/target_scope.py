from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class TargetScope(Enum):
    """
    These values represent the type of scope of the drilling target.

    :cvar VALUE_3_D_VOLUME: Generic 3 dimensional target. Defined by the
        target.
    :cvar ELLIPSOID:
    :cvar ELLIPTICAL: Elliptical targets. Includes circle (semi-major =
        semi-minor axis). Any sections present are ignored.
    :cvar HARD_LINE: Boundary Conditions. Use sections to describe,
        length and width ignore.
    :cvar IRREGULAR: Includes half circle and polygon. Use sections to
        describe, length and width ignored.
    :cvar LEASE_LINE: Boundary Conditions. Use sections to describe,
        length and width ignore.
    :cvar LINE: Line target
    :cvar PLANE: Plane target. Used for horizontal wells. Any sections
        present are ignored.
    :cvar POINT: Point Target. Any sections present are ignored.
    :cvar RECTANGULAR: Rectangular Targets. Includes square (length =
        width). Any sections present are ignored.
    """
    VALUE_3_D_VOLUME = "3D volume"
    ELLIPSOID = "ellipsoid"
    ELLIPTICAL = "elliptical"
    HARD_LINE = "hardLine"
    IRREGULAR = "irregular"
    LEASE_LINE = "lease line"
    LINE = "line"
    PLANE = "plane"
    POINT = "point"
    RECTANGULAR = "rectangular"
