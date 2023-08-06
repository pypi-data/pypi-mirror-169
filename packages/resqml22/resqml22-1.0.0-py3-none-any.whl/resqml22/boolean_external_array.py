from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_boolean_array import AbstractBooleanArray
from resqml22.external_data_array import ExternalDataArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class BooleanExternalArray(AbstractBooleanArray):
    """Array of Boolean values provided explicitly by an HDF5 dataset.

    This text needs to be altered to say that nulls are not allowed in
    the underlying implementation

    :ivar count_per_value:
    :ivar values: Reference to an HDF5 array of values.
    """
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    values: Optional[ExternalDataArray] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
