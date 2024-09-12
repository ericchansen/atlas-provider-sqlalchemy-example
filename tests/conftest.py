from datetime import datetime, timedelta
from random import randint
from uuid import uuid4

from _pytest.fixtures import SubRequest
from numpy import array
from numpy.random import randn
from pytest import fixture

from example.enum import EnumExample

DEVICE = "device"
ENUM_EXAMPLE = "enum_example"
LOCATION = "location"
N_CLASSES = "n_classes"
PARAMS = {
    DEVICE: ["blind-camel", "please-work"],
    ENUM_EXAMPLE: [x for x in EnumExample],
    LOCATION: ["here", "there"],
    N_CLASSES: [2, 3],
}


def random_datetime() -> datetime:
    start = datetime(1970, 1, 1)
    end = datetime.now()
    random_datetime = start + timedelta(
        seconds=randint(0, int((end - start).total_seconds()))
    )
    return random_datetime


@fixture
def correlation_id() -> str:
    return str(uuid4())


@fixture(params=[random_datetime() for _ in range(2)])
def datetime_fixture(request: SubRequest) -> datetime:
    return request.param


@fixture(params=PARAMS[DEVICE])
def device(request: SubRequest) -> str:
    return request.param


@fixture(params=PARAMS[ENUM_EXAMPLE])
def enum_example(request: SubRequest) -> EnumExample:
    return request.param


@fixture(params=PARAMS[LOCATION])
def location(request: SubRequest) -> EnumExample:
    return request.param


@fixture
def logits(logits_numpy: array) -> list[float]:
    return logits_numpy.tolist()


@fixture(params=PARAMS[N_CLASSES])
def logits_numpy(request: SubRequest) -> array:
    return randn(request.param)
