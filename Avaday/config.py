# Set application root
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Parameters

# Widgets

# sizes of grid with paths
BOARD_SIZE = 100
# maximum height of points after scaling z-coordinates
BOARD_HEIGHT = 20
# width of lines
LINE_WIDTH = 4
# view point
VIEW_HEIGHT, VIEW_ELEVATION, VIEW_AZIMUTH = 110, 90, 0
# default background color
BACKGROUND_COLOR = 'k'
# sides of space view widget
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700


# Handlers

# valid side of square input image
IMAGE_SIDE = 512
# number of paths to read from file with paths
NUMBER_OF_PATHS = 3700

# side of saved picture
OUT_IMAGE_SIDE_IN_PIXELS = 670
