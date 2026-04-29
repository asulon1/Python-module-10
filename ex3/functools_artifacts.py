# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/29 16:01:46 by asulon          #+#    #+#               #
#  Updated: 2026/04/29 16:25:12 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Callable
from functools import reduce
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if len(spells) < 1:
        return 0

    match operation:
        case "add":
            return reduce(lambda x, y: add(x, y), spells)
        case "multiply":
            return reduce(lambda x, y: mul(x, y), spells)
        case "max":
            return reduce(max, spells)
        case "min":
            return reduce(min, spells)
        case _:
            raise ValueError("Error: Unknown operator")


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable]:
    """
• Take a base enchantment function with signature (power: int, element: str, target:
str) -> str
• Use functools.partial to create 3 specialized versions
• Each version pre-filling power=50 and the element
"""


def memoized_fibonacci(n: int) -> int:
    """
• Use functools.lru_cache decorator for memoization
• Implement fibonacci sequence calculation
• Function should return the nth Fibonacci number
• The cache should improve performance for repeated calls
• Return the nth fibonacci number
"""


def spell_dispatcher() -> Callable[[Any], str]:
    """
• Use decorator functools.singledispatch to create a spell system
• The base function receives Any and handles unknown spell type
• Handle different types: int (damage spell), str (enchantment), list (multi-cast)
• Return the dispatcher function
• Each type should have appropriate spell behavior
"""


def main() -> None:
    print("=== Spell Reducer ===")
    int_tab = [2, 5, 8, 3, 6]
    operations = ["add", "multiply", "max", "min", "toto"]
    for operator in operations:
        try:
            print(spell_reducer(int_tab, operator))
        except ValueError as error:
            print(error)


if __name__ == "__main__":
    main()
