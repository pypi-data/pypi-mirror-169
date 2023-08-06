from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from resqml201.data_object_reference import DataObjectReference

__NAMESPACE__ = "http://www.energistics.org/energyml/data/commonv2"


@dataclass
class Hdf5Dataset:
    """
    :ivar path_in_hdf_file: The path of the referenced dataset in the
        HDF file. The separator between groups and final dataset is a
        slash '/'
    :ivar hdf_proxy:
    """
    path_in_hdf_file: Optional[str] = field(
        default=None,
        metadata={
            "name": "PathInHdfFile",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
    hdf_proxy: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "HdfProxy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/commonv2",
            "required": True,
        }
    )
