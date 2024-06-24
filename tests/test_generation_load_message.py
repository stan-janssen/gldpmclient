from datetime import datetime
from zoneinfo import ZoneInfo

from gldpmclient import GLDPMClient, objects

local_timezone = ZoneInfo("Europe/Amsterdam")


def test_generation_load_message():

    client = GLDPMClient(
        sender_id=sender_id,
        receiver_id=receiver_id,
        carrier_id=carrier_id,
        host="none",
        indent_xml=True
    )

    serialized_message = client._serialize_message(message)

    expected_message = b"""<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
  <soapenv:Header>
    <ns1:MessageAddressing xmlns:ns1="http://sys.svc.tennet.nl/MMCHub/Header/v1">
      <ns1:technicalMessageId>3609cee5-1e5e-45ca-a238-2735e472a9b2</ns1:technicalMessageId>
      <ns1:senderId>1111111111111</ns1:senderId>
      <ns1:receiverId>2222222222222</ns1:receiverId>
      <ns1:carrierId>3333333333333</ns1:carrierId>
      <ns1:contentType>GenerationLoadForecast</ns1:contentType>
    </ns1:MessageAddressing>
  </soapenv:Header>
  <soapenv:Body>
    <ns1:GL_MarketDocument xmlns:ns1="urn:iec62325.351:tc57wg16:451-6:generationloaddocument:3:0">
      <ns1:mRID>e8f5f0ed-5e09-41ef-8cc5-c1989934f0be</ns1:mRID>
      <ns1:revisionNumber>1</ns1:revisionNumber>
      <ns1:type>A67</ns1:type>
      <ns1:process.processType>A14</ns1:process.processType>
      <ns1:sender_MarketParticipant.mRID codingScheme="A10">1111111111111</ns1:sender_MarketParticipant.mRID>
      <ns1:sender_MarketParticipant.marketRole.type>A27</ns1:sender_MarketParticipant.marketRole.type>
      <ns1:receiver_MarketParticipant.mRID codingScheme="A10">2222222222222</ns1:receiver_MarketParticipant.mRID>
      <ns1:receiver_MarketParticipant.marketRole.type>A04</ns1:receiver_MarketParticipant.marketRole.type>
      <ns1:createdDateTime>2023-12-31T23:00:00Z</ns1:createdDateTime>
      <ns1:time_Period.timeInterval>
        <ns1:start>2023-12-31T23:00Z</ns1:start>
        <ns1:end>2024-01-31T23:00Z</ns1:end>
      </ns1:time_Period.timeInterval>
      <ns1:TimeSeries>
        <ns1:mRID>123456789012345678A01</ns1:mRID>
        <ns1:businessType>A01</ns1:businessType>
        <ns1:objectAggregation>A06</ns1:objectAggregation>
        <ns1:registeredResource.mRID>123456789012345678</ns1:registeredResource.mRID>
        <ns1:quantity_Measure_Unit.name>MAW</ns1:quantity_Measure_Unit.name>
        <ns1:curveType>A01</ns1:curveType>
        <ns1:Period>
          <ns1:timeInterval>
            <ns1:start>2023-12-31T23:00Z</ns1:start>
            <ns1:end>2024-01-31T23:00Z</ns1:end>
          </ns1:timeInterval>
          <ns1:resolution>PT15M</ns1:resolution>
          <ns1:Point>
            <ns1:position>1</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>2</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>3</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>4</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>5</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>6</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>7</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>8</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>9</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>10</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>11</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>12</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>13</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>14</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>15</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>16</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>17</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>18</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>19</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>20</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>21</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>22</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>23</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>24</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>25</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>26</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>27</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>28</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>29</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>30</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>31</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>32</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>33</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>34</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>35</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>36</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>37</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>38</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>39</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>40</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>41</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>42</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>43</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>44</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>45</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>46</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>47</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>48</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>49</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>50</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>51</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>52</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>53</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>54</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>55</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>56</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>57</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>58</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>59</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>60</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>61</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>62</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>63</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>64</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>65</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>66</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>67</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>68</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>69</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>70</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>71</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>72</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>73</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>74</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>75</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>76</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>77</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>78</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>79</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>80</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>81</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>82</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>83</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>84</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>85</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>86</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>87</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>88</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>89</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>90</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>91</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>92</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>93</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>94</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>95</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
          <ns1:Point>
            <ns1:position>96</ns1:position>
            <ns1:quantity>1.23</ns1:quantity>
          </ns1:Point>
        </ns1:Period>
      </ns1:TimeSeries>
    </ns1:GL_MarketDocument>
  </soapenv:Body>
</soapenv:Envelope>
"""

    assert serialized_message == expected_message




# ------------------------------------------------------------ #
#                  A generic testing message                   #
# ------------------------------------------------------------ #

sender_id = "1" * 13
receiver_id = "2" * 13
carrier_id = "3" * 13
transformer_ean = "123456789012345678"
message_id = "e8f5f0ed-5e09-41ef-8cc5-c1989934f0be"
technical_message_id = "3609cee5-1e5e-45ca-a238-2735e472a9b2"

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
        registered_resource_m_rid=transformer_ean,
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

message_addressing = objects.MessageAddressing(
    technical_message_id = technical_message_id,
    sender_id = sender_id,
    receiver_id = receiver_id,
    carrier_id = carrier_id,
    content_type = "GenerationLoadForecast"
)

message = objects.GlMarketDocument(
    header=objects.GlMarketDocument.Header(
        message_addressing=message_addressing
    ),
    body=objects.GlMarketDocument.Body(
        gl_market_document=body
    )
)
