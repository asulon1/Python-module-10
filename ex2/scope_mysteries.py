# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  scope_mysteries.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/29 02:07:54 by asulon          #+#    #+#               #
#  Updated: 2026/05/01 11:42:30 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable, Any


def mage_counter() -> Callable[..., int]:
    count = 0

    def wrapper() -> int:
        nonlocal count
        count += 1
        return count

    return wrapper


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    return lambda item: f"{enchantment_type.capitalize()} {item.capitalize()}"


def memory_vault() -> dict[str, Callable[..., Any]]:
    """
• Return a dict with ’store’ and ’recall’ functions
• ’store’ function: takes (key, value) and stores the memory
• ’recall’ function: takes (key) and returns stored value or "Memory not found"
• Use closure to maintain private memory storage
    """
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("=== Mage Counter ===")

    a = mage_counter()
    b = mage_counter()
    print(f"a 1st call: {a()}")
    print(f"a 2nd call: {a()}")
    print(f"b 1st call: {b()}")
    print(f"a 3rd call: {a()}")
    print(f"b 2nd call: {b()}")

    print("\n=== Spell Accumulator ===")
    acc = spell_accumulator(3)
    print(f"init value: {acc(0)}")
    print(f"plus 10: {acc(10)}")
    print(f"plus 20: {acc(20)}")
    print(f"plus 30: {acc(30)}")

    print("\n=== Enchantment Factory ===")
    ice_factory = enchantment_factory("Ice")
    shadow_factory = enchantment_factory("shadow")
    print(f"Enchant sword with Ice: {ice_factory('sword')}")
    print(f"Enchant wand with shadow: {shadow_factory('wand')}")

    print("\n=== Memory Vault ===")
    vault = memory_vault()
    print("Store book : toto / wand : tata / rock : 1\n")
    vault["store"]("book", "toto")
    vault["store"]("wand", "tata")
    vault["store"]("rock", 1)

    print("Recall stored data :")
    print(f" - Recall book: {vault['recall']('book')}")
    print(f" - Recall wand: {vault['recall']('wand')}")
    print(f" - Recall rock: {vault['recall']('rock')}")
    print(f" - unknown key: {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
