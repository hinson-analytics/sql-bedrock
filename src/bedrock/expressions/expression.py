"""
module bedrock.expressions.expression

Contains the definition of the Expression class which is the abstract
parent of all SQL expressions.
"""

from abc import ABCMeta


class Expression(metaclass=ABCMeta):
    # pylint: disable=missing-class-docstring, too-few-public-methods

    ...
