import os
import tempfile
from unittest.mock import patch
from uuid import uuid4

import pytest
from requests import Response
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from gldpmclient import FileStorageProvider, GLDPMClient, messages, objects
from gldpmclient.metadata import MessageAddressing

from .test_generation_load_message import body


@pytest.fixture
def storage_dir():
    with tempfile.TemporaryDirectory() as directory:
        yield directory


def test_storage(storage_dir):

    sender_id = "1" * 13
    receiver_id = "2" * 13
    carrier_id = "3" * 13

    client = GLDPMClient(
        sender_id=sender_id,
        receiver_id=receiver_id,
        carrier_id=carrier_id,
        host="http://localhost:8080",
        indent_xml=False,
        storage_provider=FileStorageProvider(directory=storage_dir)
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

        message_addressing = MessageAddressing(
            technical_message_id=str(uuid4()),
            sender_id=client.sender_id,
            receiver_id=client.receiver_id,
            carrier_id=client.carrier_id,
        )

        correlation_id = client.send_generation_load_message(body, message_addressing=message_addressing)

        assert correlation_id == "9436b1e8-a21c-4ecc-ad76-80e99027d427"

    assert os.path.exists(os.path.join(storage_dir, f"{correlation_id}_request.xml"))
    assert os.path.exists(os.path.join(storage_dir, f"{correlation_id}_response.xml"))

    with open(os.path.join(storage_dir, f"{correlation_id}_request.xml"), "rb") as file:
        contents = file.read()
        expected_contents = serializer.render(
            messages.GlMarketDocument(
                header=messages.GlMarketDocument.Header(message_addressing=message_addressing),
                body=messages.GlMarketDocument.Body(gl_market_document=body)
            )
        ).encode("utf-8")
        assert contents == expected_contents

    with open(os.path.join(storage_dir, f"{correlation_id}_response.xml"), "rb") as file:
        contents = file.read()
        assert contents == response_content

