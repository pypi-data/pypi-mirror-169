"""Utility functions for data structure handling."""

__all__ = ["ParameterList", "AzElData", "ParameterMapping"]

from dataclasses import dataclass
from typing import Any, Callable, Hashable, Iterable

import numpy as np


class ParameterList(list):
    """List, specialized in parameter storing.

    Parameters
    ----------
    value
        Iterable object to be converted to ParameterList.

    Examples
    --------
    >>> neclib.utils.ParameterList([0, 0])
    ParameterList([0, 0])
    >>> neclib.utils.ParameterList(range(5))
    ParameterList([0, 1, 2, 3, 4])

    """

    def __init__(self, value: Iterable = []):
        super().__init__(value)

    @classmethod
    def new(cls, length: int, initvalue: Any = np.nan) -> "ParameterList":
        """Create new ParameterList instance filled with initial value.

        Parameters
        ----------
        length
            Length of ``ParameterList`` to be created.
        initvalue
            Initial value to fill the ``ParameterList``.

        Examples
        --------
        >>> neclib.utils.ParameterList.new(3, 100)
        ParameterList([100, 100, 100])

        """
        return cls([initvalue for _ in range(length)])

    def push(self, value: Any) -> None:
        """Append new value to ParameterList, preserving its length.

        Parameters
        ----------
        value
            Value to be appended.

        Examples
        --------
        >>> param = neclib.utils.ParameterList([1, 2])
        >>> param.push(5)
        >>> param
        ParameterList([2, 5])

        """
        self.append(value)
        self.pop(0)

    def copy(self):
        """Return copied ParameterList.

        Examples
        --------
        >>> param = neclib.utils.ParameterList([1, 2])
        >>> param.copy()
        ParameterList([1, 2])

        """
        return self.__class__(super().copy())

    def map(self, func: Callable) -> "ParameterList":
        """Map a function to every element in the ParameterList.

        Parameters
        ----------
        func
            Function to apply.

        Examples
        --------
        >>> param = neclib.utils.ParameterList([1, 2])
        >>> param.map(lambda x: 10 * x)
        ParameterList([10, 20])

        """
        return self.__class__(list(map(func, self)))

    def __repr__(self) -> str:
        return self.__class__.__name__ + "(" + super().__repr__() + ")"


@dataclass
class AzElData:
    az: Any = None
    """Parameter related to azimuth axis."""
    el: Any = None
    """Parameter related to elevation axis."""


class ParameterMapping(dict):
    """Dict, with attribute access to parameter supported.

    Parameter mapping, supports both dict-key syntax and attribute access syntax. Dict
    methods are fully supported.

    Examples
    --------
    >>> param = neclib.utils.ParameterMapping(a=1, b=2)
    >>> param["a"]
    1
    >>> param.a
    1
    >>> neclib.utils.ParameterMapping({"a": 1, "b": 2}) == param
    True

    """

    def __repr__(self) -> str:
        return self.__class__.__name__ + "(" + super().__repr__() + ")"

    def __getattr__(self, name: Hashable) -> Any:
        try:
            return self[name]
        except KeyError as e:  # Raise AttributeError instead of KeyError.
            raise AttributeError(f"No attribute '{name}'") from e

    def copy(self):
        """Return copied ParameterMapping.

        Examples
        --------
        >>> param = neclib.utils.ParameterMapping(a=1, b=2)
        >>> param.copy()
        ParameterMapping({'a': 1, 'b': 2})

        """
        return self.__class__(super().copy())
