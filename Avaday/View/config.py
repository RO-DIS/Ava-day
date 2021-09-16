# resolution, <= 512
BOARD_SIZE = 100
# maximum height of points after scaling z-coordinates
BOARD_HEIGHT = 20
# width of lines on path
LINE_WIDTH = 3
# distance from origin for viewing pictures
VIEW_HEIGHT, VIEW_ELEVATION, VIEW_AZIMUTH = 110, 90, 0
# 125, 30, -30
# 125, 40, 180

# side of image
IMAGE_SIDE = 512

BACKGROUND_COLOR = 'k'

# sides of window
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700

from Avaday.config import ROOT_DIR, IMAGE_NAME

# path to image for map
PATH_TO_IMAGE = f"{ROOT_DIR}/resources/images/{IMAGE_NAME}.png"
PATH_TO_SAVED_IMAGE = f"{ROOT_DIR}/resources/output_images/{IMAGE_NAME}.png"

OUT_IMAGE_SIDE_IN_PIXELS = 1000

# seed for random
RANDOM_SEED = 1828283

import numpy as np
np.seterr(all='raise')
np.random.seed(RANDOM_SEED)

# Length of board side
BOARD_SIZE = 100
NUMBER_OF_PATHS = 3700