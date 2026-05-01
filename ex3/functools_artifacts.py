# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  functools_artifacts.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/29 16:01:46 by asulon          #+#    #+#               #
#  Updated: 2026/05/01 11:48:04 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Callable
from functools import reduce, partial, lru_cache, singledispatch
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
                      ) -> dict[str, Callable[[Any], Any]]:
    return {
        "fire": partial(base_enchantment, 5, "fire"),
        "water": partial(base_enchantment, 15, "water"),
        "light": partial(base_enchantment, 50, "light"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("number must be >= 0")
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(args: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register
    def _(power: int) -> str:
        return f"Damage spell: {power} damage"

    @dispatcher.register
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register
    def _(spells: list[Any]) -> str:
        return f"Multi-cast: {len(spells)} spells"

    return dispatcher


def main() -> None:
    print("=== Spell Reducer ===")
    int_tab = [2, 5, 8, 3, 6]
    operations = ["add", "multiply", "max", "min", "toto"]
    for operator in operations:
        try:
            print(spell_reducer(int_tab, operator))
        except ValueError as error:
            print(error)

    print("\n=== Partial enchenter ===")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return (f"{element.capitalize()} enchantment "
                f"deals {power} DMG to {target.capitalize()}")

    base = partial_enchanter(base_enchantment)
    print(base["fire"]('dragon'))
    print(base["water"]('fire elemental'))
    print(base["light"]('demon'))

    print("\n=== Memoized fibonacci ===")
    print("Fib(0):", memoized_fibonacci(0))
    print("Fib(1):", memoized_fibonacci(1))
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))
    try:
        memoized_fibonacci(-1)
    except Exception as e:
        print(f"Fib(-1): {e}")
    print("Lru.cache Info:", memoized_fibonacci.cache_info())

    print("\n=== Spell dispatcher ===")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("arcane blast"))
    print(dispatcher(["te", 1, "fr"]))
    print(dispatcher(42.42))


if __name__ == "__main__":
    main()
