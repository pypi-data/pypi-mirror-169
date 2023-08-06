from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_object import AbstractObject
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicColumn(AbstractObject):
    """A global interpretation of the stratigraphy, which can be made up of
    several ranks of stratigraphic unit interpretations.

    BUSINESS RULE: All stratigraphic column rank interpretations that
    make up a stratigraphic column must be ordered by age.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ranks: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Ranks",
            "type": "Element",
            "min_occurs": 1,
        }
    )
