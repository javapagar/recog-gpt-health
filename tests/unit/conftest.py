import json

import pytest

@pytest.fixture(scope="module")
def event_v2():
    with open("tests/events/event_api_gateway_v2.json") as event:
        test_event = json.loads(event.read())
    return test_event

@pytest.fixture(scope="module")
def event_v2_400_error():
    with open("tests/events/event_400_error.json") as event:
        test_event = json.loads(event.read())
    return test_event