# pylint: disable=duplicate-code
from dataclasses import dataclass, field

from ..enums import UnitSymbol


@dataclass(kw_only=True)
class EsmpVoltage:
    class Meta:
        name = "ESMP_Voltage"
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"([0-9]+((\.[0-9])*))",
        }
    )
    unit: UnitSymbol = field(
        init=False,
        default=UnitSymbol.KVT,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
