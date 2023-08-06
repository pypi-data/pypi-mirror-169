from __future__ import annotations
from dataclasses import dataclass
from resqml22.abstract_object import AbstractObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Geocentric3DCrs(AbstractObject):
    class Meta:
        name = "Geocentric3dCrs"
