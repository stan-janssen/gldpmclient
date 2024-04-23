from dataclasses import dataclass, field
from typing import Optional

from ..enums import CodingSchemeType


@dataclass
class AreaIdString:
    class Meta:
        name = "AreaID_String"
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 18,
        }
    )
    coding_scheme: Optional[CodingSchemeType] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )

@dataclass
class PartyIdString:
    class Meta:
        name = "PartyID_String"
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 16,
        }
    )
    coding_scheme: Optional[CodingSchemeType] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ResourceIdString:
    class Meta:
        name = "ResourceID_String"
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 18,
        }
    )
    coding_scheme: Optional[CodingSchemeType] = field(
        default=None,
        metadata={
            "name": "codingScheme",
            "type": "Attribute",
            "required": True,
        }
    )
