from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_parent_window import AbstractParentWindow
from resqml201.abstract_representation import AbstractRepresentation
from resqml201.cell_fluid_phase_units import CellFluidPhaseUnits
from resqml201.cell_stratigraphic_units import CellStratigraphicUnits

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractGridRepresentation(AbstractRepresentation):
    """
    Abstract class for all grid representations.
    """
    cell_fluid_phase_units: Optional[CellFluidPhaseUnits] = field(
        default=None,
        metadata={
            "name": "CellFluidPhaseUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    parent_window: Optional[AbstractParentWindow] = field(
        default=None,
        metadata={
            "name": "ParentWindow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    cell_stratigraphic_units: Optional[CellStratigraphicUnits] = field(
        default=None,
        metadata={
            "name": "CellStratigraphicUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
