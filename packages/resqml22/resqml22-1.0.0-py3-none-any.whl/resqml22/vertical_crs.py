from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.abstract_object import AbstractObject
from resqml22.abstract_vertical_crs import AbstractVerticalCrs
from resqml22.length_uom import LengthUom
from resqml22.vertical_direction import VerticalDirection

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class VerticalCrs(AbstractObject):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    direction: Optional[VerticalDirection] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "required": True,
        }
    )
    abstract_vertical_crs: Optional[AbstractVerticalCrs] = field(
        default=None,
        metadata={
            "name": "AbstractVerticalCrs",
            "type": "Element",
            "required": True,
        }
    )
    uom: Optional[Union[LengthUom, str]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".*:.*",
        }
    )
