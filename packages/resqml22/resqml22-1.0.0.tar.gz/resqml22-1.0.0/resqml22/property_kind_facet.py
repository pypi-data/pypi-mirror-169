from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Union
from resqml22.facet import Facet
from resqml22.facet_kind import FacetKind

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class PropertyKindFacet:
    """Qualifiers for property values, which allow users to semantically
    specialize a property without creating a new property kind.

    For the list of enumerations, see FacetKind.

    :ivar facet: A facet allows you to better define a property in the
        context of its property kind. The technical advantage of using a
        facet vs. a specialized property kind is to limit the number of
        property kinds.
    :ivar kind: Facet kind of the property kind (see the enumeration)
    """
    facet: Optional[Union[Facet, str]] = field(
        default=None,
        metadata={
            "name": "Facet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r".*:.*",
        }
    )
    kind: Optional[FacetKind] = field(
        default=None,
        metadata={
            "name": "Kind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
