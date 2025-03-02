"""
module bedrock.dialects.sqldialecttype

Contains the SqlDialectType enum for supported SQL dialects.
"""

from enum import auto, StrEnum, unique


@unique
class SqlDialectType(StrEnum):
    """Enum for supported SQL dialects."""

    SQLITE = auto()
    POSTGRES = auto()
