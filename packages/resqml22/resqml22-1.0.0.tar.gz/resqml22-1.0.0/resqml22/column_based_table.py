from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.abstract_object import AbstractObject
from resqml22.column import Column

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ColumnBasedTable(AbstractObject):
    """A column-based table allows the exchange of tables, where the values are
    arranged against columns that are defined by PropertyKind, UOM and Facet.

    EXAMPLES: KrPc table and facies tables.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    column: List[Column] = field(
        default_factory=list,
        metadata={
            "name": "Column",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    key_column: List[Column] = field(
        default_factory=list,
        metadata={
            "name": "KeyColumn",
            "type": "Element",
        }
    )
