from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22.abstract_geographic2d_crs import AbstractGeographic2DCrs
from resqml22.authority_qualified_name import AuthorityQualifiedName

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class GeodeticLocalAuthorityCrs(AbstractGeographic2DCrs):
    """This class contains a code for a geodetic CRS according to a local
    authority.

    This would be used in a case where a company or regulatory regime
    has chosen not to use EPSG codes.
    """
    local_authority_crs_name: Optional[AuthorityQualifiedName] = field(
        default=None,
        metadata={
            "name": "LocalAuthorityCrsName",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
