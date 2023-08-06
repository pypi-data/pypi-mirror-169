from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class DigitalStorageUom(Enum):
    """
    :cvar BIT: bit
    :cvar BYTE: byte
    :cvar KIBYTE: kibibyte
    :cvar MIBYTE: mebibyte
    """
    BIT = "bit"
    BYTE = "byte"
    KIBYTE = "Kibyte"
    MIBYTE = "Mibyte"
