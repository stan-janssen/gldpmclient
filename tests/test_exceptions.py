from dataclasses import dataclass, field
from unittest.mock import patch

import pytest
from requests import Response
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from gldpmclient import GLDPMClient, objects, exceptions
from .test_generation_load_message import message

serializer = XmlSerializer(config=SerializerConfig(xml_declaration=False))


@dataclass
class HTMLDocument:
    """
    Dummy HTML document class for non-functional responses.
    """

    class Meta:
        name = "html"

    head: str = field(metadata={"type": "Element", "name": "head"})

    body: str = field(metadata={"type": "Element", "name": "body"})


@pytest.mark.parametrize(
    "test_message,expected_exception",
    [
        (
            serializer.render(HTMLDocument(head="Hello", body="World")).encode("utf-8"),
            exceptions.ParsingException("Could not parse the following message: <html><head>Hello</head><body>World</body></html>. Error: Unknown property {http://schemas.xmlsoap.org/soap/envelope/}Envelope:head" ),
        ),
        (
            b"\xff\x12\x34\x56",
            exceptions.ParsingException("Could not parse the following message: b'\\xff\\x124V'. Error: not well-formed (invalid token): line 1, column 0"),
        ),
    ],
    ids=["html-response", "non-unicode-response"],
)
def test_parsing_exceptions(test_message, expected_exception):
    client = GLDPMClient(
        sender_id="1" * 13,
        receiver_id="2" * 13,
        carrier_id="3" * 13,
        host="http://localhost:8080",
        indent_xml=True,
    )

    with pytest.raises(expected_exception.__class__) as exc_info:
        client._parse_message(test_message)

    assert exc_info.value.args[0] == expected_exception.args[0]


def test_gldpm_faults():
    client = GLDPMClient(
        sender_id="1" * 13,
        receiver_id="2" * 13,
        carrier_id="3" * 13,
        host="http://localhost:8080",
        indent_xml=True,
    )

    test_message = objects.GlMarketDocumentResponse(
        header="",
        body=objects.GlMarketDocumentResponse.Body(
            fault=objects.Fault(faultcode="123", faultstring="Something went wrong")
        ),
    )

    with pytest.raises(exceptions.GLDPMException) as exc_info:
        client._raise_on_gldpm_fault(test_message)

    assert exc_info.value.fault.faultcode == "123"
    assert exc_info.value.fault.faultstring == "Something went wrong"


@pytest.mark.parametrize(
    'response_content,expected_err',
    [(b"Bad Gateway", "Bad Gateway"), (b"\xff\x12", "b'\\xff\\x12'")],
    ids=["bad-gateway","non-unicode-response"]
)
def test_http_exception(response_content, expected_err):
    client = GLDPMClient(
        sender_id="1" * 13,
        receiver_id="2" * 13,
        carrier_id="3" * 13,
        host="http://localhost:8080",
        indent_xml=True,
    )

    with patch('requests.post') as patched_requests:
        mock_response = Response()
        mock_response.status_code = 502
        mock_response._content = response_content
        patched_requests.return_value = mock_response

        with pytest.raises(exceptions.HTTPException) as exc_info:
            client._post_message(message, client.host)

        assert exc_info.value.args[0] == f'Got HTTP status 502 when performing request to http://localhost:8080. Response: {expected_err}'
