from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_seismic_survey_feature import AbstractSeismicSurveyFeature
from resqml22.integer_lattice_array import IntegerLatticeArray
from resqml22.seismic_lattice_set_feature import SeismicLatticeSetFeature

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SeismicLatticeFeature(AbstractSeismicSurveyFeature):
    """Defined by two lateral ordered dimensions: inline (lateral), crossline
    (lateral and orthogonal to the inline dimension), which are fixed.

    To specify its location, a seismic feature can be associated with
    the seismic coordinates of the points of a representation.
    Represented by a 2D grid representation.

    :ivar crossline_labels: The labels (as they would be found in SEGY
        trace headers for example) of the crosslines of the 3D seismic
        survey. BUSINESS RULE: Count of this array must be the same as
        the count of nodes in the slowest axis of the associated grid 2D
        representations.
    :ivar inline_labels: The labels (as they would be found in SEGY
        trace headers for example) of the inlines of the 3D seismic
        survey. BUSINESS RULE: Count of this array must be the same as
        the count of nodes in the fastest axis of the associated grid 2D
        representations.
    :ivar is_part_of:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    crossline_labels: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "CrosslineLabels",
            "type": "Element",
        }
    )
    inline_labels: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "InlineLabels",
            "type": "Element",
        }
    )
    is_part_of: Optional[SeismicLatticeSetFeature] = field(
        default=None,
        metadata={
            "name": "IsPartOf",
            "type": "Element",
        }
    )
