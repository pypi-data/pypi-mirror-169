from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_tvd_interval import AbstractTvdInterval
from resqml22.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DatumTvdInterval(AbstractTvdInterval):
    """
    :ivar datum: The datum the TVD interval is referenced to. Required
        when there is no default TVD datum associated with the data
        object this is used in.
    """
    datum: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Datum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
