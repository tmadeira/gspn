import sys
import warnings
from copy import deepcopy
from typing import Tuple

from spn.structure.Base import Leaf, Node, Product, Sum, get_topological_order
from spn.structure.leaves.parametric.Parametric import Gaussian
from spn.algorithms.Inference import log_likelihood
from spn.io.Graphics import plot_spn

from dill_utils import load


def get_stats(spn: Node):
    nodes = get_topological_order(spn)

    height = {}
    for node in nodes:
        if isinstance(node, Leaf):
            height[node.id] = 1
        else:
            height[node.id] = max(map(lambda v: height[v.id], node.children)) + 1

    return {
        "variables": len(spn.scope),
        "height": height[spn.id],
        "nodes": len(nodes),
        "sum_nodes": len(list(filter(lambda node: isinstance(node, Sum), nodes))),
        "product_nodes": len(list(filter(lambda node: isinstance(node, Product), nodes))),
        "leaf_nodes": len(list(filter(lambda node: isinstance(node, Leaf), nodes))),
    }


def main(spn_dill: str):
    spn = load(spn_dill)

    stats = get_stats(spn)

    print("Random variables:", stats["variables"])
    print("Height:", stats["height"])
    print("Nodes:", stats["nodes"])
    print("  Sum nodes:", stats["sum_nodes"])
    print("  Product nodes:", stats["product_nodes"])
    print("  Leaf nodes:", stats["leaf_nodes"])


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1])
