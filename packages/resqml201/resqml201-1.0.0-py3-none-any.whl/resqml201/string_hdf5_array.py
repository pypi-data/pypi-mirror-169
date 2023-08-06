from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.abstract_value_array import AbstractValueArray
from resqml201.hdf5_dataset import Hdf5Dataset

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StringHdf5Array(AbstractValueArray):
    """Used to store explicit string values, i.e., values that are not double,
    boolean or integers.

    The datatype of the values will be identified by means of the HDF5
    API.

    :ivar values: Reference to HDF5 array of integer or double
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
