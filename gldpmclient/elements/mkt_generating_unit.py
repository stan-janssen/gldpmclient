from dataclasses import dataclass, field
from typing import Optional

from .esmp_active_power import EsmpActivePower
from ..metadata import ResourceIdString


@dataclass(kw_only=True)
class MktGeneratingUnit:
    class Meta:
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    nominal_p: Optional[EsmpActivePower] = field(
        default=None,
        metadata={
            "name": "nominalP",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
