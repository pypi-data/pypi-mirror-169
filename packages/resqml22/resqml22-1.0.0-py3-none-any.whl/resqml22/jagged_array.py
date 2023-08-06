from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_integer_array import AbstractIntegerArray
from resqml22.abstract_value_array import AbstractValueArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class JaggedArray:
    """Data storage object for an array of variable length 1D sub-arrays. The
    jagged array object consists of these two arrays:

    - An aggregation of all the variable length sub-arrays into a single 1D array.
    - The offsets into the single 1D array, given by the sum of all the sub-array lengths up to and including the current sub-array.
    Often referred to as a "list-of-lists" or "array-of-arrays" construction.
    For example to store the following three arrays as a jagged array:
    (a b c)
    (d e f g)
    (h)
    Elements = (a b c d e f g h)
    Cumulative Length = (3 7 8)

    :ivar elements: 1D array of elements containing the aggregation of
        individual array data.
    :ivar cumulative_length: 1D array of cumulative lengths to the end
        of the current sub-array. Each cumulative length is also equal
        to the index of the first element of the next sub-array, i.e.,
        the index in the elements array for which the next variable
        length sub-array begins.
    """
    elements: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "Elements",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    cumulative_length: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CumulativeLength",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
