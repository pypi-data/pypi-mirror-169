from __future__ import annotations
from dataclasses import dataclass
from resqml22.abstract_feature import AbstractFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Model(AbstractFeature):
    """The explicit description of the relationships between geologic features,
    such as rock features (e.g. stratigraphic units, geobodies, phase unit) and
    boundary features (e.g., genetic, tectonic, and fluid boundaries).

    In general, this concept is usually called an "earth model", but it
    is not called that in RESQML. In RESQML, model is not to be confused
    with the concept of earth model organization interpretation.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"
