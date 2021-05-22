"""Roll bot command"""

import random

from typing import Optional

from sadbot.commands.interface import CommandsInterface
from sadbot.message import Message


class RollBotCommand(CommandsInterface):
    """This is the roll bot command class"""

    def __init__(self, con: str):
        self.con = con

    def get_regex(self) -> str:
        """Returns the regex for matching the roll command"""
        return r"^(.roll)$"

    def get_reply(self, message: Optional[Message] = None) -> Optional[str]:
        """Rolls a number"""
        return str(random.randint(0, 9))
