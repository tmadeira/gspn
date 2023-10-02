import sys
import warnings
import pandas as pd
import numpy as np
from cluster_utils import save_image_from_dataset
from spn.algorithms.LearningWrappers import learn_parametric
from spn.structure.Base import Context
from spn.structure.leaves.parametric.Parametric import Gaussian
from dill_utils import save


def main(csv: str):
    df = pd.read_csv(csv)
    png = csv.replace(".csv", ".png")
    save_image_from_dataset(df, png)


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1])
