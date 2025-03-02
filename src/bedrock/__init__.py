"""
module bedrock

Contains all submodules that make up sql-bedrock as well as the definition
of the command-line interface.
"""

import importlib.metadata


__all__ = ["dialects", "expressions", "parsing", "__version__"]

from . import dialects
from . import expressions
from . import parsing


# the version is maintained for us by poetry. we can access it by
# introspecting the package after installation
__version__ = importlib.metadata.version("sql-bedrock")
