from dataclasses import dataclass, field
from datetime import datetime


@dataclass(kw_only=True)
class EsmpDateTimeInterval:
    class Meta:
        name = "ESMP_DateTimeInterval"
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    start: datetime = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    end: datetime = field(
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
