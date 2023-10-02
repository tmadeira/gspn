import sys
import warnings
import pandas as pd
from spn.algorithms.LearningWrappers import learn_parametric
from spn.structure.Base import Context
from spn.structure.leaves.parametric.Parametric import Gaussian
from dill_utils import save


def main(csv: str, min_instances_slice: int, threshold: float):
    df = pd.read_csv(csv)
    np_array = df.to_numpy()
    context = Context(parametric_types=([Gaussian] * 5)).add_domains(np_array)
    spn = learn_parametric(
        np_array,
        context,
        rows="gmm",
        min_instances_slice=min_instances_slice,
        threshold=threshold,
    )
    dill_file = csv.replace(".csv", "_%d_%f.dill" % (min_instances_slice, threshold))
    save(spn, dill_file)
    print(dill_file)


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1], int(sys.argv[2]), float(sys.argv[3]))
