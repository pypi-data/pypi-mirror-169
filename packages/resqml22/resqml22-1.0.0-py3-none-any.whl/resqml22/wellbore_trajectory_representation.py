from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_parametric_line_geometry import AbstractParametricLineGeometry
from resqml22.abstract_representation import AbstractRepresentation
from resqml22.data_object_reference import DataObjectReference
from resqml22.md_domain import MdDomain
from resqml22.md_interval import MdInterval
from resqml22.wellbore_trajectory_parent_intersection import WellboreTrajectoryParentIntersection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WellboreTrajectoryRepresentation(AbstractRepresentation):
    """Representation of a wellbore trajectory.

    For this particular representation a WITSML v2 Wellbore is
    considered as a RESQML Technical Feature, meaning that the WITSML v2
    Wellbore can be used as the represented data object for this
    representation.

    :ivar md_interval: The interval which represents the minimum and
        maximum values of measured depth for the trajectory. BUSINESS
        RULE: For purposes of the trajectory the MdDatum within the
        MdInterval is mandatory. BUSINESS RULE: The MdMin must be less
        than the MdMax within the MdInterval
    :ivar custom_unit_dictionary: If the unit of measure of the
        MdInterval is an extended value, this is a reference to an
        object containing the custom unit dictionary.
    :ivar md_domain: Indicates if the MD is either in "driller" domain
        or "logger" domain.
    :ivar witsml_trajectory: Pointer to the WITSML trajectory that is
        contained in the referenced wellbore. (For information about
        WITSML well and wellbore references, see the definition for
        RESQML technical feature, WellboreFeature).
    :ivar parent_intersection:
    :ivar geometry: Explicit geometry is not required for vertical wells
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
        }
    )
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
        }
    )
    md_domain: Optional[MdDomain] = field(
        default=None,
        metadata={
            "name": "MdDomain",
            "type": "Element",
        }
    )
    witsml_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlTrajectory",
            "type": "Element",
        }
    )
    parent_intersection: Optional[WellboreTrajectoryParentIntersection] = field(
        default=None,
        metadata={
            "name": "ParentIntersection",
            "type": "Element",
        }
    )
    geometry: Optional[AbstractParametricLineGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        }
    )
