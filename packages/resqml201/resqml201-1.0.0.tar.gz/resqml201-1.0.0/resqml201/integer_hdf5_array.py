from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_integer_array import AbstractIntegerArray
from resqml201.hdf5_dataset import Hdf5Dataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class IntegerHdf5Array(AbstractIntegerArray):
    """Array of integer values provided explicitly by a HDF5 dataset.

    The null value is explicitly provided. WHERE IS THE NULL VALUE
    SPECIFIED?

    :ivar null_value:
    :ivar values: Reference to an HDF5 array of integers or doubles.
    """
    null_value: Optional[int] = field(
        default=None,
        metadata={
            "name": "NullValue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
    values: Optional[Hdf5Dataset] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
