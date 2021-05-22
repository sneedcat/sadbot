"""Compliment bot command"""

import random

from typing import Optional

from sadbot.commands.interface import CommandsInterface
from sadbot.message import Message


class ComplimentBotCommand(CommandsInterface):
    """This is the compliment bot command class"""

    def __init__(self, con: str):
        self.con = con

    def get_regex(self) -> str:
        """Returns the regex for matching compliments"""
        return r"(good bot|based bot)"

    def get_reply(self, message: Optional[Message] = None) -> Optional[str]:
        """Gets a reply for when the bot receives a compliment"""
        compliment_replies = [
            "t-thwanks s-senpaii *starts twerking*",
            "at your service, sir",
            "thank youu!!",
            "good human",
        ]
        return random.choice(compliment_replies)
