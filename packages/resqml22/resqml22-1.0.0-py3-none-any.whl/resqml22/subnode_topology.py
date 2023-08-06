from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from resqml22.uniform_subnode_patch import UniformSubnodePatch
from resqml22.variable_subnode_patch import VariableSubnodePatch

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SubnodeTopology:
    """
    Finite element subnode topology for an unstructured cell can be either
    variable or uniform, but not columnar.
    """
    variable_subnode_patch: List[VariableSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "VariableSubnodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
    uniform_subnode_patch: List[UniformSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "UniformSubnodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        }
    )
