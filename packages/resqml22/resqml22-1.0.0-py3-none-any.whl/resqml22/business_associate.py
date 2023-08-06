from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from resqml22.abstract_object import AbstractObject
from resqml22.email_qualifier_struct import EmailQualifierStruct
from resqml22.general_address import GeneralAddress
from resqml22.name_struct import NameStruct
from resqml22.organization_kind import OrganizationKind
from resqml22.person_name import PersonName
from resqml22.phone_number_struct import PhoneNumberStruct

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class BusinessAssociate(AbstractObject):
    """Describes any company, person, group, consultant, etc., which is
    associated within a context (e.g., a well).

    The information contained in this module is: (1) contact
    information, such as address, phone numbers, email, (2) alternate
    name, or aliases, and (3) associations, such as the business
    associate that this one is associated with, or a contact who is
    associated with this business associate.

    :ivar name: Name of the business associate.
    :ivar authority_code: The code used when this business associate is
        used as an authority attribute or extensible enumeration
        authority within Energistics standards.
    :ivar organization_kind: The kind of organizational structure the
        business associate fits into. Typical values include: Operating
        Unit, Operating sub Unit, A Business, A Department, Government
        Agency, etc.
    :ivar role: The role of the business associate within the context.
        For example, "driller" or "operator", "lead agency - CEQA
        compliance" "regulatory contact", "safety contact". A business
        associate generally has one role but the role may be called
        different things in different naming systems.
    :ivar address: The business address.
    :ivar contact: A pointer to a business associate (generally a
        person) who serves as a contact for this business associate.
    :ivar phone_number: Various types of phone numbers may be given.
        They may be office or home, they may be a number for a cell
        phone, or for a fax, etc. Attributes of PhoneNumber declare the
        type of phone number that is being given.
    :ivar email: The email address may be home, office, or permanent.
        More than one may be given.
    :ivar effective_date_time: The date and time when the business
        associate became effective (e.g., the date it was founded).
    :ivar termination_date_time: The data and time when the business
        associate ceased to be effective (e.g., the date when it was
        acquired by another company).
    :ivar purpose: The reason the business associate was formed.
    :ivar is_internal: Indicates if the business associate is internal
        to the enterprise.
    :ivar associated_with: A pointer to another business associate that
        this business associate is associated with. The most common
        situation is that of an employee being associated with a
        company. But it may also be, for example, a work group
        associated with a university.
    :ivar personnel_count: The count of personnel in a group.
    :ivar person_name: The components of a person's name.
    """
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/commonv2"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "required": True,
            "max_length": 256,
        }
    )
    authority_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthorityCode",
            "type": "Element",
            "max_length": 64,
        }
    )
    organization_kind: Optional[Union[OrganizationKind, str]] = field(
        default=None,
        metadata={
            "name": "OrganizationKind",
            "type": "Element",
            "pattern": r".*:.*",
        }
    )
    role: List[NameStruct] = field(
        default_factory=list,
        metadata={
            "name": "Role",
            "type": "Element",
        }
    )
    address: Optional[GeneralAddress] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    contact: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Contact",
            "type": "Element",
            "max_length": 64,
        }
    )
    phone_number: List[PhoneNumberStruct] = field(
        default_factory=list,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
        }
    )
    email: List[EmailQualifierStruct] = field(
        default_factory=list,
        metadata={
            "name": "Email",
            "type": "Element",
        }
    )
    effective_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "EffectiveDateTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    termination_date_time: Optional[str] = field(
        default=None,
        metadata={
            "name": "TerminationDateTime",
            "type": "Element",
            "pattern": r".+T.+[Z+\-].*",
        }
    )
    purpose: Optional[str] = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Element",
            "max_length": 2000,
        }
    )
    is_internal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsInternal",
            "type": "Element",
        }
    )
    associated_with: Optional[str] = field(
        default=None,
        metadata={
            "name": "AssociatedWith",
            "type": "Element",
            "max_length": 64,
        }
    )
    personnel_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonnelCount",
            "type": "Element",
        }
    )
    person_name: Optional[PersonName] = field(
        default=None,
        metadata={
            "name": "PersonName",
            "type": "Element",
        }
    )
