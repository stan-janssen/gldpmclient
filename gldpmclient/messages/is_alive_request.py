from dataclasses import dataclass


@dataclass(kw_only=True)
class IsAliveRequestMessage:
    class Meta:
        namespace = "http://tennet.eu/cdm/tennet/TennetService/Message/v2.0"
