# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  decorator_mastery.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: asulon <asulon@student.42nice.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/30 01:56:36 by asulon          #+#    #+#               #
#  Updated: 2026/04/30 02:00:26 by asulon          ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Callable, Any
from functools import wraps


def spell_timer(func: Callable) -> Callable:
    """
• Create a decorator factory that validates power levels
• Applied on a standalone function whose first argument is power.
• If power is valid (>= min_power), execute the function normally
• If invalid, return "Insufficient power for this spell"
• Use functools.wraps properly
"""


def power_validator(min_power: int) -> Callable:
    """
• Create a decorator that retries failed spells
• If function raises an exception, retry up to max_attempts times
• Print "Spell failed, retrying... (attempt n/max_attempts)"
• If all attempts fail, return "Spell casting failed after max_attempts attempts"
• If one attempt succeeds, return its result normally
"""


def retry_spell(max_attempts: int) -> Callable:
    """
• Create a decorator that measures function execution time
• Print "Casting function_name..." before execution
• Print "Spell completed in X.XXX seconds" after execution (3 decimal places)
• Use functools.wraps to preserve original function metadata
• Return the original function’s result
"""


class MageGuild:
    """
• validate_mage_name(name) - Static method that checks if name is valid
• Name is valid if it’s at least 3 characters and contains only letters/spaces
• cast_spell(self, spell_name, power) - Instance method
• Should use the power_validator decorator with min_power=10
• When power is valid, return "Successfully cast spell_name with <power> power"
• Otherwise return "Insufficient power for this spell"s
"""
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main() -> None:
    pass


if __name__ == "__main__":
    main()
