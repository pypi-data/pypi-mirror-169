from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_cited_data_object import AbstractCitedDataObject

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class ObjEpcExternalPartReference(AbstractCitedDataObject):
    """It defines a proxy for external part of the EPC package.

    It must be used at least for external HDF parts.

    :ivar mime_type: IAMF registered, if one exists, or a free text
        field. Needs documentation on seismic especially. MIME type for
        HDF proxy is : application/x-hdf5 (by RESQML convention).
    """
    class Meta:
        name = "obj_EpcExternalPartReference"

    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "MimeType",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
