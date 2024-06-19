# pylint: disable=duplicate-code
from dataclasses import dataclass, field


@dataclass(kw_only=True)
class MmcHubResponse:
    class Meta:
        name = "MMCHubResponse"
        target_namespace = "http://sys.svc.tennet.nl/MMCHub/common/v1"

    correlation_id: str = field(
        metadata={
            "name": "correlationId",
            "type": "Element",
            "namespace": "http://sys.svc.tennet.nl/MMCHub/common/v1",
            "required": True,
            "pattern": r"[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}",
        }
    )
