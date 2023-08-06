from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_boolean_array import AbstractBooleanArray
from resqml201.hdf5_dataset import Hdf5Dataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BooleanHdf5Array(AbstractBooleanArray):
    """
    Array of boolean values provided explicitly by an HDF5 dataset.

    :ivar values: Reference to an HDF5 array of values.
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
