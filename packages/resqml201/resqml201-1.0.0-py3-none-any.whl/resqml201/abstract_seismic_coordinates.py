from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractSeismicCoordinates:
    """Parent class is used to associate horizon and fault representations to
    seismic 2D and seismic 3D technical features.

    It stores a 1-to-1 mapping between geometry coordinates (usually X,
    Y, Z) and trace or inter-trace positions on a seismic survey.
    """
    seismic_support: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SeismicSupport",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
