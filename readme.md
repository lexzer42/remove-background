# Background Removal with OpenCV

This project uses the GrabCut algorithm in OpenCV to remove the background from an image.

## Installation

This project requires Python and the following Python libraries installed:

- [OpenCV](https://opencv.org/)
- [NumPy](https://numpy.org/)

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](https://www.anaconda.com/distribution/) distribution of Python, which already has the above packages and more included.

To install the required packages, navigate to the project directory and run:

```sh
pip install opencv-python
```

## How it Works

1. The script first loads an image and creates a mask of the same size.
2. The user is asked to draw a bounding box around the object of interest. The GrabCut algorithm is then run with this bounding box to create an initial segmentation of the object.
3. The user can then refine the segmentation by drawing on the image. Left mouse button for drawing the areas that should be kept and right mouse button for the areas that should be removed.
4. After the user is done drawing, the GrabCut algorithm is run again with the new mask, and the final segmentation is displayed.

## Usage

To run the script, navigate to the project directory and run:

```sh
python remove_bg.py
```

Then follow the instructions in the script to select the object and refine the segmentation.