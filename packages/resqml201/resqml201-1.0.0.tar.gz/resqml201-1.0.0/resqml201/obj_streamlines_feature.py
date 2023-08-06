from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_technical_feature import AbstractTechnicalFeature
from resqml201.streamline_flux import StreamlineFlux
from resqml201.time_index import TimeIndex

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjStreamlinesFeature(AbstractTechnicalFeature):
    """Specification of the vector field upon which the streamlines are based.

    Streamlines are commonly used to trace the flow of phases (water /
    oil / gas / total) based upon their flux at a specified time. They
    may also be used for trace components for compositional simulation,
    e.g., CO2, or temperatures for thermal simulation. The flux
    enumeration provides support for the most usual cases with provision
    for extensions to other fluxes.

    :ivar flux: Specification of the streamline flux, drawn from the
        enumeration.
    :ivar other_flux: Optional specification of the streamline flux, if
        an extension is required beyond the enumeration. BUSINESS RULE:
        OtherFlux should appear if Flux has the value of other.
    :ivar time_index:
    """
    class Meta:
        name = "obj_StreamlinesFeature"

    flux: Optional[StreamlineFlux] = field(
        default=None,
        metadata={
            "name": "Flux",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    other_flux: Optional[str] = field(
        default=None,
        metadata={
            "name": "OtherFlux",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "TimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
