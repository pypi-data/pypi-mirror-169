from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/witsmlv2"


class ToolSubKind(Enum):
    BLIND = "blind"
    BLIND_PLUS_TREND = "blind plus trend"
    CAMERA_BASED_FILM_GYRO_MULTI_SHOT = "camera based film gyro multi shot"
    CAMERA_BASED_FILM_GYRO_SINGLE_SHOT = "camera based film gyro single shot"
    CAMERA_BASED_FILM_MAGNETIC_MULTI_SHOT = "camera based film magnetic multi shot"
    CAMERA_BASED_FILM_MAGNETIC_SINGLE_SHOT = "camera based film magnetic single shot"
    DIPMETER = "dipmeter"
    ELECTRO_MAGNETIC_SURVEY = "electro magnetic survey"
    FERRANTI_INERTIAL_NAVIGATION_SYSTEM = "ferranti inertial navigation system"
    GYRO_SUSPICIOUS = "gyro suspicious"
    GYRO_WHILE_DRILLING = "gyro while drilling"
    INCLINOMETER_ACTUAL = "inclinometer actual"
    INCLINOMETER_PLANNED = "inclinometer planned"
    INCLINOMETER_PLUS_TREND = "inclinometer plus trend"
    MAGNETIC_WHILE_DRILLING = "magnetic while drilling"
    NORTH_SEEKING_GYRO = "north seeking gyro"
    RING_LASER_INERTIAL_GUIDANCE_SURVEYOR = "ring laser inertial guidance surveyor"
    SURFACE_READOUT_GYRO_MULTI_SHOT = "surface readout gyro multi shot"
    SURFACE_READOUT_GYRO_SINGLE_SHOT = "surface readout gyro single shot"
    ZERO_ERROR = "zero error"
    UNKNOWN = "unknown"
