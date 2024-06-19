from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
from zoneinfo import ZoneInfo

import pytest

from gldpmclient import GLDPMClient, objects, exceptions


local_timezone = ZoneInfo("Europe/Amsterdam")


def test_perform_request_with_fault():

    sender_id = "1" * 13
    receiver_id = "2" * 13
    carrier_id = "3" * 13
    transformer_ean = "123456789012345678"
    message_id = "e8f5f0ed-5e09-41ef-8cc5-c1989934f0be"
    technical_message_id = "3609cee5-1e5e-45ca-a238-2735e472a9b2"

    client = GLDPMClient(
        sender_id=sender_id,
        receiver_id=receiver_id,
        carrier_id=carrier_id,
        host="http://localhost:8080",
        indent_xml=True
    )

    points = [
        objects.Point(
            position=i+1,
            quantity=1.23
        )
        for i in range(96)
    ]

    periods = [
        objects.SeriesPeriod(
            time_interval=objects.EsmpDateTimeInterval(
                start=datetime(2024,1,1,0,0,0,tzinfo=local_timezone),
                end=datetime(2024,2,1,0,0,0,tzinfo=local_timezone)
            ),
            resolution="PT15M",
            points=points
        )
    ]

    time_series = [
        objects.TimeSeries(
            m_rid=f"{transformer_ean}{str(objects.BusinessType.PRODUCTION)}",
            business_type=objects.BusinessType.PRODUCTION,
            object_aggregation=objects.ObjectAggregationType.RESOURCE_OBJECT,
            registered_resource_m_rid=objects.ResourceIdString(
                value=transformer_ean,
                coding_scheme=objects.CodingSchemeType.GS1
            ),
            quantity_measure_unit_name=objects.UnitOfMeasureType.MEGAWATT,
            curve_type=objects.CurveType.SEQUENTIAL_FIXED_SIZE_BLOCK,
            periods=periods
        )
    ]

    body = objects.GlMarketDocumentBody(
        m_rid=message_id,
        revision_number=1,
        type_value=objects.MessageType.RESOURCE_PROVIDER_SCHEDULE_FOR_PRODUCTION_CONSUMPTION,
        process_type=objects.ProcessType.FORECAST,
        sender_market_participant_m_rid=objects.PartyIdString(sender_id, coding_scheme=objects.CodingSchemeType.GS1),
        sender_market_participant_market_role_type=objects.RoleType.RESOURCE_PROVIDER,
        receiver_market_participant_m_rid=objects.PartyIdString(receiver_id, coding_scheme=objects.CodingSchemeType.GS1),
        receiver_market_participant_market_role_type=objects.RoleType.SYSTEM_OPERATOR,
        created_date_time=datetime(2024,1,1,0,0,0, tzinfo=local_timezone),
        time_period_time_interval=periods[0].time_interval,
        time_series=time_series
    )


    server = HTTPServer(('localhost', 8080), GLDPMRequestHandler)
    server.gldpm_client = client
    t = Thread(target=server.serve_forever)
    t.start()

    with pytest.raises(exceptions.GLDPMException) as error:
        correlation_id = client.send_generation_load_message(body)
        assert error.fault.faultcode == "123"
        assert error.fault.faultstring == "Something went wrong"

    server.shutdown()
    t.join()


class GLDPMRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        response = objects.GlMarketDocumentResponse(
            header="",
            body=objects.GlMarketDocumentResponse.Body(
                fault=objects.Fault(
                    faultcode="123",
                    faultstring="Something went wrong"
                )
            ),
        )

        serialized = self.server.gldpm_client._serialize_message(response)

        response_length = len(serialized)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(serialized)
