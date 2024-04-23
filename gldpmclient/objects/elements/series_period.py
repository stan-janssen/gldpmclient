from dataclasses import dataclass, field
from typing import List

from xsdata.models.datatype import XmlDuration

from .esmp_date_time_interval import EsmpDateTimeInterval
from .point import Point


@dataclass(kw_only=True)
class SeriesPeriod:
    class Meta:
        name = "Series_Period"
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "timeInterval",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    resolution: XmlDuration = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    points: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "min_occurs": 1,
        }
    )
