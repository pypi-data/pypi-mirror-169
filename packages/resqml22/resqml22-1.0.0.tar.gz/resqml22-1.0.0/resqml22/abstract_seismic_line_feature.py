from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_seismic_survey_feature import AbstractSeismicSurveyFeature
from resqml22.data_object_reference import DataObjectReference
from resqml22.string_external_array import StringExternalArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractSeismicLineFeature(AbstractSeismicSurveyFeature):
    """Location of the line used in a 2D seismic acquisition.

    Defined by one lateral dimension: trace (lateral). To specify its
    location, the seismic feature can be associated with the seismic
    coordinates of the points of a representation. Represented by a
    PolylineRepresentation.
    """
    trace_labels: Optional[StringExternalArray] = field(
        default=None,
        metadata={
            "name": "TraceLabels",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    is_part_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IsPartOf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
