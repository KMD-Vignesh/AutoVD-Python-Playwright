from dataclasses import dataclass
from typing import Self

from library.helper.vd_play import PlayVD



@dataclass
class PageVD:
    def __init__(self, playVD: PlayVD) -> None:
        self.playVD: PlayVD = playVD

    def open_app(self, url: str) -> Self:
        self.playVD.open(url=url)
        return self
    
    def log(self, message: str) -> Self:
        self.playVD.log(message=message)
        return self

    def sleep(self, seconds: int | float) -> Self:
        self.playVD.sleep(seconds=seconds)
        return self

    def assert_true(self, condition: bool, failure_message: str = "Assertion") -> Self:
        self.playVD.assert_true(condition=condition, failure_message=failure_message)
        return self

    def assert_false(self, condition: bool, failure_message: str = "Assertion") -> Self:
        self.playVD.assert_false(condition=condition, failure_message=failure_message)
        return self