from __future__ import annotations
from dataclasses import dataclass
from resqml22.abstract_seismic_line_feature import AbstractSeismicLineFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ShotPointLineFeature(AbstractSeismicLineFeature):
    """
    Location of a single line of shot points in a 2D seismic acquisition.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
