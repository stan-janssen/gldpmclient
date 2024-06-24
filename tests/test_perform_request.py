from unittest.mock import patch

from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from requests import Response

from gldpmclient import GLDPMClient, objects
from .test_generation_load_message import body


def test_perform_request():
    sender_id = "1" * 13
    receiver_id = "2" * 13
    carrier_id = "3" * 13

    client = GLDPMClient(
        sender_id=sender_id,
        receiver_id=receiver_id,
        carrier_id=carrier_id,
        host="http://localhost:8080",
        indent_xml=True,
    )

    response_message = objects.GlMarketDocumentResponse(
        body=objects.GlMarketDocumentResponse.Body(
            result=objects.GlMarketDocumentResponse.Body.Result(
                correlation_id="9436b1e8-a21c-4ecc-ad76-80e99027d427"
            )
        ),
    )

    serializer = XmlSerializer(config=SerializerConfig())
    response_content = serializer.render(response_message).encode("utf-8")

    with patch("requests.post") as patched_requests:
        mock_response = Response()
        mock_response.status_code = 200
        mock_response._content = response_content
        patched_requests.return_value = mock_response

        correlation_id = client.send_generation_load_message(body)

        assert correlation_id == "9436b1e8-a21c-4ecc-ad76-80e99027d427"
