from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class WitsmlWellWellbore:
    """
    Reference to the WITSML wellbore that this wellbore feature is based on.
    """
    witsml_well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlWell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    witsml_wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlWellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
