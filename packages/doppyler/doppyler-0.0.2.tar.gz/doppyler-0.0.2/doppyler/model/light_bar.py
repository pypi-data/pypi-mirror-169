"""Models for setting light bar effects."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import timedelta
from typing import Any, TypedDict

from .color import Color


class LightbarDisplayDict(TypedDict):
    """lightbardisplay dict."""

    colors: list[list[int]]
    duration: int
    speed: int
    attributes: dict[str, Any]


@dataclass
class LightbarDisplayEffect:
    """LightbarDisplayEffect class."""

    colors: list[Color]
    duration: timedelta
    speed: int
    attributes: dict[str, Any]

    def to_dict(self) -> LightbarDisplayDict:
        """Convert LightbarDisplayEffect to LightbarDisplayDict."""
        return {
            "colors": [color.to_list() for color in self.colors],
            "duration": int(self.duration.total_seconds()),
            "speed": self.speed,
            "attributes": self.attributes,
        }

    @staticmethod
    def from_dict(lgt_dict: LightbarDisplayDict) -> "LightbarDisplayEffect":
        """Convert LightbarDisplayDict to LightbarDisplayEffect."""
        return LightbarDisplayEffect(
            [Color.from_list(color) for color in lgt_dict["colors"]],
            timedelta(seconds=lgt_dict["duration"]),
            lgt_dict["speed"],
            lgt_dict["attributes"],
        )
