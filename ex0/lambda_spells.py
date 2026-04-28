# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  lambda_spells.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/29 00:02:47 by asulon          #+#    #+#               #
#  Updated: 2026/04/29 01:09:34 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]
                    ) -> list[dict[str, Any]]:
    return sorted(artifacts,
                  key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, int | float]:
    return {"max_power": max(mages, key=lambda mage: mage["power"])["power"],
            "min_power": min(mages, key=lambda mage: mage["power"])["power"],
            "avg_power": round(
                sum(map(lambda mage: mage["power"], mages)) / len(mages),
                2,
    )}


def main() -> None:
    print("=== Sorted Artifact ===")
    artifacts = [
        {'name': 'book', 'power': 65, 'type': 'Dark'},
        {'name': 'stone', 'power': 15, 'type': 'Fire'},
        {'name': 'Wand', 'power': 100, 'type': 'Water'},
    ]
    print(artifact_sorter(artifacts))

    print("\n=== Filter Mages ===")
    mages = [{'name': 'Sora', 'power': 15, 'element': 'Fire'},
             {'name': 'Aqua', 'power': 65, 'element': 'Water'},
             {'name': 'Tera', 'power': 104, 'element': 'Earth'},]
    print(power_filter(mages, 65))

    print("\n=== Spells Transform ===")
    spells = ["Fire", "Water", "Earth", "Dark", "Lightning"]
    print(spell_transformer(spells))

    print("\n=== Mages Stats ===")
    mage_stats(mages)
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
