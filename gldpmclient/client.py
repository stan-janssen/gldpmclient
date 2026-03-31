from uuid import uuid4

import requests
from xsdata.exceptions import ParserError
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from .exceptions import GLDPMException, HTTPException, ParsingException
from .objects import (
    GlMarketDocument,
    GlMarketDocumentBody,
    GlMarketDocumentResponse,
    MessageAddressing,
    RoleType,
)
from .storage import MessageDirection, StorageProvider


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
        sender_market_role_type: RoleType = RoleType.RESOURCE_PROVIDER,
        receiver_market_role_type: RoleType = RoleType.SYSTEM_OPERATOR,
        indent_xml: bool = False,
        store_xml: bool = False,
        storage_provider: StorageProvider | None = None,
        **request_options
    ):
        """
        Create a GLDPM Client, used to communicate from one sender
        to one receiver, indicating the carrier of the message.

        :param str sender_id: The id of the sending party
        :param str receiver_id: The id of the receiving party
        :param str carrier_id: The id of the carrying party
        :param str host: The hostname of the API where to send the messages to
        :param RoleType sender_market_role_type: The role type of the sending party
        :param RoleType receiver_market_role_type: The role type of the receiving party
        :param bool indent_xml: Whether or not to indent the XML messages
        :param bool store_xml: Whether or not to store the XML messages. Use an XMLStorageProvider
        """
        self.host = host.removesuffix("/")
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.carrier_id = carrier_id
        self.sender_market_role_type = sender_market_role_type
        self.receiver_market_role_type = receiver_market_role_type

        self.serializer_config = SerializerConfig(indent='  ' if indent_xml else None)
        self.serializer = XmlSerializer(config=self.serializer_config)
        self.parser_context = XmlContext()
        self.parser = XmlParser(context=self.parser_context)

        self.request_options = request_options
        self.request_timeout = self.request_options.pop("timeout", 30)
        self.http_headers = self.request_options.pop("headers", {"Content-Type": "application/xml"})

        self.storage_provider = storage_provider

    def send_generation_load_message(
        self,
        message_body: GlMarketDocumentBody,
        message_addressing: MessageAddressing | None = None,
    ) -> str:
        """
        Send the GlMarketDocumentBody to the receiver,
        returning the MMCHubResponse.

        Optionally provide the message_adressing to set the
        SOAP headers.
        """
        if message_addressing is None:
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

        response = self._post_message(message, self.host)
        self._raise_on_gldpm_fault(response)
        return response.body.result.correlation_id

    def _post_message(self, message, url):
        """
        Post the message to the given URL. Serializes the
        request into XML and parses the response XML.
        """
        xml_document: bytes = self._serialize_message(message)
        response = requests.post(
            url,
            data=xml_document,
            headers=self.http_headers,
            timeout=self.request_timeout,
            **self.request_options
        )

        if response.status_code != 200:
            try:
                decoded_response = response.content.decode("utf-8")
            except Exception:
                decoded_response = response.content
            raise HTTPException(
                f"Got HTTP status {response.status_code} when performing request to {url}. "
                f"Response: {decoded_response}"
            )

        response_document = self._parse_message(response.content)

        if self.storage_provider:
            self.storage_provider.store_xml(
                correlation_id=response_document.body.result.correlation_id,
                direction=MessageDirection.REQUEST,
                contents=xml_document
            )
            self.storage_provider.store_xml(
                correlation_id=response_document.body.result.correlation_id,
                direction=MessageDirection.RESPONSE,
                contents=response.content
            )

        return response_document


    def _serialize_message(self, message) -> bytes:
        return self.serializer.render(message).encode("utf-8")

    def _parse_message(self, xml_bytes, message_type=GlMarketDocumentResponse):
        print("GlMarketDocumentResponse raw message:")
        print(xml_bytes)
        try:
            return self.parser.from_bytes(xml_bytes, message_type)
        except ParserError as err:
            try:
                decoded_content = xml_bytes.decode("utf-8")
            except Exception:
                decoded_content = xml_bytes
            raise ParsingException(
                f"Could not parse the following message: {decoded_content}. "
                f"Error: {err}"
            ) from err

    def _raise_on_gldpm_fault(self, response):
        if response.body.fault:
            raise GLDPMException(fault=response.body.fault)
