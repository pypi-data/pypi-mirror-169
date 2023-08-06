from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_boolean_array import AbstractBooleanArray
from resqml22.abstract_integer_array import AbstractIntegerArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class BooleanArrayFromIndexArray(AbstractBooleanArray):
    """An array of Boolean values defined by specifying explicitly which
    indices in the array are either true or false.

    This class is used to represent very sparse true or false data.

    :ivar count: Total number of Boolean elements in the array. This
        number is different from the number of indices used to represent
        the array.
    :ivar indices: Array of integer indices. BUSINESS RULE: Must be non-
        negative.
    :ivar index_is_true: Indicates whether the specified elements are
        true or false.
    :ivar count_per_value:
    """
    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "min_inclusive": 1,
        }
    )
    indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "Indices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    index_is_true: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IndexIsTrue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    count_per_value: int = field(
        default=1,
        metadata={
            "name": "CountPerValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
