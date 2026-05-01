# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42.fr>             +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/30 01:56:36 by asulon          #+#    #+#               #
#  Updated: 2026/05/01 12:00:54 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable, Any
from functools import wraps
import time


def spell_timer(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: str, **kwargs: int) -> str:
        print(f"Casting {func.__name__} ...")
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} second")
        return res
    return wrapper


def power_validator(min_power: int) -> Callable[[Any], Any]:
    def validator(func: Callable[..., str]) -> Any:
        @wraps(func)
        def wrapper(*args: str, **kwargs: int) -> Callable[[Any], Any]:
            power: int
            if isinstance(args[2], int):
                power = args[2]
            elif isinstance(args[1], int):
                power = args[1]

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return validator


def retry_spell(max_attempts: int) -> Callable[[Any], Any]:
    def retry(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: str, **kwargs: int) -> Any:
            attemp = 1
            while attemp < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying ... (attemp {attemp}/3)")
                    attemp += 1
            return (f"Spell casting failed after {max_attempts} attempts")
        return wrapper
    return retry


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (len(name) >= 3 and
                all(letter.isalpha() or letter.isspace() for letter in name))

    @power_validator(5)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name.capitalize()} "
                f"with {power} power")


def main() -> None:
    @spell_timer
    def fireball() -> str:
        time.sleep(1)
        return "Fireball cast!"

    @retry_spell(5)
    def lightning(failure: bool) -> str:
        if failure:
            raise Exception("Spell failed")
        else:
            return "lightning strikes"

    print("=== Spell timer ===")
    print(f"Result {fireball()}\n")

    print("=== Retry spell ===")
    print(f"{lightning(True)}\n")
    print("=== MageGuild ===")
    mageguild = MageGuild()
    print("Testing mage name 'Icien': "
          f"{mageguild.validate_mage_name('Icien')}")
    print("Testing mage name 'Ici en': "
          f"{mageguild.validate_mage_name('Ici en')}")
    print("Testing mage name 'Ici5en': "
          f"{mageguild.validate_mage_name('Ici5en')}")
    print(f"Testing mage name 'I': {mageguild.validate_mage_name('I')}")

    print("Testing Lightning with 15 power:\n "
          f"{mageguild.cast_spell('lightning', 15)}")
    print("Testing Fireball with 3 power:\n "
          f"{mageguild.cast_spell('Fireball', 3)}")


if __name__ == "__main__":
    main()
