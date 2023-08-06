from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.measure_class import MeasureType
from resqml22.string_measure import StringMeasure

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ExtensionNameValue:
    """Extension values Schema.

    The intent is to allow standard ML domain "named" extensions without
    having to modify the schema. A client or server can ignore any name
    that it does not recognize but certain metadata is required to allow
    generic clients or servers to process the value.

    :ivar name: The name of the extension. Each standard name should
        document the expected measure class. Each standard name should
        document the expected maximum size. For numeric values the size
        should be in terms of xsd types such as int, long, short, byte,
        float or double. For strings, the maximum length should be
        defined in number of characters. Local extensions to the list of
        standard names are allowed but it is strongly recommended that
        the names and definitions be approved by the respective SIG
        Technical Team before use.
    :ivar value: The value of the extension. This may also include a uom
        attribute. The content should conform to constraints defined by
        the data type.
    :ivar measure_class: The kind of the measure. For example, "length".
        This should be specified if the value requires a unit of
        measure.
    :ivar dtim: The date-time associated with the value.
    :ivar index: Indexes things with the same name. That is, 1 indicates
        the first one, 2 indicates the second one, etc.
    :ivar description: A textual description of the extension.
    """
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 64,
        }
    )
    value: Optional[StringMeasure] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    measure_class: Optional[MeasureType] = field(
        default=None,
        metadata={
            "name": "MeasureClass",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    dtim: Optional[str] = field(
        default=None,
        metadata={
            "name": "DTim",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
