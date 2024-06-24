# pylint: disable=duplicate-code
from dataclasses import dataclass, field
from typing import Optional

from ..elements import Fault


@dataclass(kw_only=True)
class GlMarketDocumentResponse():
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: Optional[str] = field(
        default="",
        metadata = {
            "name": "Header",
            "type": "Element",
        },
    )

    body: "GlMarketDocumentResponse.Body" = field(
        metadata={
            "type": "Element",
            "name": "Body"
        }
    )

    @dataclass(kw_only=True)
    class Body:

        result: Optional["GlMarketDocumentResponse.Body.Result"] = field(
            default=None,
            metadata={
                "type": "Element",
                "name": "GL_MarketDocumentResponse",
                "namespace": "http://sys.svc.tennet.nl/GenerationLoad/v1"
            }
        )

        fault: Optional[Fault] = field(
            default=None,
            metadata={
                "type": "Element",
                "name": "Fault",
            }
        )

        @dataclass(kw_only=True)
        class Result:
            correlation_id: str = field(
                metadata={
                    "name": "correlationId",
                    "type": "Element",
                    "namespace": "http://sys.svc.tennet.nl/MMCHub/common/v1",
                    "required": True,
                    "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
                }
            )
