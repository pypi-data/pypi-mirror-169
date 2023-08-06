from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml201.uniform_subnode_patch import UniformSubnodePatch
from resqml201.variable_subnode_patch import VariableSubnodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SubnodeTopology:
    """
    Finite element subnode topology for an unstructured cell can be either
    variable or uniform, but not columnar.
    """
    variable_subnodes: List[VariableSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "VariableSubnodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    uniform_subnodes: List[UniformSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "UniformSubnodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
