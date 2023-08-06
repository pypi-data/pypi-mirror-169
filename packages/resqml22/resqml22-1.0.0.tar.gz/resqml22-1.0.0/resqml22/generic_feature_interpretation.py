from __future__ import annotations
from dataclasses import dataclass
from resqml22.abstract_feature_interpretation import AbstractFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GenericFeatureInterpretation(AbstractFeatureInterpretation):
    """An interpretation of a feature that is not specialized.

    For example, use it when the specialized type of the associated
    feature is not known. For example, to set up a
    StructuralOrganizationInterpretation you must reference the
    interpretations of each feature you want to include. These features
    must include FrontierFeatures which have no interpretations because
    they are technical features. For consistency of design of the
    StructuralOrganizationInterpretation, create a
    GenericFeatureInterpretation for each FrontierFeature.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
