from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_string_array import AbstractStringArray
from resqml22.external_data_array import ExternalDataArray

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class StringExternalArray(AbstractStringArray):
    """Used to store explicit string values, i.e., values that are not double,
    boolean or integers.

    The datatype of the values will be identified by means of the HDF5
    API.

    :ivar count_per_value:
    :ivar values: Reference to HDF5 array of integer or double
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
