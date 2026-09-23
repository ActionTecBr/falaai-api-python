from enum import StrEnum


class ParticipantRole(StrEnum):
    AGENT = "agent"
    BOT = "bot"
    CLIENT = "client"

    def __str__(self) -> str:
        return str(self.value)
