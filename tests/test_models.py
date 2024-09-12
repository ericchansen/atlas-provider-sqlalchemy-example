from datetime import datetime

from example.enum import EnumExample
from example.one.models import Simple
from example.two.models import Inference


class TestInference:
    def test_init(
        self,
        correlation_id: str,
        datetime_fixture: datetime,
        device: str,
        enum_example: EnumExample,
        location: str,
        logits: list[float],
    ) -> None:
        Inference(
            _class=enum_example,
            correlation_id=correlation_id,
            datetime=datetime_fixture,
            device=device,
            location=location,
            logits=logits,
        )

    def test_init_no_args(self) -> None:
        Inference()


class TestSimple:
    def test_init(self) -> None:
        Simple(integer=0)
        Simple(integer=1)
