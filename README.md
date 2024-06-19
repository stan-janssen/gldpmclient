GLDPM Client for Python
=======================

Basic client that allows you to send Generation Load Market Document
messages. This is used in the energy sector to communicate day-ahead
forecasting information.

Installation
------------

```
pip install gldpmclient
```

Usage
-----

```python
from uuid import uuid4
from gldpmclient import GLDPMClient, objects, exceptions


# Create the GLDPM Client object

client = GLDPMClient(
    sender_id=sender_id,
    receiver_id=receiver_id,
    carrier_id=carrier_id,
    host="https://gldpm-receiver-url.com/SendGenerationLoadMessage",
    sender_market_role_type=RoleType.RESOURCE_PROVIDER,
    receiver_market_role_type=RoleType.SYSTEM_OPERATOR,
    indent_xml=True,
    # Optionally add additional keyword arguments that are
    # passed to requests.post here:
    auth=('username', 'password'),
    timeout=60
)

# Create a message by packing a list of Points into a
# SeriesPeriod and into a TimeSeries

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
            start=datetime(2024, 1, 1, 0, 0, 0).astimezone(),
            end=datetime(2024, 2, 1, 0, 0, 0).astimezone()
        ),
        resolution="PT15M",
        points=points
    )
]

time_series = [
    objects.TimeSeries(
        m_rid=f"8765000000001{str(objects.BusinessType.PRODUCTION)}",
        business_type=objects.BusinessType.PRODUCTION,
        object_aggregation=objects.ObjectAggregationType.RESOURCE_OBJECT,
        registered_resource_m_rid="8765000000001",
        quantity_measure_unit_name=objects.UnitOfMeasureType.MEGAWATT,
        curve_type=objects.CurveType.SEQUENTIAL_FIXED_SIZE_BLOCK,
        periods=periods
    )
]

# Create the Generation Load Market Document body by adding
# metadata about the timeseries

body = objects.GlMarketDocumentBody(
    m_rid=str(uuid4()),
    revision_number=1,
    type_value=objects.MessageType.RESOURCE_PROVIDER_SCHEDULE_FOR_PRODUCTION_CONSUMPTION,
    process_type=objects.ProcessType.FORECAST,
    sender_market_participant_market_role_type=objects.RoleType.RESOURCE_PROVIDER,
    sender_market_participant_m_rid=objects.PartyIdString(
        sender_id, 
        coding_scheme=objects.CodingSchemeType.GS1
    ),
    receiver_market_participant_market_role_type=objects.RoleType.SYSTEM_OPERATOR,
    receiver_market_participant_m_rid=objects.PartyIdString(
        receiver_id, 
        coding_scheme=objects.CodingSchemeType.GS1
    ),
    created_date_time=datetime.now().astimezone(),
    time_period_time_interval=periods[0].time_interval,
    time_series=time_series
)


# Send the message to the receiver. This serializes the
# message and parses the response, and returns the
# correlation_id for the message.

try:
    correlation_id: str = client.send_generation_load_message(body=body)
except exceptions.GLDPMException as err:
    # Detailed fault informatien from the SOAP 
    # message is availabe in the exception:
    fault: objects.Fault = err.fault
    print(fault.faultcode)
    print(fault.faultstring)
    print(fault.faultactor)
    print(fault.details)

```

The response from the receiver will only be the correlation_id (str) for the message. You can use this ID to correlate future messages.


Enumerations
------------

The GLDPM protocol contains many enumerated types that describe asset types, business types, curve types, et cetera. These are denoted by A-codes, like A01, A02, and so on. To make these more human-readable in the code, these are available as human readable strings, like:

- `BusinessType.PRODUCTION`
- `CurveType.SEQUENTIAL_FIXED_SIZE_BLOCK`

Look in the `gldpmclient/objects/enums` directory for all possible options.


Use of Python types
-------------------

Most properties will accept and return usual Python types. Some things to look out for:

- You can use regular `datetime.datetime` objects. Be mindful that these will be converted into the UTC timezone before serialization. You should always make sure that your timestamps have timezone information associated with them before offering them to the library code, or you should know how Python interprets a naive timestamp on the server you are running the code on: a naive timestamp is assumed to be in the server's timezone, which may be different from the timezone you use during development.
- Durations are not converted to `datetime.timedelta` objects, but are kept as strings.
- Point Values can be offered as integers, decimals or floats. 


Contributing
------------

You are very welcome to open up issues or pull requests here to improve `gldpmclient`.

Development
-----------

For development, clone this repository, and install the requirements:

```
pip install -e .[dev]
```

You can run the test suite (which generates a coverage report as well) by running:

```
pytest
```
