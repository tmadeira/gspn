import multiprocessing
import sys
import warnings
from copy import deepcopy
from typing import Tuple
from joblib import Parallel, delayed
import numpy as np
from scipy.special import logsumexp
import pandas as pd
from analyze_recolored import count_centers
from cluster_utils import save_image_from_dataset

from spn.structure.Base import Leaf, Node, Product, Sum, get_topological_order
from spn.structure.leaves.parametric.Parametric import Gaussian
from spn.algorithms.Inference import log_likelihood

from dill_utils import load

MAX_STEPS = 30


def modal_em(root: Node, x_0: np.ndarray) -> np.ndarray:
    x_r = x_0
    for r in range(MAX_STEPS):
        prev = deepcopy(x_r)
        (nums, dems) = mem_step(root, x_r)
        x_r = np.exp(nums - dems)
        if np.linalg.norm(x_r - prev) < 1:
            break

    return x_r


def mem_step(root: Node, x: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    n = len(x)
    nodes = get_topological_order(root)
    nums = np.zeros((len(nodes), n))
    dems = np.zeros((len(nodes), n))
    for node in nodes:
        if isinstance(node, Gaussian):
            ll = log_likelihood(node, np.array([x]))
            nums[node.id] = np.repeat(ll, n)
            dems[node.id] = np.repeat(ll, n)
            i = node.scope[0]
            nums[node.id][i] += np.log(node.mean) - 2 * np.log(node.stdev)
            dems[node.id][i] -= 2 * np.log(node.stdev)
        elif isinstance(node, Product):
            for c in node.children:
                nums[node.id] += nums[c.id]
                dems[node.id] += dems[c.id]
        else:
            assert isinstance(node, Sum)
            eval_children = np.array([(nums[c.id], dems[c.id]) for c in node.children])
            for i in range(len(node.children)):
                eval_children[i] += np.log(node.weights[i])
            nums_children = np.transpose(
                np.array(list(map(lambda c: c[0], eval_children)))
            )
            dems_children = np.transpose(
                np.array(list(map(lambda c: c[1], eval_children)))
            )
            nums[node.id] = np.array([logsumexp(nums_children[i]) for i in range(n)])
            dems[node.id] = np.array([logsumexp(dems_children[i]) for i in range(n)])
    return (nums[root.id], dems[root.id])


def process(spn: Node, row):
    x = row.to_numpy()
    center = modal_em(spn, x)
    rounded_center = np.rint(center).astype(int)
    row["r"] = rounded_center[2]
    row["g"] = rounded_center[3]
    row["b"] = rounded_center[4]
    return row


def main(csv: str, spn_dill: str):
    dataset = pd.read_csv(csv)
    spn = load(spn_dill)
    num_cores = multiprocessing.cpu_count()

    recolored_rows = Parallel(n_jobs=num_cores)(
        delayed(process)(spn, row) for _, row in list(dataset.iterrows())
    )

    centers = set()
    for row in recolored_rows:
        centers.add(tuple(row))

    df = pd.DataFrame(recolored_rows)
    recolored_csv = "mem_recolored_" + spn_dill.replace(".dill", ".csv")
    recolored_png = "mem_recolored_" + spn_dill.replace(".dill", ".png")
    df.to_csv(recolored_csv, index=False)
    save_image_from_dataset(df, recolored_png)
    print(count_centers(df), recolored_csv, recolored_png)
    # plot_center_colors(centers)


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1], sys.argv[2])
