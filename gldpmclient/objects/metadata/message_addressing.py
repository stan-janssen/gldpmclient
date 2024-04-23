from dataclasses import dataclass, field
from typing import Optional


@dataclass(kw_only=True)
class MessageAddressing:
    class Meta:
        name = "MessageAddressing"
        namespace = "http://sys.svc.tennet.nl/MMCHub/Header/v1"

    technical_message_id: str = field(
        metadata={
            "name": "technicalMessageId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    correlation_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "correlationId",
            "type": "Element",
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
    sender_id: str = field(
        metadata={
            "name": "senderId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{13}",
        }
    )
    receiver_id: str = field(
        metadata={
            "name": "receiverId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{13}",
        }
    )
    carrier_id: str = field(
        metadata={
            "name": "carrierId",
            "type": "Element",
            "required": True,
            "pattern": r"[0-9]{13}",
        }
    )
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
        }
    )
