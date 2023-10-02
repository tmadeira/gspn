This directory contains code to replicate various image segmentation experiments using Python. Follow the instructions below to get started.

## Installation

First, make sure you have Python installed on your system. Then, install the required packages by running the following command:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Converting an Image to a Dataset**: Use `convert.py` to convert an image into a dataset. Here's an example of how to do it:

    ```bash
    python convert.py starry_night.jpg > starry_night.csv
    ```

2. **Image Segmentation with K-means**: To segment the image using the K-means algorithm, use `kmeans.py`. The second argument is `k`, representing the number of clusters. Here's an example:

    ```bash
    python kmeans.py starry_night.csv 4
    ```

3. **Learning a GSPN from the Image**: To learn a Gaussian Sum-Product Network (GSPN) from the image using SPFlow, use `learn.py`. The first argument is the CSV dataset, the second is the `min_instances_slice` parameter, and the third is the `threshold` parameter. The trained GSPN will be saved as a DILL file. Example:

    ```bash
    python learn.py starry_night.csv 500 0.3
    # The SPN will be saved to starry_night.dill.
    ```

4. **Image Segmentation with Modal EM**: To segment the image using the Modal EM algorithm, use `mem.py`. The first argument is the CSV dataset, and the second is a DILL file containing the SPN. Example:

    ```bash
    python mem.py starry_night.csv starry_night.dill
    ```

Other `.py` files in this repository contain various utilities that can be used to view, analyze, and recolorize the output of the segmentation algorithms.

