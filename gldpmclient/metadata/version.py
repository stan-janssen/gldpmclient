from dataclasses import dataclass, field
from typing import List, Optional



@dataclass(kw_only=True)
class Version:
    class Meta:
        namespace = "http://tennet.eu/cdm/tennet/v1.0"

    service_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "ServiceVersion",
            "type": "Element",
            "required": True,
            "pattern": r"\d{1,2}\.\d{1,3}(\.\d{1,3})?",
        }
    )
    components: List["Version.Component"] = field(
        default_factory=list,
        metadata={
            "name": "Component",
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class Component:
        component_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "ComponentName",
                "type": "Element",
                "required": True,
            }
        )
        component_version: Optional[str] = field(
            default=None,
            metadata={
                "name": "ComponentVersion",
                "type": "Element",
                "required": True,
                "pattern": r"\d{1,2}\.\d{1,3}(\.\d{1,3})?",
            }
        )
