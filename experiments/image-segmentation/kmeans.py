import sys
import warnings
import pandas as pd
from sklearn.cluster import KMeans
from cluster_utils import (
    plot_center_colors,
    save_image_from_dataset,
    recolor_using_cluster_centers,
)


def main(csv: str, k: int):
    dataset = pd.read_csv(csv)
    kmeans = KMeans(n_clusters=k).fit(dataset)
    centers = kmeans.cluster_centers_
    predictions = kmeans.predict(dataset)
    recolored = recolor_using_cluster_centers(dataset, predictions, centers)
    recolored_png = "k_%d_recolored_%s" % (k, csv.replace(".csv", ".png"))
    save_image_from_dataset(recolored, recolored_png)
    print(recolored_png)
    # plot_center_colors(centers)


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1], int(sys.argv[2]))
