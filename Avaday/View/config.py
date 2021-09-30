# resolution, <= 512
BOARD_SIZE = 100
# maximum height of points after scaling z-coordinates
BOARD_HEIGHT = 20
# width of lines on path
LINE_WIDTH = 4
# distance from origin for viewing pictures
VIEW_HEIGHT, VIEW_ELEVATION, VIEW_AZIMUTH = 110, 90, 0
# 125, 30, -30
# 125, 40, 180

# side of image
IMAGE_SIDE = 512

# BACKGROUND_COLOR = 'k'
BACKGROUND_COLOR = 'w'

# sides of window
WINDOW_HEIGHT = 700
WINDOW_WIDTH = 700

OUT_IMAGE_SIDE_IN_PIXELS = 670

# seed for random
RANDOM_SEED = 1828283

import numpy as np
np.seterr(all='raise')
np.random.seed(RANDOM_SEED)

# Length of board side
BOARD_SIZE = 100
NUMBER_OF_PATHS = 3700