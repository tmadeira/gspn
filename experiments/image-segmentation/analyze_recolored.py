import sys
import warnings
import pandas as pd
from spn.structure.Base import Context
from spn.structure.leaves.parametric.Parametric import Gaussian
from dill_utils import save


def count_centers(df: pd.DataFrame):
    centers = set()
    for _, row in df.iterrows():
        centers.add(tuple(row[2:]))
    return len(centers)


def main(csv: str):
    df = pd.read_csv(csv)
    print(count_centers(df))


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1])
