import sys
import warnings
from PIL import Image
import numpy as np


def main(image: str):
    print("i,j,r,g,b")
    with Image.open(image) as im:
        pixels = np.array(im)
        for i, row in enumerate(pixels):
            for j, val in enumerate(row):
                print("%d,%d,%d,%d,%d" % (i, j, val[0], val[1], val[2]))


if __name__ == "__main__":
    warnings.simplefilter("ignore")
    main(sys.argv[1])
 