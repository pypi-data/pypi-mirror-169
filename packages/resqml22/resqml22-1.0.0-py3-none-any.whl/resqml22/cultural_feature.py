from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.abstract_technical_feature import AbstractTechnicalFeature
from resqml22.cultural_feature_kind import CulturalFeatureKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CulturalFeature(AbstractTechnicalFeature):
    """
    Identifies a frontier or boundary in the earth model that is not a
    geological feature but an arbitrary geographic/geometric surface used to
    delineate the boundary of the model.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    cultural_feature_kind: Optional[Union[CulturalFeatureKind, str]] = field(
        default=None,
        metadata={
            "name": "CulturalFeatureKind",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        }
    )
