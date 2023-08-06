from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class DataObjectReference:
    """
    It only applies for Energistics data object.

    :ivar content_type: The content type of the referenced element.
    :ivar title: The Title of the referenced object. The Title of a top
        level element would be inherited from AbstractObject and must be
        present on any referenced object.
    :ivar uuid: Reference to an object using its global UID.
    :ivar uuid_authority: The authority that issued and maintains the
        uuid of the referenced object. Used mainly in alias context.
    :ivar uri: This is the URI of a referenced object. Do not use this
        to store the path and file names of an external object - that is
        done through the External Dataset machinery. This element is
        intended for use with the Energistics Transfer Protocol.
    :ivar version_string: Indicates the version of the object which is
        referenced.
    """
    content_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContentType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "max_length": 2000,
        }
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uuid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    uuid_authority: Optional[str] = field(
        default=None,
        metadata={
            "name": "UuidAuthority",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
    uri: Optional[str] = field(
        default=None,
        metadata={
            "name": "Uri",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
        }
    )
    version_string: Optional[str] = field(
        default=None,
        metadata={
            "name": "VersionString",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "max_length": 64,
        }
    )
