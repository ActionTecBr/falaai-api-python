from enum import StrEnum


class AuditoriaRiscoRequestCallDirectionType0(StrEnum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

    def __str__(self) -> str:
        return str(self.value)
