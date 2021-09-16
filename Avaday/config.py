# seed for random
RANDOM_SEED = 1828283

import numpy as np
np.seterr(all='raise')
np.random.seed(RANDOM_SEED)

# Length of board side
BOARD_SIZE = 100

# Set application root
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_NAME = "hockey"