import sys
import warnings
import pandas as pd
import numpy as np
from spn.algorithms.LearningWrappers import learn_parametric
from spn.structure.Base import Context
from spn.structure.leaves.parametric.Parametric import Gaussian
from dill_utils import save


def fix_colors(original: pd.DataFrame, recolored: pd.DataFrame):
    points = {}
    for _, row in recolored.iterrows():
        points[tuple(row[0:2])] = tuple(row[2:])

    colors = {}
    for _, row in original.iterrows():
        cur_center = points[tuple(row[0:2])]
        if cur_center not in colors:
            colors[cur_center] = []
        colors[cur_center].append(tuple(row[2:]))

    mean = {}
    for center, point_colors in colors.items():
        mean[center] = np.rint(np.mean(point_colors, axis=0)).astype(int)

    for _, row in recolored.iterrows():
        new_colors = mean[tuple(row[2:])]
        row[2:] = new_colors

    return recolored


def main(csv: str, recolored_csv: str):
    original = pd.read_csv(csv)
    recolored = pd.read_csv(recolored_csv)
    new_recolored = fix_colors(original, recolored)
    new_recolored.to_csv("fixed_" + recolored_csv, index=False)


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1], sys.argv[2])
