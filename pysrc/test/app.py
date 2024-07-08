import dataclasses
from typing import Annotated, NewType

from litestar import Litestar, get

TestId = NewType("TestId", str)


@dataclasses.dataclass
class TestModel:
    id: Annotated[TestId, "foo"]


@get("/")
def get_test() -> TestModel: ...


app = Litestar(
    [get_test],
)
