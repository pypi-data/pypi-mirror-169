from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CellFluidPhaseUnits:
    """
    A mapping from cells to fluid phase unit interpretation to describe the
    initial hydrostatic fluid column.

    :ivar phase_unit_indices: Index of the phase unit kind within a
        given fluid phase organization for each cell. Follows the
        indexing defined by the PhaseUnit enumeration. When applied to
        the wellbore frame representation, the indexing is identical to
        the number of intervals. Use null (-1) if no fluid phase is
        present, e.g., within the seal. BUSINESS RULE: Array length is
        equal to the number of cells in the representation (grid,
        wellbore frame or blocked well).
    :ivar fluid_organization:
    """
    phase_unit_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "PhaseUnitIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    fluid_organization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FluidOrganization",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
