"""
module bedrock.dialects.sqldialect

Contains the SqlDialect enum for supported SQL dialects.
"""

from enum import auto, StrEnum, unique


@unique
class SqlDialect(StrEnum):
    """Enum for supported SQL dialects."""

    SQLITE = auto()
    POSTGRES = auto()
