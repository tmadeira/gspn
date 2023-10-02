import numpy as np
import pandas as pd
from PIL import Image


DEFAULT_WIDTH = 600
DEFAULT_HEIGHT = 150


def plot_center_colors(centers: np.ndarray):
    image = Image.new(mode="RGB", size=(DEFAULT_WIDTH, DEFAULT_HEIGHT))
    for idx, center in enumerate(centers):
        r, g, b = np.rint(center[2:5]).astype(int)
        color = Image.new(
            mode="RGB",
            size=(DEFAULT_WIDTH // len(centers), DEFAULT_HEIGHT),
            color=(r, g, b),
        )
        image.paste(color, (idx * DEFAULT_WIDTH // len(centers), 0))
    image.show()


def recolor_using_cluster_centers(
    dataset: pd.DataFrame, predictions: np.ndarray, centers: np.ndarray
):
    centers_rgb = np.rint(centers).astype(int)[:, 2:]
    recolored = dataset.assign(prediction=predictions)
    recolored["r"] = recolored["prediction"].map(
        lambda prediction: centers_rgb[prediction][0]
    )
    recolored["g"] = recolored["prediction"].map(
        lambda prediction: centers_rgb[prediction][1]
    )
    recolored["b"] = recolored["prediction"].map(
        lambda prediction: centers_rgb[prediction][2]
    )
    return recolored.drop("prediction", axis=1)


def make_image_from_dataset(dataset: pd.DataFrame):
    width = dataset["j"].max() + 1
    height = dataset["i"].max() + 1
    image = Image.new(mode="RGB", size=(width, height))
    pixels = image.load()
    for _, row in dataset.iterrows():
        pixels[row["j"], row["i"]] = (row["r"], row["g"], row["b"])
    return image


def plot_image_from_dataset(dataset: pd.DataFrame):
    image = make_image_from_dataset(dataset)
    image.show()


def save_image_from_dataset(dataset: pd.DataFrame, filename: str):
    image = make_image_from_dataset(dataset)
    image.save(filename)
