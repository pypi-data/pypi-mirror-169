from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_contact_interpretation_part import AbstractContactInterpretationPart
from resqml22.abstract_feature_interpretation import AbstractFeatureInterpretation

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractOrganizationInterpretation(AbstractFeatureInterpretation):
    """The main class used to group features into meaningful units as a step in
    working towards the goal of building an earth model (the organization of
    all other organizations in RESQML). An organization interpretation:

    - Is typically comprised of one stack of its contained elements.
    - May be built on other organization interpretations.
    Typically contains:
    - contacts between the elements of this stack among themselves.
    - contacts between the stack elements and other organization elements.
    """
    contact_interpretation: List[AbstractContactInterpretationPart] = field(
        default_factory=list,
        metadata={
            "name": "ContactInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
