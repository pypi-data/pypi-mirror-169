from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.abstract_feature_interpretation import AbstractFeatureInterpretation
from resqml22.depositional_environment_kind import DepositionalEnvironmentKind
from resqml22.depositional_facies_kind import DepositionalFaciesKind
from resqml22.geologic_unit_material_emplacement import GeologicUnitMaterialEmplacement
from resqml22.lithology_kind import LithologyKind
from resqml22.shape3d import Shape3D

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeologicUnitInterpretation(AbstractFeatureInterpretation):
    """The main class for data describing an opinion of an originally
    continuous rock volume individualized in view of some characteristic
    property (e.g., physical, chemical, temporal) defined by
    GeologicUnitComposition and/or GeologicUnitMaterialImplacement, which can
    have a 3D defined shape.

    BUSINESS RULE: The data object reference (of type "interprets") must
    reference only a rock volume feature. In an earth model, a
    geological unit interrupted by faults may consist of several
    disconnected rock volumes.

    :ivar geologic_unit_composition:
    :ivar geologic_unit_material_emplacement: Attribute specifying
        whether the GeologicalUnitIntepretation is intrusive or not.
    :ivar geologic_unit3d_shape: 3D shape of the geologic unit.
    :ivar depositional_environment:
    :ivar depositional_facies:
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    geologic_unit_composition: Optional[Union[LithologyKind, str]] = field(
        default=None,
        metadata={
            "name": "GeologicUnitComposition",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    geologic_unit_material_emplacement: Optional[GeologicUnitMaterialEmplacement] = field(
        default=None,
        metadata={
            "name": "GeologicUnitMaterialEmplacement",
            "type": "Element",
        }
    )
    geologic_unit3d_shape: Optional[Union[Shape3D, str]] = field(
        default=None,
        metadata={
            "name": "GeologicUnit3dShape",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    depositional_environment: Optional[Union[DepositionalEnvironmentKind, str]] = field(
        default=None,
        metadata={
            "name": "DepositionalEnvironment",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    depositional_facies: Optional[Union[DepositionalFaciesKind, str]] = field(
        default=None,
        metadata={
            "name": "DepositionalFacies",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
