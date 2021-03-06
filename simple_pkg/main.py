import graphviz
import sklearn
import dask
import cv2
import dask.array as da
import numpy as np
import h5py


def main():
    print(graphviz.Digraph())
    dir(sklearn)
    _ = dask.arange(24).reshape(2,3,4)
    _ = cv2.__version__
    cwd = Path('.')
    print(cwd)

    # Create a black image
    img = np.zeros((512,512,3), np.uint8)

    # Draw a diagonal blue line with thickness of 5 px
    img = cv2.line(img,(0,0),(511,511),(255,0,0),5)


if __name__ == '__main__':
    main()
