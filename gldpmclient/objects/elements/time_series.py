# pylint: disable=too-many-instance-attributes
from dataclasses import dataclass, field
from typing import List, Optional

from .mkt_psr_type import MktPsrType
from .series_period import SeriesPeriod
from ..enums import BusinessType, CurveType, IndicatorType, ObjectAggregationType, UnitOfMeasureType
from ..metadata import AreaIdString, ResourceIdString


@dataclass(kw_only=True)
class TimeSeries:
    class Meta:
        target_namespace = "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0"

    m_rid: str = field(
        metadata={
            "name": "mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
            "max_length": 35,
        }
    )
    business_type: BusinessType = field(
        metadata={
            "name": "businessType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    object_aggregation: ObjectAggregationType = field(
        metadata={
            "name": "objectAggregation",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    in_bidding_zone_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "inBiddingZone_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    out_bidding_zone_domain_m_rid: Optional[AreaIdString] = field(
        default=None,
        metadata={
            "name": "outBiddingZone_Domain.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    registered_resource_m_rid: Optional[ResourceIdString] = field(
        default=None,
        metadata={
            "name": "registeredResource.mRID",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    registered_resource_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "registeredResource.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    quantity_measure_unit_name: UnitOfMeasureType = field(
        metadata={
            "name": "quantity_Measure_Unit.name",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    curve_type: CurveType = field(
        metadata={
            "name": "curveType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
            "required": True,
        }
    )
    cancelled_ts: Optional[IndicatorType] = field(
        default=None,
        metadata={
            "name": "cancelledTS",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    mkt_psrtype: Optional[MktPsrType] = field(
        default=None,
        metadata={
            "name": "MktPSRType",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
    periods: List[SeriesPeriod] = field(
        default_factory=list,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0",
        }
    )
