from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_double_array import AbstractDoubleArray
from resqml201.abstract_representation import AbstractRepresentation
from resqml201.cell_fluid_phase_units import CellFluidPhaseUnits
from resqml201.data_object_reference import DataObjectReference
from resqml201.interval_stratigraphic_units import IntervalStratigraphicUnits

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class ObjWellboreFrameRepresentation(AbstractRepresentation):
    """Representation of a wellbore that is organized along a wellbore
    trajectory by its MD values.

    RESQML uses MD values to associate properties on points and to
    organize association of properties on intervals between MD points.

    :ivar node_count: Number of nodes. Must be positive.
    :ivar node_md: MD values for each node. BUSINESS RULE: MD values and
        UOM must be consistent with the trajectory representation.
    :ivar witsml_log_reference: The reference to the equivalent WITSML
        well log.
    :ivar interval_stratigraphi_units:
    :ivar cell_fluid_phase_units:
    :ivar trajectory:
    """
    class Meta:
        name = "obj_WellboreFrameRepresentation"

    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    node_md: Optional[AbstractDoubleArray] = field(
        default=None,
        metadata={
            "name": "NodeMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    witsml_log_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlLogReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    interval_stratigraphi_units: Optional[IntervalStratigraphicUnits] = field(
        default=None,
        metadata={
            "name": "IntervalStratigraphiUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    cell_fluid_phase_units: Optional[CellFluidPhaseUnits] = field(
        default=None,
        metadata={
            "name": "CellFluidPhaseUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
