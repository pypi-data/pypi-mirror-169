from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_representation import AbstractRepresentation
from resqml201.streamline_polyline_set_patch import StreamlinePolylineSetPatch
from resqml201.streamline_wellbores import StreamlineWellbores

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStreamlinesRepresentation(AbstractRepresentation):
    """Representation of streamlines associated with a streamline feature and
    interpretation.

    Use StreamlinesFeature to define the vector field that supports the
    streamlines, i.e., describes what flux is being traced. Use
    Interpretation to distinguish between shared and differing
    interpretations. Usage Note: When defining streamline geometry, the
    PatchIndex will not be referenced, and may be set to a value of 0.

    :ivar line_count: Number of streamlines.
    :ivar streamline_wellbores:
    :ivar geometry:
    """
    class Meta:
        name = "obj_StreamlinesRepresentation"

    line_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    streamline_wellbores: Optional[StreamlineWellbores] = field(
        default=None,
        metadata={
            "name": "StreamlineWellbores",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    geometry: Optional[StreamlinePolylineSetPatch] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
