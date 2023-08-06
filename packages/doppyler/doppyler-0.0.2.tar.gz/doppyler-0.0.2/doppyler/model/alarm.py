"""Models for alarm."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import time
from enum import Enum, IntEnum
from typing import TypedDict

from .color import Color, ColorDict


class RepeatDayOfWeek(str, Enum):
    """Day of the week to repeat alarm enum."""

    MONDAY = "Mo"
    TUESDAY = "Tu"
    WEDNESDAY = "We"
    THURSDAY = "Th"
    FRIDAY = "Fr"
    SATURDAY = "Sa"
    SUNDAY = "Su"


class AlarmSource(IntEnum):
    """Alarm source enum."""

    SYSTEM = 0
    APP = 1
    ALEXA = 2


class AlarmDict(TypedDict):
    """Representation of an alarm."""

    id: int
    name: str
    time_hr: int
    time_min: int
    repeat: str
    color: ColorDict
    volume: int
    status: int
    src: int
    sound: str


@dataclass
class Alarm:
    """Alarm class."""

    id: int
    name: str
    alarm_time: time
    repeat: list[RepeatDayOfWeek]
    color: Color
    volume: int
    status: bool
    src: AlarmSource
    sound: str

    def to_dict(self) -> AlarmDict:
        """Convert Alarm to AlarmDict."""
        return {
            "id": self.id,
            "name": self.name,
            "time_hr": self.alarm_time.hour,
            "time_min": self.alarm_time.minute,
            "repeat": "".join([day_of_week.value for day_of_week in self.repeat]),
            "color": {
                "red": self.color.red,
                "green": self.color.green,
                "blue": self.color.blue,
            },
            "volume": self.volume,
            "status": int(self.status),
            "src": self.src.value,
            "sound": self.sound,
        }

    @staticmethod
    def from_dict(alarm_dict: AlarmDict) -> "Alarm":
        """Create Alarm from dict."""
        alarm_dict["repeat"] = alarm_dict["repeat"].replace("0", "")
        return Alarm(
            alarm_dict["id"],
            alarm_dict["name"],
            time(hour=alarm_dict["time_hr"], minute=alarm_dict["time_min"]),
            [
                RepeatDayOfWeek(day)
                for day in [
                    alarm_dict["repeat"][i : i + 2]
                    for i in range(0, len(alarm_dict["repeat"]), 2)
                    if alarm_dict["repeat"][i : i + 2]
                ]
            ],
            Color.from_dict(alarm_dict["color"]),
            alarm_dict["volume"],
            bool(alarm_dict["status"]),
            AlarmSource(alarm_dict["src"]),
            alarm_dict["sound"],
        )
