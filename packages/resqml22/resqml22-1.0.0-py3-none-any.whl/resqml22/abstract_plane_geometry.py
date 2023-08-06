from __future__ import annotations
from dataclasses import dataclass
from resqml22.abstract_geometry import AbstractGeometry

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractPlaneGeometry(AbstractGeometry):
    """
    The abstract class for all geometric values defined by planes.
    """
