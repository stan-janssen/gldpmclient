# pylint: disable=duplicate-code
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class GlMarketDocumentResponse():
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: str = field(
        metadata = {
            "name": "Header",
            "type": "Element",
        }
    )

    body: "GlMarketDocumentResponse.Body" = field(
        metadata={
            "type": "Element",
            "name": "Body"
        }
    )

    @dataclass(kw_only=True)
    class Body:

        response: "GlMarketDocumentResponse.Body.GlMarketDocumentResponseBody" = field(
            metadata={
                "type": "Element",
                "name": "GL_MarketDocumentResponse",
                "namespace": "http://sys.svc.tennet.nl/GenerationLoad/v1"
            }
        )

        @dataclass(kw_only=True)
        class GlMarketDocumentResponseBody:
            correlation_id: str = field(
                metadata={
                    "name": "correlationId",
                    "type": "Element",
                    "namespace": "http://sys.svc.tennet.nl/MMCHub/common/v1",
                    "required": True,
                    "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
                }
            )
