from gldpmclient.objects import EsmpDateTimeInterval
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser


local_timezone = ZoneInfo("Europe/Amsterdam")


def test_serialize_esmp_date_time_interval():
    e = EsmpDateTimeInterval(
        start=datetime(2024, 1, 1, 0, 0, 0, tzinfo=local_timezone),
        end=datetime(2024, 1, 2, 0, 0, 0, tzinfo=local_timezone)
    )

    config = SerializerConfig(indent='  ')
    serializer = XmlSerializer(config=config)

    result = serializer.render(e)

    expected_result = """<?xml version="1.0" encoding="UTF-8"?>
<ESMP_DateTimeInterval>
  <ns0:start xmlns:ns0="urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0">2023-12-31T23:00Z</ns0:start>
  <ns0:end xmlns:ns0="urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0">2024-01-01T23:00Z</ns0:end>
</ESMP_DateTimeInterval>
"""

    assert result == expected_result


def test_parse_esmp_date_time_interval():

    input_xml = """<ns1:ESMP_DateTimeInterval xmlns:ns1="urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0">
  <ns0:start xmlns:ns0="urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0">2023-12-31T23:00Z</ns0:start>
  <ns0:end xmlns:ns0="urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0">2024-01-01T23:00Z</ns0:end>
</ns1:ESMP_DateTimeInterval>
"""

    context = XmlContext()
    parser = XmlParser(context=context)
    result = parser.from_string(input_xml)

    expected_result = EsmpDateTimeInterval(
        start=datetime(2024, 1, 1, 0, 0, 0, tzinfo=local_timezone),
        end=datetime(2024, 1, 2, 0, 0, 0, tzinfo=local_timezone)
    )

    assert result == expected_result
