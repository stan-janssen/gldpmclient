from uuid import uuid4

import requests
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from .objects import (
    GlMarketDocument,
    GlMarketDocumentBody,
    GlMarketDocumentResponse,
    MessageAddressing,
    RoleType,
)

# pylint: disable=too-many-instance-attributes
class GLDPMClient:
    """
    Client used to communicate to the GLDPM receiver.
    """

    # pylint: disable=too-many-arguments
    def __init__(
        self,
        sender_id: str,
        receiver_id: str,
        carrier_id: str,
        host: str,
        sender_market_role_type=RoleType.RESOURCE_PROVIDER,
        receiver_market_role_type=RoleType.SYSTEM_OPERATOR,
        indent_xml=False,
        http_headers=None,
    ):
        """
        Create a GLDPM Client, used to communicate from one sender
        to one receiver, indicating the carrier of the message.
        """
        self.host = host
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.carrier_id = carrier_id
        self.sender_market_role_type = sender_market_role_type
        self.receiver_market_role_type = receiver_market_role_type

        self.serializer_config = SerializerConfig(indent='  ' if indent_xml else None)
        self.serializer = XmlSerializer(config=self.serializer_config)
        self.parser_context = XmlContext()
        self.parser = XmlParser(context=self.parser_context)

        self.http_headers = http_headers or {}

    def send_generation_load_message(
        self,
        message_body: GlMarketDocumentBody,
        message_addressing: MessageAddressing = None,
    ) -> str:
        """
        Send the GlMarketDocumentBody to the receiver,
        returning the MMCHubResponse.

        Optionally provide the message_adressing to set the
        SOAP headers.
        """
        if not message_addressing:
            message_addressing = MessageAddressing(
                technical_message_id=str(uuid4()),
                sender_id=self.sender_id,
                receiver_id=self.receiver_id,
                carrier_id=self.carrier_id,
                content_type="GenerationLoadForecast",
            )

        message = GlMarketDocument(
            body=GlMarketDocument.Body(message_body),
            header=GlMarketDocument.Header(message_addressing),
        )

        return self._post_message(message, self.host).body.correlation_id

    def _post_message(self, message, url):
        """
        Post the message to the given URL. Serializes the
        request into XML and parses the response XML.
        """
        response = requests.post(
            url,
            data=self._serialize_message(message),
            headers=self.http_headers | {"Content-Type": "application/xml"},
            timeout=30,
        )

        return self._parse_message(response.content)

    def _serialize_message(self, message):
        return self.serializer.render(message).encode("utf-8")

    def _parse_message(self, xml_bytes):
        return self.parser.from_bytes(xml_bytes, GlMarketDocumentResponse)
