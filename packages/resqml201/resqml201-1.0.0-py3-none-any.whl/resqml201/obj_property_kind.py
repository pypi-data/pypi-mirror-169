from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_property_kind import AbstractPropertyKind
from resqml201.abstract_resqml_data_object import AbstractResqmlDataObject
from resqml201.resqml_uom import ResqmlUom

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjPropertyKind(AbstractResqmlDataObject):
    """A description of a property name relative to a standard definition.

    For example, you may specify if the property kind is abstract, the
    dictionary in which the property is unique, and the representative
    unit of measure.

    :ivar naming_system: The name of the dictionary within which the
        property is unique. This also defines the name of the
        controlling authority. Use a URN of the form
        "urn:x-resqml:domainOrEmail:dictionaryName". An example public
        dictionary: "urn:resqml:energistics.org:RESQML" assigned to
        values defined by ResqmlPropertyKind. An example corporate
        dictionary: "urn:resqml:slb.com:product-x". An example personal
        dictionary:
        "urn:resqml:first.last@mycompany.com:my.first.dictionary". The
        purpose of this scheme is to generate a unique name. Parsing for
        semantics is not intended.
    :ivar is_abstract: A value of true indicates that the property kind
        is abstract and an instance of property values must not
        represent this kind. A value of false indicates otherwise (i.e.,
        that an instance of property values may represent this kind).
    :ivar representative_uom: Generally matches the base for conversion,
        except where multiple classes have the same underlying
        dimensional analysis. In this case, the representative unit may
        provide additional information about the underlying concept of
        the class. For example, "area per volume" has the same
        dimensional analysis as "per length", but it specifies a
        representative unit of "m2/m3" instead of "1/m".
    :ivar parent_property_kind:
    """
    class Meta:
        name = "obj_PropertyKind"

    naming_system: Optional[str] = field(
        default=None,
        metadata={
            "name": "NamingSystem",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    is_abstract: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAbstract",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    representative_uom: Optional[ResqmlUom] = field(
        default=None,
        metadata={
            "name": "RepresentativeUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    parent_property_kind: Optional[AbstractPropertyKind] = field(
        default=None,
        metadata={
            "name": "ParentPropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
