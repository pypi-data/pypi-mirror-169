from __future__ import annotations
from enum import Enum

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


class OrganizationKind(Enum):
    """
    Kind of organization.
    """
    ACADEMIC_INSTITUTION = "academic institution"
    GOVERNMENT_AGENCY = "government agency"
    INDUSTRY_ORGANIZATION = "industry organization"
    NON_GOVERNMENTAL_ORGANIZATION = "non-governmental organization"
    ORGANIZATION_UNIT = "organization unit"
