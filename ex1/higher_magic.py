# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  higher_magic.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/29 01:10:08 by asulon          #+#    #+#               #
#  Updated: 2026/04/29 02:05:46 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable


def spell_combiner(spell1: Callable[[str, int], str],
                   spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], tuple[str, str]]:
    return lambda target, power: (spell1(target, power), spell2(target, power))


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    return lambda target, power: base_spell(target, power * multiplier)


def conditional_caster(condition: Callable[[int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:
    return lambda target, power: (
        spell(target, power)
        if condition(power)
        else "Spell fizzled"
    )


def spell_sequence(spells: list[Callable[[str, int], str]]
                   ) -> Callable[[str, int], list[str]]:

    return lambda target, power: list(
        map(lambda spell: spell(target, power), spells)
    )


def main() -> None:
    def fireball(target: str, power: int) -> str:
        return f"Fireball deals {power} DMG to {target}"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {power} HP to {target}"

    def lightning(target: str, power: int) -> str:
        return f"Lightning deals {power} DMG to {target}"

    def freeze(target: str, power: int) -> str:
        return f"Freeze deals {power} DMG to {target}"

    def is_valid(power: int) -> bool:
        return power > 10

    print("=== Spell Combiner ===")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 4))

    print("\n=== Spell Amplifier ===")
    mega_lightning = power_amplifier(lightning, 2)

    print(mega_lightning("Hydra", 10))

    print("\n=== Conditional Caster ===")
    conditional = conditional_caster(is_valid, heal)
    print(conditional("Rotnat", 40))
    print(conditional("Rotnat", 3))

    print("\n=== Spell Sequence ===")
    sequence = spell_sequence([fireball, heal, lightning, freeze])
    print(sequence("Rotnat", 3))


if __name__ == "__main__":
    main()
