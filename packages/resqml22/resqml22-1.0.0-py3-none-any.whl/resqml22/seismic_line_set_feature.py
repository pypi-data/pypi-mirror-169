from __future__ import annotations
from dataclasses import dataclass
from resqml22.abstract_seismic_survey_feature import AbstractSeismicSurveyFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SeismicLineSetFeature(AbstractSeismicSurveyFeature):
    """An unordered set of several seismic lines.

    Generally, it has no direct interpretation or representation.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
