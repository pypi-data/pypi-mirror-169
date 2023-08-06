"""Models for main display text."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from typing import TypedDict

from .color import Color


class MainDisplayTextDict(TypedDict):
    """maindisplaytext dict"""

    text: str
    duration: int
    speed: int
    color: list[int]


@dataclass
class MainDisplayText:
    """MainDisplayText class."""

    text: str
    duration: timedelta
    speed: int
    color: Color

    def to_dict(self) -> MainDisplayTextDict:
        """Convert MainDisplayText to MainDisplayTextDict."""
        return {
            "text": self.text,
            "duration": int(self.duration.total_seconds()),
            "speed": self.speed,
            "color": self.color.to_list(),
        }

    @staticmethod
    def from_dict(mdt_dict: MainDisplayTextDict) -> "MainDisplayText":
        """Convert MainDisplayTextDict to MainDisplayText."""
        return MainDisplayText(
            mdt_dict["text"],
            timedelta(seconds=mdt_dict["duration"]),
            mdt_dict["speed"],
            Color.from_list(mdt_dict["color"]),
        )
