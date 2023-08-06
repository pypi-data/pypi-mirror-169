from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from witsml21.abstract_cartesian2d_position import AbstractCartesian2DPosition
from witsml21.public_land_survey_system_location import PublicLandSurveySystemLocation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PublicLandSurveySystem2DPosition(AbstractCartesian2DPosition):
    class Meta:
        name = "PublicLandSurveySystem2dPosition"

    public_land_survey_system_location: Optional[PublicLandSurveySystemLocation] = field(
        default=None,
        metadata={
            "name": "PublicLandSurveySystemLocation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
