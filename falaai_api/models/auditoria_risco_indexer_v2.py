from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_indexer_v2_suggested_terms_for_bank_item import (
        AuditoriaRiscoIndexerV2SuggestedTermsForBankItem,
    )


T = TypeVar("T", bound="AuditoriaRiscoIndexerV2")


@_attrs_define
class AuditoriaRiscoIndexerV2:
    """
    Attributes:
        suggested_terms_for_bank (list[AuditoriaRiscoIndexerV2SuggestedTermsForBankItem] | Unset): Suggested terms for
            bank
    """

    suggested_terms_for_bank: list[AuditoriaRiscoIndexerV2SuggestedTermsForBankItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        suggested_terms_for_bank: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suggested_terms_for_bank, Unset):
            suggested_terms_for_bank = []
            for suggested_terms_for_bank_item_data in self.suggested_terms_for_bank:
                suggested_terms_for_bank_item = suggested_terms_for_bank_item_data.to_dict()
                suggested_terms_for_bank.append(suggested_terms_for_bank_item)

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if suggested_terms_for_bank is not UNSET:
            field_dict["suggested_terms_for_bank"] = suggested_terms_for_bank

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_indexer_v2_suggested_terms_for_bank_item import (
            AuditoriaRiscoIndexerV2SuggestedTermsForBankItem,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _suggested_terms_for_bank = d.pop("suggested_terms_for_bank", UNSET)
        suggested_terms_for_bank: list[AuditoriaRiscoIndexerV2SuggestedTermsForBankItem] | Unset = UNSET
        if _suggested_terms_for_bank is not UNSET:
            suggested_terms_for_bank = []
            for suggested_terms_for_bank_item_data in _suggested_terms_for_bank:
                suggested_terms_for_bank_item = AuditoriaRiscoIndexerV2SuggestedTermsForBankItem.from_dict(
                    suggested_terms_for_bank_item_data
                )

                suggested_terms_for_bank.append(suggested_terms_for_bank_item)

        auditoria_risco_indexer_v2 = cls(
            suggested_terms_for_bank=suggested_terms_for_bank,
        )

        return auditoria_risco_indexer_v2
