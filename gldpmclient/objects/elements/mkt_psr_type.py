from dataclasses import dataclass, field
from typing import List, Optional

from .esmp_voltage import EsmpVoltage
from .mkt_generating_unit import MktGeneratingUnit
from ..enums import AssetType


@dataclass(kw_only=True)
class MktPsrType:
    class Meta:
        name = "MktPSRType"
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    psr_type: Optional[AssetType] = field(
        default=None,
        metadata={
            "name": "psrType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    voltage_power_system_resources_high_voltage_limit: Optional[EsmpVoltage] = field(
        default=None,
        metadata={
            "name": "voltage_PowerSystemResources.highVoltageLimit",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    power_system_resources: List[MktGeneratingUnit] = field(
        default_factory=list,
        metadata={
            "name": "PowerSystemResources",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
