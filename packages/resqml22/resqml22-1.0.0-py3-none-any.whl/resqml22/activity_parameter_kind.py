from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class ActivityParameterKind(Enum):
    DATA_OBJECT = "dataObject"
    DOUBLE = "double"
    INTEGER = "integer"
    STRING = "string"
    TIMESTAMP = "timestamp"
    SUB_ACTIVITY = "subActivity"
