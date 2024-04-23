from dataclasses import dataclass

from .mmc_hub_response import MmcHubResponse

@dataclass(kw_only=True)
class AcknowledgementMarketDocumentResponse(MmcHubResponse):
    class Meta:
        name = "Acknowledgement_MarketDocumentResponse"
        namespace = "http://sys.svc.tennet.nl/GenerationLoad/v1"
