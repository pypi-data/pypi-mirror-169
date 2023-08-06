from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


class CulturalFeatureKind(Enum):
    """
    The enumeration of the possible cultural feature.
    """
    FIELDBLOCK = "fieldblock"
    LICENSES = "licenses"
    PIPELINE = "pipeline"
    PROJECT_BOUNDARIES = "project boundaries"
    MODEL_FRONTIER = "model frontier"
