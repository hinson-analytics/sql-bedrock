"""
module bedrock.parsing.adapters.generic.parseradapter

Contains the abstract base class for SQL query parsers.
"""

from abc import ABCMeta, abstractmethod
import os
from typing import List

from ....dialects import SqlDialect
from ....expressions import Expression


class ParserAdapter(metaclass=ABCMeta):
    """
    class ParserAdapter

    Abstract base class for SQL query parsers. This class defines the interface
    that all SQL query parsers must implement in order to be used by sql-bedrock
    """

    @abstractmethod
    def parse_query(
        self: "ParserAdapter", query: str, dialect: SqlDialect
    ) -> List[Expression]:
        """
        Parse a SQL query string into an Expression object.

        Args:
            query (str): The SQL query to parse

        Returns:
            List[Expression]: A list of Expression objects representing the
                parsed query

        Raises:
            NotImplementedError: This method must be implemented by all
                subclasses
        """

    def parse_file(
        self: "ParserAdapter",
        file_path: str | bytes | os.PathLike,
        dialect: SqlDialect,
        encoding: str = "utf-8",
    ) -> List[Expression]:
        """
        Parse a SQL query from a file into an Expression object.

        Args:
            file_path (str | bytes | os.PathLike): The path to the file
                containing the SQL query to parse
            encoding (str): The encoding of the file (default is "utf-8")

        Returns:
            List[Expression]: A list of Expression objects representing the
                parsed query

        Raises:
            FileNotFoundError: If the file does not exist
            NotImplementedError: This method must be implemented by all
                subclasses
        """

        with open(file_path, "r", encoding=encoding) as query_file:
            return self.parse_query(query_file.read(), dialect=dialect)
