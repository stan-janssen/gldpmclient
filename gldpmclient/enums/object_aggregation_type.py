# pylint: disable=line-too-long
from enum import StrEnum


class ObjectAggregationType(StrEnum):
    AREA                     = "A01"  #: The object being described concerns an area.
    METERING_POINT           = "A02"  #: The object being described concerns a metering point.
    PARTY                    = "A03"  #: The object being described concerns a party.
    AGREEMENT_IDENTIFICATION = "A04"  #: The object being described concerns an agreement identification.
    ACCOUNTING_POINT         = "A05"  #: The object being described concerns an accounting point.
    RESOURCE_OBJECT          = "A06"  #: The object being described concerns a resource object.
    TIELINE                  = "A07"  #: The object being described concerns a tieline.
    RESOURCE_TYPE            = "A08"  #: The object being described concerns a resource type.
    DC_LINK                  = "A09"  #: The object being described concerns a DC link.
    AC_LINK                  = "A10"  #: The object being described concerns an AC link.
    MERCHANT_LINE            = "A11"  #: The object being described concerns a merchant line.
