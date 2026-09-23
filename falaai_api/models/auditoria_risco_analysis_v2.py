from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auditoria_risco_analysis_v2_final_analysis import AuditoriaRiscoAnalysisV2FinalAnalysis
    from ..models.auditoria_risco_analysis_v2_frameworks import AuditoriaRiscoAnalysisV2Frameworks
    from ..models.auditoria_risco_analysis_v2_global_metrics import AuditoriaRiscoAnalysisV2GlobalMetrics


T = TypeVar("T", bound="AuditoriaRiscoAnalysisV2")


@_attrs_define
class AuditoriaRiscoAnalysisV2:
    """
    Attributes:
        global_metrics (AuditoriaRiscoAnalysisV2GlobalMetrics | Unset): Global metrics
        final_analysis (AuditoriaRiscoAnalysisV2FinalAnalysis | Unset): Final analysis
        frameworks (AuditoriaRiscoAnalysisV2Frameworks | Unset): Frameworks (COPC/ISO/Kirkpatrick/CES)
    """

    global_metrics: AuditoriaRiscoAnalysisV2GlobalMetrics | Unset = UNSET
    final_analysis: AuditoriaRiscoAnalysisV2FinalAnalysis | Unset = UNSET
    frameworks: AuditoriaRiscoAnalysisV2Frameworks | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        global_metrics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.global_metrics, Unset):
            global_metrics = self.global_metrics.to_dict()

        final_analysis: dict[str, Any] | Unset = UNSET
        if not isinstance(self.final_analysis, Unset):
            final_analysis = self.final_analysis.to_dict()

        frameworks: dict[str, Any] | Unset = UNSET
        if not isinstance(self.frameworks, Unset):
            frameworks = self.frameworks.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if global_metrics is not UNSET:
            field_dict["global_metrics"] = global_metrics
        if final_analysis is not UNSET:
            field_dict["final_analysis"] = final_analysis
        if frameworks is not UNSET:
            field_dict["frameworks"] = frameworks

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auditoria_risco_analysis_v2_final_analysis import (
            AuditoriaRiscoAnalysisV2FinalAnalysis,  # noqa: PLC0415
        )
        from ..models.auditoria_risco_analysis_v2_frameworks import AuditoriaRiscoAnalysisV2Frameworks  # noqa: PLC0415
        from ..models.auditoria_risco_analysis_v2_global_metrics import (
            AuditoriaRiscoAnalysisV2GlobalMetrics,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _global_metrics = d.pop("global_metrics", UNSET)
        global_metrics: AuditoriaRiscoAnalysisV2GlobalMetrics | Unset
        if isinstance(_global_metrics, Unset):
            global_metrics = UNSET
        else:
            global_metrics = AuditoriaRiscoAnalysisV2GlobalMetrics.from_dict(_global_metrics)

        _final_analysis = d.pop("final_analysis", UNSET)
        final_analysis: AuditoriaRiscoAnalysisV2FinalAnalysis | Unset
        if isinstance(_final_analysis, Unset):
            final_analysis = UNSET
        else:
            final_analysis = AuditoriaRiscoAnalysisV2FinalAnalysis.from_dict(_final_analysis)

        _frameworks = d.pop("frameworks", UNSET)
        frameworks: AuditoriaRiscoAnalysisV2Frameworks | Unset
        if isinstance(_frameworks, Unset):
            frameworks = UNSET
        else:
            frameworks = AuditoriaRiscoAnalysisV2Frameworks.from_dict(_frameworks)

        auditoria_risco_analysis_v2 = cls(
            global_metrics=global_metrics,
            final_analysis=final_analysis,
            frameworks=frameworks,
        )

        return auditoria_risco_analysis_v2
