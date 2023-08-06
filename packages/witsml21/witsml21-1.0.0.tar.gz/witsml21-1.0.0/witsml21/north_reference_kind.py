from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class NorthReferenceKind(Enum):
    """The kinds of north references likely to be encountered in oil &amp; gas
    data. A north reference is a clear definition of what is meant by the word
    "north" (and by extension all of the compass points). Some of this wording
    is from the NGS Geodetic Glossary.

    true north - the common name of what is formally called geodetic north. This is along the rotational axis of the earth, and cannot be easily measured in the field.  The rigorous definition of geodetic north is "the positive direction of that line parallel to the Earth's axis of rotation and perpendicularly to the left of an observer facing in the direction of the Earth's rotation." True north is normally computed from an imperfect measurement of north.
    astronomic north - An estimate of true north derived from astronomic observations. This differs from true north slightly because astronomic instruments rely on gravity to define "up" (the vertical) while the earth's gravity field is seldom perfectly vertical. A "Laplace correction" is applied to the astronomic north to get geodetic north. Astronomic north is seldom used in oil &amp; gas operations.
    magnetic north - The direction of the Earth's magnetic north pole. A "declination" correction is applied to calculate true north from magnetic north. Since the Earth's magnetic north pole is constantly in motion, the date and time an observation is made are critically important to be able to find the correct declination value to be used.
    compass north - A raw reading of the north-seeking end of a needle or other magnetic component of a compass. This differs from magnetic north because of the influence of iron and other magnetic materials which disturb the Earth's magnetic field close to the compass instrument. There may be a correction applied to compass north to realize a magnetic north reading. This kind of north is encountered in older oil &amp; gas data.
    grid north - The direction of the north lines on a map projection. In most projections there is only one north line which points to true geodetic north, the central meridian in a UTM projection, for example. At any point on a grid there can be a "convergence angle" defined which relates the grid north to true geodetic north. Grid north is not measured in the field; it must be calculated.
    plant north - A direction in a local engineering coordinate reference system which is normally oriented more or less north. This is used in industrial facilities (like gas plants or offshore platforms) and for smaller areas like drilling pads. Distances and directions in this local system are easier to handle without need for a professional land surveyor because the need for accuracy is less and the distances involved are limited. In this case a surveyor might determine the location of a corner of the facility and the angle between true north and the apparent north of the facility.
    """
    ASTRONOMIC_NORTH = "astronomic north"
    COMPASS_NORTH = "compass north"
    GRID_NORTH = "grid north"
    MAGNETIC_NORTH = "magnetic north"
    PLANT_NORTH = "plant north"
    TRUE_NORTH = "true north"
