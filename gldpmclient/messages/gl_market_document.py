from dataclasses import dataclass, field

from .gl_market_document_body import GlMarketDocumentBody
from ..metadata import MessageAddressing


@dataclass(kw_only=True)
class GlMarketDocument:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    header: "GlMarketDocument.Header" = field(
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )

    body: "GlMarketDocument.Body" = field(
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Header:
        class Meta:
            namespace = "http://sys.svc.tennet.nl/MMCHub/Header/v1"

        message_addressing: MessageAddressing = field(
            default=None,
            metadata={
                "name": "MessageAddressing",
                "type": "Element"
            }
        )

    @dataclass
    class Body:
        class Meta:
            namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

        gl_market_document: GlMarketDocumentBody = field(
            default=None,
            metadata={
                "name": "GL_MarketDocument",
                "type": "Element"
            }
        )
