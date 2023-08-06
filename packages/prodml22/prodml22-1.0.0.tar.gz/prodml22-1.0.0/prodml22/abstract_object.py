from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Union
from prodml22.citation import Citation
from prodml22.custom_data import CustomData
from prodml22.existence_kind import ExistenceKind
from prodml22.extension_name_value import ExtensionNameValue
from prodml22.object_alias import ObjectAlias
from prodml22.osduintegration import Osduintegration

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class AbstractObject:
    """
    The parent class for all top-level elements across the Energistics MLs.

    :ivar aliases:
    :ivar citation: Use the citation data element to optionally add
        simple authorship metadata to any Energistics object. The
        citation data object uses attributes like title, originator,
        editor, last update, etc. from the Energy Industry Profile of
        ISO 19115-1 (EIP).
    :ivar existence: A lifecycle state like actual, required, planned,
        predicted, etc. This is used to qualify any top-level element
        (from Epicentre 2.1).
    :ivar object_version_reason: An optiona, human-readable reason why
        this version of the object was created.
    :ivar business_activity_history: Business processes/workflows that
        the data object has been through (ex. well planning,
        exploration).
    :ivar osduintegration:
    :ivar custom_data:
    :ivar extension_name_value:
    :ivar uuid: A universally unique identifier (UUID) as defined by RFC
        4122. For rules and guidelines about the format of UUIDs with
        the current version of Energistics standards, see the
        Energistics Identifier Specification v5.0. IMMUTABLE. Set on
        object creation and MUST NOT change thereafter. Customer
        provided changes after creation are an error.
    :ivar schema_version: The version of the Energistics schema used for
        a data object. The schema version is the first 2 digits of an ML
        version. EXAMPLES: - For WITSML v2.0 the schema version is 20 -
        For RESQML v2.0.1 the schema version is 20
    :ivar object_version:
    """
    aliases: List[ObjectAlias] = field(
        default_factory=list,
        metadata={
            "name": "Aliases",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    citation: Optional[Citation] = field(
        default=None,
        metadata={
            "name": "Citation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    existence: Optional[Union[ExistenceKind, str]] = field(
        default=None,
        metadata={
            "name": "Existence",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "pattern": r".*:.*",
        }
    )
    object_version_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "ObjectVersionReason",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 2000,
        }
    )
    business_activity_history: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BusinessActivityHistory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    osduintegration: Optional[Osduintegration] = field(
        default=None,
        metadata={
            "name": "OSDUIntegration",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    custom_data: Optional[CustomData] = field(
        default=None,
        metadata={
            "name": "CustomData",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    extension_name_value: List[ExtensionNameValue] = field(
        default_factory=list,
        metadata={
            "name": "ExtensionNameValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    schema_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "schemaVersion",
            "type": "Attribute",
            "required": True,
            "max_length": 64,
        }
    )
    object_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "objectVersion",
            "type": "Attribute",
            "max_length": 64,
        }
    )
