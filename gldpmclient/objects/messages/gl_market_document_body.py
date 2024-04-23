# pylint: disable=too-many-instance-attributes
from dataclasses import dataclass, field
from datetime import datetime
from typing import List

from ..enums import MessageType, ProcessType, RoleType
from ..metadata import PartyIdString
from ..elements import EsmpDateTimeInterval, TimeSeries



@dataclass(kw_only=True)
class GlMarketDocumentBody:
    class Meta:
        name = "GL_MarketDocument"
        namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "required": True,
            "max_length": 35,
        }
    )
    revision_number: int = field(
        metadata={
            "name": "revisionNumber",
            "type": "Element",
            "required": True,
        }
    )
    type_value: MessageType = field(
        metadata={
            "name": "type",
            "type": "Element",
            "required": True,
        }
    )
    process_type: ProcessType = field(
        metadata={
            "name": "process.processType",
            "type": "Element",
            "required": True,
        }
    )
    sender_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "sender_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        }
    )
    sender_market_participant_market_role_type: RoleType = field(
        metadata={
            "name": "sender_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        }
    )
    receiver_market_participant_m_rid: PartyIdString = field(
        metadata={
            "name": "receiver_MarketParticipant.mRID",
            "type": "Element",
            "required": True,
        }
    )
    receiver_market_participant_market_role_type: RoleType = field(
        metadata={
            "name": "receiver_MarketParticipant.marketRole.type",
            "type": "Element",
            "required": True,
        }
    )
    created_date_time: datetime = field(
        metadata={
            "name": "createdDateTime",
            "type": "Element",
            "required": True,
            "format": "%Y-%m-%dT%H:%M:%S%z"
        }
    )
    time_period_time_interval: EsmpDateTimeInterval = field(
        metadata={
            "name": "time_Period.timeInterval",
            "type": "Element",
            "required": True,
        }
    )
    time_series: List[TimeSeries] = field(
        default_factory=list,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
            "min_occurs": 1,
        }
    )
