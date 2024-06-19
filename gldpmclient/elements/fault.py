from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class Fault:
    """
    Generic SOAP Fault that is part of the SOAP specification.
    This is the SOAP 1.1 version of this type.
    """
    faultcode: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    faultstring: str = field(
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    faultactor: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    detail: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
