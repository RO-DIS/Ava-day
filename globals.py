# seed for random
random_seed = 1828283

import numpy as np
np.seterr(all='raise')
np.random.seed(random_seed)

number_of_paths = 3700
max_path_length = 200

# controls if needed to run ga
enable_calculations = False
enable_GA = False
enable_get_new_paths = False

board_size = 100

import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root