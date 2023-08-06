from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml22dev3.abstract_contact_interpretation_part import AbstractContactInterpretationPart
from resqml22dev3.contact_element_reference import ContactElementReference
from resqml22dev3.contact_verb import ContactVerb

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BinaryContactInterpretationPart(AbstractContactInterpretationPart):
    """The main class for data describing an opinion of the contact between two
    geologic feature-interpretations.

    - A contact interpretation between two surface geological boundaries is usually a line.
    - A contact interpretation between two volumes (rock feature-interpretation) is usually a surface.
    This class allows you to build a formal sentence—in the pattern of subject-verb-direct object—which is used to describe the construction of a node, line, or surface contact. It is also possible to attach a primary and a secondary qualifier to the subject and to the direct object.
    For more information, see the RESQML Technical Usage Guide.
    For example, one contact interpretation can be described by a sentence such as:
    The interpreted fault named F1 interp on its hanging wall side splits the interpreted horizon named H1 Interp on both its sides.
    Subject = F1 Interp, with qualifier "hanging wall side"
    Verb = splits
    Direct Object = H1 Interp, with qualifier "on both sides"

    :ivar direct_object: Data-object reference (by UUID link) to a
        geologic feature-interpretation, which is the direct object of
        the sentence that defines how the contact was constructed.
    :ivar subject: Data-object reference (by UUID link) to a geologic
        feature-interpretation, which is the subject of the sentence
        that defines how the contact was constructed.
    :ivar verb:
    """
    direct_object: Optional[ContactElementReference] = field(
        default=None,
        metadata={
            "name": "DirectObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    subject: Optional[ContactElementReference] = field(
        default=None,
        metadata={
            "name": "Subject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    verb: Optional[ContactVerb] = field(
        default=None,
        metadata={
            "name": "Verb",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
