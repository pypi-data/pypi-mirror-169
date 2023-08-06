"""Models for mini display number."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from typing import TypedDict

from .color import Color


class MiniDisplayNumberDict(TypedDict):
    """minidisplaynumber dict"""

    num: int
    duration: int
    color: list[int]


@dataclass
class MiniDisplayNumber:
    """MiniDisplayNumber class."""

    number: int
    duration: timedelta
    color: Color

    def to_dict(self) -> MiniDisplayNumberDict:
        """Convert MiniDisplayNumber to MiniDisplayNumberDict."""
        return {
            "num": self.number,
            "duration": int(self.duration.total_seconds()),
            "color": self.color.to_list(),
        }

    @staticmethod
    def from_dict(mdn_dict: MiniDisplayNumberDict) -> "MiniDisplayNumber":
        """Convert MiniDisplayNumberDict to MiniDisplayNumber."""
        return MiniDisplayNumber(
            mdn_dict["num"],
            timedelta(seconds=mdn_dict["duration"]),
            Color.from_list(mdn_dict["color"]),
        )
