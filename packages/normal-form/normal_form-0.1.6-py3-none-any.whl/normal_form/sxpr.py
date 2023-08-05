#!/usr/bin/env python3.8
"""Functions for working with s-expressions.

s-expressions are inspired from Lisp.
"""
# Imports from standard library.
import functools as ft
from dataclasses import dataclass
from typing import Callable, Generic, Tuple, TypeVar

# Imports from third-party modules.
from colorama import Fore, Style
from loguru import logger


# Type variables and aliases
Src = TypeVar('Src', covariant=True)
Trgt = TypeVar('Trgt', covariant=True)


@dataclass
class Sxpr(Generic[Src, Trgt]):
    """Define generic S-expression."""

    op: Callable[[Trgt, Src], Trgt]  # pylint: disable=invalid-name
    terms: Tuple[Src, ...]
    init: Trgt

    def reduce(self) -> Trgt:
        """Use ft.reduce to evaluate the s-expression.

        Example:
           (+, (1 2 3 4), 0) will evaluate to ((((0 + 1) + 2) + 3) + 4).
        """
        return ft.reduce(self.op, self.terms, self.init)


class SatSxpr(Sxpr[Src, bool]):  # pylint: disable=too-few-public-methods
    """A subclass of Sxpr[--, bool].

    Args:
       op (:obj:`Callable[[bool, Src], bool]`): This can only be one of two options --
          either `sat_and` or `sat_or`.
       terms (:obj:`Tuple[Src, ...]`): a tuple of terms.

    Returns:
       Computes `init` value based on `op`. Then calls the `__init__` method of `Sxpr`.
    """
    def __init__(self, op: Callable[[bool, Src], bool], terms: Tuple[Src, ...]):
        init: bool
        if op.__name__ in ('sat_and', 'and_'):
            init = True
        elif op.__name__ in ('sat_or', 'or_'):
            init = False
        else:
            raise ValueError(f'Unknown operation {op.__name__ = } encountered')
        super().__init__(op, terms, init)

    def __repr__(self) -> str:  # pragma: no cover
        """Use for pretty-printing an S-expression."""
        if self.op.__name__ in ('sat_and', 'and'):
            symb: str = ' ∧ '
            color: str = Fore.RED
        elif self.op.__name__ in ('sat_or', 'or'):
            symb = ' ∨ '
            color = Fore.GREEN
        else:
            symb = ' ? '
            color = ''
            logger.warning(f'Unknown operation {self.op.__name__ = } encountered')

        reset: str = Style.RESET_ALL
        colored_symbol: str = color + symb + reset
        bracket: Tuple[str, str] = (color + "[" + reset, color + "]" + reset)

        if not self.terms:
            return bracket[0] + colored_symbol.join(map(repr, [self.init])) + bracket[1]
        return bracket[0] + colored_symbol.join(map(repr, self.terms)) + bracket[1]


AtomicSxpr = SatSxpr[bool]


if __name__ == "__main__":  # pragma: no cover
    from time import time

    # conf.logger.remove()
    with logger.catch(message="Something unexpected happened ..."):
        time0 = time()
