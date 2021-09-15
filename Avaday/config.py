# seed for random
RANDOM_SEED = 1828283

import numpy as np
np.seterr(all='raise')
np.random.seed(RANDOM_SEED)

# control density of paths
NUMBER_OF_PATHS = 3700
MAXIMAL_PATH_LENGTH = 200

# need to run model?
IS_ENABLED_CALCULATIONS = False 
IS_ENABLED_GA = True
IS_ENABLED_NEW_PATHS = True

# Length of board side
BOARD_SIZE = 100


# Set application root
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))