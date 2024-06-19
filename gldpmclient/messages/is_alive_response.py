from dataclasses import dataclass, field
from typing import Optional

from ..metadata import Version

@dataclass(kw_only=True)
class IsAliveResponseMessage:
    class Meta:
        namespace = "http://tennet.eu/cdm/tennet/TennetService/Message/v2.0"

    version: Optional[Version] = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://tennet.eu/cdm/tennet/v1.0",
            "required": True,
        }
    )
