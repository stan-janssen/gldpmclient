from uuid import uuid4

from gldpmclient import GLDPMClient, objects

def test_parse_gl_market_document_response():
    client = GLDPMClient(
        sender_id="123",
        receiver_id="123",
        carrier_id="123",
        host="none",
        indent_xml=True
    )

    response = objects.GlMarketDocumentResponse(
        body=objects.GlMarketDocumentResponse.Body(
            correlation_id=str(uuid4())
        )
    )

    serialized = client._serialize_message(response)
    print(serialized)
    parsed = client._parse_message(serialized)

    assert parsed == response

