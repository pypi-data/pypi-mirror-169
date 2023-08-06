from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class OsduspatialLocationIntegration:
    """
    Details about an OSDU Spatial Location.

    :ivar spatial_location_coordinates_date: Date when coordinates were
        measured or retrieved.
    :ivar quantitative_accuracy_band: An approximate quantitative
        assessment of the quality of a location (accurate to &gt; 500 m
        (i.e. not very accurate)), to &lt; 1 m, etc.
    :ivar qualitative_spatial_accuracy_type: A qualitative description
        of the quality of a spatial location, e.g. unverifiable, not
        verified, basic validation.
    :ivar coordinate_quality_check_performed_by: The user who performed
        the Quality Check.
    :ivar coordinate_quality_check_date_time: The date of the Quality
        Check.
    :ivar coordinate_quality_check_remark: Freetext remarks on Quality
        Check.
    :ivar applied_operation: The audit trail of operations applied to
        the coordinates from the original state to the current state.
        The list may contain operations applied prior to ingestion as
        well as the operations applied to produce the Wgs84Coordinates.
        The text elements refer to ESRI style CRS and Transformation
        names, which may have to be translated to EPSG standard names.
    """
    class Meta:
        name = "OSDUSpatialLocationIntegration"

    spatial_location_coordinates_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "SpatialLocationCoordinatesDate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    quantitative_accuracy_band: Optional[str] = field(
        default=None,
        metadata={
            "name": "QuantitativeAccuracyBand",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    qualitative_spatial_accuracy_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "QualitativeSpatialAccuracyType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    coordinate_quality_check_performed_by: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoordinateQualityCheckPerformedBy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    coordinate_quality_check_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "CoordinateQualityCheckDateTime",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    coordinate_quality_check_remark: List[str] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateQualityCheckRemark",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 256,
        }
    )
    applied_operation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "AppliedOperation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 256,
        }
    )
