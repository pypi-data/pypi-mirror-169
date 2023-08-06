from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_double_array import AbstractDoubleArray
from resqml201.hdf5_dataset import Hdf5Dataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class DoubleHdf5Array(AbstractDoubleArray):
    """An array of double values provided explicitly by an HDF5 dataset.

    By convention, the null value is NaN.

    :ivar values: Reference to an HDF5 array of doubles.
    """
    values: Optional[Hdf5Dataset] = field(
        default=None,
        metadata={
            "name": "Values",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        }
    )
